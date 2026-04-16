#!/usr/bin/env python3
"""
LTV / ARPU / ROAS / Breakeven calculator for mobile subscription apps.

Companion to modules/unit-economics-calculator.md. Run from Bash:

    python3 tools/ltv-calculator.py

Or import in another script:

    from ltv_calculator import calculate, Plan
    plans = [Plan("annual", 89.99, 0.25), Plan("monthly", 19.99, 0.75)]
    result = calculate(plans, monthly_installs=40000, cr_to_purchase=0.06, cpi=3.0)
    print(result.summary())

Defaults sourced from:
- Adapty State of In-App Subscriptions 2026 (16K apps, $3B revenue)
- RevenueCat State of Subscription Apps 2026 (115K apps)
- AppsFlyer State of Subscriptions 2026 (1.7B installs)
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from typing import Literal

PlanType = Literal["weekly", "monthly", "quarterly", "annual", "lifetime"]
TIME_HORIZONS = ["7d", "1mo", "3mo", "6mo", "1yr", "2yr", "3yr", "4yr"]

# Default cumulative renewal multipliers per plan type per time horizon.
# "Cumulative renewals" = total payment cycles AFTER the first purchase.
# So total payments = 1 (initial) + cumulative_renewals.
# Source: Adapty 2026 + RC 2026 cross-referenced.
DEFAULT_RETENTION = {
    "weekly": {
        "7d": 0.0,
        "1mo": 2.0,
        "3mo": 4.5,
        "6mo": 7.0,
        "1yr": 10.0,
        "2yr": 13.0,
        "3yr": 15.0,
        "4yr": 16.0,
    },
    "monthly": {
        "7d": 0.0,
        "1mo": 0.4,
        "3mo": 0.7,
        "6mo": 1.0,
        "1yr": 1.6,
        "2yr": 2.0,
        "3yr": 2.2,
        "4yr": 2.3,
    },
    "quarterly": {
        "7d": 0.0,
        "1mo": 0.0,
        "3mo": 0.15,
        "6mo": 0.2,
        "1yr": 0.35,
        "2yr": 0.4,
        "3yr": 0.45,
        "4yr": 0.42,
    },
    "annual": {
        "7d": 0.0,
        "1mo": 0.0,
        "3mo": 0.0,
        "6mo": 0.0,
        "1yr": 0.1,
        "2yr": 0.13,
        "3yr": 0.15,
        "4yr": 0.16,
    },
    "lifetime": {h: 0.0 for h in TIME_HORIZONS},  # no renewals
}

# Adapty 2026 LTV by category (12-month, all plans combined).
CATEGORY_LTV_BENCHMARK = {
    "productivity": 46.97,
    "utilities": 46.30,
    "education": 45.10,
    "health_fitness": 46.00,
    "photo_video": 42.00,
    "lifestyle": 43.00,
    "graphics_design": 39.00,
    "entertainment": 35.00,
    "ai": 49.92,  # RC 2026
    "gaming": 11.22,  # RC 2026
}


@dataclass
class Plan:
    plan_type: PlanType
    price: float
    distribution: float  # 0.0 to 1.0


@dataclass
class CalculatorResult:
    inputs: dict
    blended_arppu: dict[str, float]  # by horizon
    arpu_net: dict[str, float]
    revenue: dict[str, float]
    roas: dict[str, float]
    cac: float
    breakeven_horizon: str | None
    ltv_to_cac_4yr: float
    grades: dict[str, str]
    advice: list[str]

    def summary(self) -> str:
        lines = []
        lines.append("=" * 72)
        lines.append("UNIT ECONOMICS CALCULATOR — RESULTS")
        lines.append("=" * 72)
        lines.append("")

        lines.append("Inputs:")
        for k, v in self.inputs.items():
            lines.append(f"  {k}: {v}")
        lines.append("")

        # Table
        header = f"{'Metric':<16} " + " ".join(f"{h:>9}" for h in TIME_HORIZONS)
        lines.append(header)
        lines.append("-" * len(header))
        lines.append(
            f"{'Blended ARPPU':<16} "
            + " ".join(f"${self.blended_arppu[h]:>8.2f}" for h in TIME_HORIZONS)
        )
        lines.append(
            f"{'ARPU (net)':<16} "
            + " ".join(f"${self.arpu_net[h]:>8.2f}" for h in TIME_HORIZONS)
        )
        lines.append(
            f"{'Revenue':<16} "
            + " ".join(f"${self.revenue[h]:>8,.0f}" for h in TIME_HORIZONS)
        )
        lines.append(
            f"{'ROAS':<16} " + " ".join(f"{self.roas[h]:>8.2f}x" for h in TIME_HORIZONS)
        )
        lines.append("")

        lines.append(f"CAC: ${self.cac:.2f}")
        if self.breakeven_horizon:
            lines.append(
                f"Breakeven: {self.breakeven_horizon} (first horizon where ROAS >= 1.0)"
            )
        else:
            lines.append("Breakeven: Not reached within 4 years")
        lines.append(f"LTV:CAC (4yr): {self.ltv_to_cac_4yr:.2f}:1")
        lines.append("")

        lines.append("Performance grades:")
        for k, v in self.grades.items():
            lines.append(f"  {k}: {v}")
        lines.append("")

        if self.advice:
            lines.append("Top recommendations:")
            for i, a in enumerate(self.advice, 1):
                lines.append(f"  {i}. {a}")

        lines.append("=" * 72)
        return "\n".join(lines)


def grade_cr(cr: float) -> str:
    if cr >= 0.08:
        return "Excellent"
    elif cr >= 0.05:
        return "Good"
    elif cr >= 0.03:
        return "Average"
    else:
        return "Below average"


def grade_trial_start(rate: float) -> str:
    if rate >= 0.14:
        return "Excellent (NA benchmark)"
    elif rate >= 0.10:
        return "Good"
    elif rate >= 0.07:
        return "Average"
    else:
        return "Below average"


def grade_trial_to_paid(rate: float) -> str:
    if rate >= 0.40:
        return "Excellent"
    elif rate >= 0.28:
        return "Good"
    elif rate >= 0.15:
        return "Average"
    else:
        return "Poor"


def grade_breakeven(horizon: str | None) -> str:
    if horizon is None:
        return "Critical — unit economics broken"
    order = {
        "7d": 0,
        "1mo": 1,
        "3mo": 2,
        "6mo": 3,
        "1yr": 4,
        "2yr": 5,
        "3yr": 6,
        "4yr": 7,
    }
    n = order[horizon]
    if n <= 2:
        return "Exceptional — scale aggressively"
    elif n <= 3:
        return "Excellent — healthy economics"
    elif n <= 4:
        return "Normal — sustainable"
    elif n <= 5:
        return "Warning — long payback"
    else:
        return "Critical — fix before paid UA"


def grade_ltv_cac(ratio: float) -> str:
    if ratio > 5:
        return "Strong — likely underinvesting in growth"
    elif ratio >= 3:
        return "Healthy — sustainable economics"
    elif ratio >= 2:
        return "Marginal — optimize before scaling"
    else:
        return "Unprofitable — fix LTV side first"


def calculate(
    plans: list[Plan],
    monthly_installs: float,
    cr_to_purchase: float | None = None,
    trial_start_rate: float | None = None,
    trial_to_paid_rate: float | None = None,
    cpi: float = 2.50,
    apple_fee: float = 0.15,
    custom_retention: dict | None = None,
) -> CalculatorResult:
    """
    Run the full unit-economics calculation.

    Either cr_to_purchase OR (trial_start_rate AND trial_to_paid_rate) must be provided.
    If both are provided, trial funnel takes precedence.
    """
    # Validate distributions sum to ~1.0
    total_dist = sum(p.distribution for p in plans)
    if abs(total_dist - 1.0) > 0.01:
        raise ValueError(f"Plan distributions must sum to 1.0, got {total_dist:.3f}")

    # Determine effective CR
    if trial_start_rate is not None and trial_to_paid_rate is not None:
        effective_cr = trial_start_rate * trial_to_paid_rate
    elif cr_to_purchase is not None:
        effective_cr = cr_to_purchase
    else:
        raise ValueError(
            "Provide either cr_to_purchase or (trial_start_rate AND trial_to_paid_rate)"
        )

    retention = custom_retention or DEFAULT_RETENTION

    # Per-plan LTV at each horizon
    blended_arppu = {}
    for h in TIME_HORIZONS:
        total = 0.0
        for plan in plans:
            cum_renewals = retention.get(plan.plan_type, {}).get(h, 0.0)
            ltv_plan = plan.price * (1 + cum_renewals)
            total += ltv_plan * plan.distribution
        blended_arppu[h] = total

    arpu_net = {h: blended_arppu[h] * (1 - apple_fee) for h in TIME_HORIZONS}
    revenue = {h: monthly_installs * effective_cr * arpu_net[h] for h in TIME_HORIZONS}
    roas = {
        h: (effective_cr * arpu_net[h]) / cpi if cpi > 0 else 0 for h in TIME_HORIZONS
    }

    # Breakeven
    breakeven_horizon = None
    for h in TIME_HORIZONS:
        if roas[h] >= 1.0:
            breakeven_horizon = h
            break

    cac = cpi / effective_cr if effective_cr > 0 else float("inf")
    ltv_to_cac_4yr = arpu_net["4yr"] / cac if cac > 0 else 0

    # Grades
    grades = {
        "Effective CR": f"{effective_cr*100:.2f}% — {grade_cr(effective_cr)}",
        "Breakeven": grade_breakeven(breakeven_horizon),
        "LTV:CAC (4yr)": f"{ltv_to_cac_4yr:.2f}:1 — {grade_ltv_cac(ltv_to_cac_4yr)}",
    }
    if trial_start_rate is not None:
        grades["Trial Start Rate"] = (
            f"{trial_start_rate*100:.2f}% — {grade_trial_start(trial_start_rate)}"
        )
    if trial_to_paid_rate is not None:
        grades["Trial-to-Paid"] = (
            f"{trial_to_paid_rate*100:.2f}% — {grade_trial_to_paid(trial_to_paid_rate)}"
        )

    # Advice engine
    advice = []
    if ltv_to_cac_4yr < 2:
        advice.append(
            f"LTV:CAC of {ltv_to_cac_4yr:.2f}:1 is unprofitable. "
            f"Don't increase UA spend. Fix pricing, plan mix, or retention first."
        )
    elif ltv_to_cac_4yr < 3:
        advice.append(
            f"LTV:CAC of {ltv_to_cac_4yr:.2f}:1 is marginal. "
            f"Test +20-30% on highest-distribution plan. Pricing has 45.5% A/B win rate (Adapty)."
        )
    elif ltv_to_cac_4yr > 5:
        advice.append(
            f"LTV:CAC of {ltv_to_cac_4yr:.2f}:1 is strong — likely underinvesting in growth. "
            f"You could increase CPI to ${arpu_net['4yr']/3:.2f} and still maintain healthy 3:1."
        )

    annual_share = sum(p.distribution for p in plans if p.plan_type == "annual")
    monthly_share = sum(p.distribution for p in plans if p.plan_type == "monthly")
    if annual_share < 0.20 and monthly_share > 0.30:
        advice.append(
            f"Only {annual_share*100:.0f}% choose annual; annual delivers ~Nx LTV of monthly. "
            f"Restructure paywall: default to annual + savings callout. "
            f"Plan duration A/B win rate: 58.7% (Adapty)."
        )

    if breakeven_horizon is None or breakeven_horizon in ("3yr", "4yr"):
        advice.append(
            f"Breakeven slow ({breakeven_horizon or 'never'}). "
            f"Add a weekly plan with free trial — weekly captures 55.5% of all subscription revenue. "
            f"Weekly+trial 12-mo LTV $49.27."
        )

    if apple_fee >= 0.30:
        advice.append(
            "You're paying 30% Apple fee. If revenue <$1M annually, switch to "
            "Small Business Program (15% rate) — instant +17.6% net ARPU. "
            "Apply: https://developer.apple.com/app-store/small-business-program/"
        )

    if trial_start_rate is not None and trial_start_rate < 0.10:
        advice.append(
            f"Trial Start Rate {trial_start_rate*100:.1f}% below 11.2% global / 14.5% NA. "
            f"Paywall not compelling. Test stronger benefit copy, video bg (8-15% lift per Adapty), "
            f"or hard paywall."
        )

    if trial_to_paid_rate is not None and trial_to_paid_rate < 0.20:
        advice.append(
            f"Trial-to-Paid {trial_to_paid_rate*100:.1f}% well below 27.8% benchmark. "
            f"Check: trial too long (forget to cancel), value not hit in first 2-3 days, "
            f"missing pre-expiry reminder (Blinkist Day-5 push lifted notif opt-in 1,200%)."
        )

    return CalculatorResult(
        inputs={
            "plans": [
                {"type": p.plan_type, "price": p.price, "distribution": p.distribution}
                for p in plans
            ],
            "monthly_installs": monthly_installs,
            "effective_cr": f"{effective_cr*100:.2f}%",
            "cpi": cpi,
            "apple_fee": f"{apple_fee*100:.0f}%",
        },
        blended_arppu=blended_arppu,
        arpu_net=arpu_net,
        revenue=revenue,
        roas=roas,
        cac=cac,
        breakeven_horizon=breakeven_horizon,
        ltv_to_cac_4yr=ltv_to_cac_4yr,
        grades=grades,
        advice=advice[:3],  # top 3 only
    )


def main():
    parser = argparse.ArgumentParser(
        description="Mobile subscription unit economics calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Annual + monthly plan, 6% CR, $3 CPI, 40k installs
  python3 tools/ltv-calculator.py \\
    --plan annual:89.99:0.25 \\
    --plan quarterly:39.99:0.35 \\
    --plan monthly:19.99:0.35 \\
    --plan lifetime:99:0.05 \\
    --installs 40000 \\
    --cr 0.06 \\
    --cpi 3 \\
    --apple-fee 0.15

  # With trial funnel
  python3 tools/ltv-calculator.py \\
    --plan annual:59.99:0.7 \\
    --plan monthly:9.99:0.3 \\
    --installs 20000 \\
    --trial-start 0.11 \\
    --trial-paid 0.30 \\
    --cpi 2.50

  # JSON input
  cat input.json | python3 tools/ltv-calculator.py --stdin
""",
    )
    parser.add_argument(
        "--plan",
        action="append",
        required=False,
        help="Plan in format 'type:price:distribution', e.g. 'annual:89.99:0.5'",
    )
    parser.add_argument("--installs", type=float, help="Monthly installs")
    parser.add_argument(
        "--cr", type=float, help="CR to purchase (0-1), e.g. 0.06 for 6%%"
    )
    parser.add_argument(
        "--trial-start", type=float, help="Trial start rate (0-1), e.g. 0.112"
    )
    parser.add_argument(
        "--trial-paid", type=float, help="Trial-to-paid rate (0-1), e.g. 0.278"
    )
    parser.add_argument(
        "--cpi", type=float, default=2.50, help="Cost per install (USD), default $2.50"
    )
    parser.add_argument(
        "--apple-fee",
        type=float,
        default=0.15,
        help="Apple fee (0.15 SBP or 0.30), default 0.15",
    )
    parser.add_argument(
        "--stdin", action="store_true", help="Read JSON config from stdin"
    )
    parser.add_argument(
        "--json", action="store_true", help="Output JSON instead of formatted text"
    )

    args = parser.parse_args()

    if args.stdin:
        config = json.load(sys.stdin)
        plans = [
            Plan(p["type"], p["price"], p["distribution"]) for p in config["plans"]
        ]
        result = calculate(
            plans=plans,
            monthly_installs=config["installs"],
            cr_to_purchase=config.get("cr"),
            trial_start_rate=config.get("trial_start"),
            trial_to_paid_rate=config.get("trial_paid"),
            cpi=config.get("cpi", 2.50),
            apple_fee=config.get("apple_fee", 0.15),
        )
    else:
        if not args.plan or not args.installs:
            parser.print_help()
            sys.exit(1)

        plans = []
        for spec in args.plan:
            parts = spec.split(":")
            if len(parts) != 3:
                print(f"Invalid plan spec: {spec}. Format: type:price:distribution")
                sys.exit(1)
            plans.append(Plan(parts[0], float(parts[1]), float(parts[2])))

        result = calculate(
            plans=plans,
            monthly_installs=args.installs,
            cr_to_purchase=args.cr,
            trial_start_rate=args.trial_start,
            trial_to_paid_rate=args.trial_paid,
            cpi=args.cpi,
            apple_fee=args.apple_fee,
        )

    if args.json:
        out = {
            "inputs": result.inputs,
            "blended_arppu": result.blended_arppu,
            "arpu_net": result.arpu_net,
            "revenue": result.revenue,
            "roas": result.roas,
            "cac": result.cac,
            "breakeven_horizon": result.breakeven_horizon,
            "ltv_to_cac_4yr": result.ltv_to_cac_4yr,
            "grades": result.grades,
            "advice": result.advice,
        }
        print(json.dumps(out, indent=2))
    else:
        print(result.summary())


if __name__ == "__main__":
    main()
