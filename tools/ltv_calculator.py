#!/usr/bin/env python3
"""
LTV / ARPU / ROAS / breakeven calculator for mobile subscription apps.

CLI:
    python3 tools/ltv-calculator.py

Import:
    from tools.ltv_calculator import Plan, calculate
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from typing import Literal

PlanType = Literal["weekly", "monthly", "quarterly", "annual", "lifetime"]
ALLOWED_PLAN_TYPES: tuple[PlanType, ...] = (
    "weekly",
    "monthly",
    "quarterly",
    "annual",
    "lifetime",
)
TIME_HORIZONS = ["7d", "1mo", "3mo", "6mo", "1yr", "2yr", "3yr", "4yr"]

# Default cumulative renewal multipliers per plan type per time horizon.
# "Cumulative renewals" = total payment cycles AFTER the first purchase.
# So total payments = 1 (initial) + cumulative_renewals.
# Source: Adapty 2026 + RevenueCat 2026 cross-referenced.
DEFAULT_RETENTION: dict[PlanType, dict[str, float]] = {
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
        "4yr": 0.45,
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
    "lifetime": {h: 0.0 for h in TIME_HORIZONS},
}


@dataclass(frozen=True)
class Plan:
    plan_type: PlanType
    price: float
    distribution: float


@dataclass
class CalculatorResult:
    inputs: dict
    blended_arppu: dict[str, float]
    arpu_net: dict[str, float]
    revenue: dict[str, float]
    roas: dict[str, float]
    cac: float
    breakeven_horizon: str | None
    ltv_to_cac_4yr: float
    grades: dict[str, str]
    advice: list[str]

    def to_json_dict(self) -> dict:
        return _json_safe(asdict(self))

    def summary(self) -> str:
        lines = []
        lines.append("=" * 72)
        lines.append("UNIT ECONOMICS CALCULATOR — RESULTS")
        lines.append("=" * 72)
        lines.append("")

        lines.append("Inputs:")
        for key, value in self.inputs.items():
            lines.append(f"  {key}: {value}")
        lines.append("")

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

        roas_cells = []
        for horizon in TIME_HORIZONS:
            roas = self.roas[horizon]
            if math.isinf(roas):
                roas_cells.append(f"{'inf':>8}x")
            else:
                roas_cells.append(f"{roas:>8.2f}x")
        lines.append(f"{'ROAS':<16} " + " ".join(roas_cells))
        lines.append("")

        if math.isinf(self.cac):
            lines.append("CAC: inf")
        else:
            lines.append(f"CAC: ${self.cac:.2f}")

        if self.breakeven_horizon:
            lines.append(
                f"Breakeven: {self.breakeven_horizon} (first horizon where ROAS >= 1.0)"
            )
        else:
            lines.append("Breakeven: Not reached within 4 years")

        if math.isinf(self.ltv_to_cac_4yr):
            lines.append("LTV:CAC (4yr): inf:1")
        else:
            lines.append(f"LTV:CAC (4yr): {self.ltv_to_cac_4yr:.2f}:1")
        lines.append("")

        lines.append("Performance grades:")
        for key, value in self.grades.items():
            lines.append(f"  {key}: {value}")
        lines.append("")

        if self.advice:
            lines.append("Top recommendations:")
            for index, item in enumerate(self.advice, 1):
                lines.append(f"  {index}. {item}")

        lines.append("=" * 72)
        return "\n".join(lines)


def grade_cr(rate: float) -> str:
    if rate >= 0.08:
        return "Excellent"
    if rate >= 0.05:
        return "Good"
    if rate >= 0.03:
        return "Average"
    return "Below average"


def grade_trial_start(rate: float) -> str:
    if rate >= 0.14:
        return "Excellent (NA benchmark)"
    if rate >= 0.10:
        return "Good"
    if rate >= 0.07:
        return "Average"
    return "Below average"


def grade_trial_to_paid(rate: float) -> str:
    if rate >= 0.40:
        return "Excellent"
    if rate >= 0.28:
        return "Good"
    if rate >= 0.15:
        return "Average"
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
    step = order[horizon]
    if step <= 2:
        return "Exceptional — scale aggressively"
    if step <= 3:
        return "Excellent — healthy economics"
    if step <= 4:
        return "Normal — sustainable"
    if step <= 5:
        return "Warning — long payback"
    return "Critical — fix before paid UA"


def grade_ltv_cac(ratio: float) -> str:
    if math.isinf(ratio):
        return "Strong — organic or near-zero CAC"
    if ratio > 5:
        return "Strong — likely underinvesting in growth"
    if ratio >= 3:
        return "Healthy — sustainable economics"
    if ratio >= 2:
        return "Marginal — optimize before scaling"
    return "Unprofitable — fix LTV side first"


def _json_safe(value):
    if isinstance(value, float) and math.isinf(value):
        return "inf"
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    return value


def _validate_rate(name: str, value: float) -> None:
    if not 0 <= value <= 1:
        raise ValueError(f"{name} must be between 0 and 1, got {value}")


def _validate_plan(plan: Plan) -> None:
    if plan.plan_type not in ALLOWED_PLAN_TYPES:
        allowed = ", ".join(ALLOWED_PLAN_TYPES)
        raise ValueError(f"Unknown plan_type '{plan.plan_type}'. Expected one of: {allowed}")
    if plan.price <= 0:
        raise ValueError(f"Plan price must be > 0, got {plan.price}")
    if not 0 < plan.distribution <= 1:
        raise ValueError(
            f"Plan distribution must be > 0 and <= 1, got {plan.distribution}"
        )


def _validate_retention(retention: dict[PlanType, dict[str, float]]) -> None:
    for plan_type in ALLOWED_PLAN_TYPES:
        plan_curve = retention.get(plan_type)
        if plan_curve is None:
            raise ValueError(f"Missing retention curve for plan_type '{plan_type}'")

        previous = -1.0
        for horizon in TIME_HORIZONS:
            if horizon not in plan_curve:
                raise ValueError(
                    f"Missing retention value for plan_type '{plan_type}' at horizon '{horizon}'"
                )
            value = plan_curve[horizon]
            if value < 0:
                raise ValueError(
                    f"Retention value must be >= 0 for '{plan_type}' at '{horizon}', got {value}"
                )
            if value < previous:
                raise ValueError(
                    f"Retention curve for '{plan_type}' must be non-decreasing; "
                    f"'{horizon}' = {value} after {previous}"
                )
            previous = value


def _effective_cr(
    cr_to_purchase: float | None,
    trial_start_rate: float | None,
    trial_to_paid_rate: float | None,
) -> float:
    if trial_start_rate is None and trial_to_paid_rate is None:
        if cr_to_purchase is None:
            raise ValueError(
                "Provide either cr_to_purchase or (trial_start_rate AND trial_to_paid_rate)"
            )
        return cr_to_purchase

    if trial_start_rate is None or trial_to_paid_rate is None:
        raise ValueError(
            "Provide both trial_start_rate and trial_to_paid_rate when using trial funnel inputs"
        )

    return trial_start_rate * trial_to_paid_rate


def _plan_ltv(plan: Plan, retention: dict[PlanType, dict[str, float]], horizon: str) -> float:
    return plan.price * (1 + retention[plan.plan_type][horizon])


def _average_plan_ltv(
    plans: list[Plan], plan_type: PlanType, retention: dict[PlanType, dict[str, float]], horizon: str
) -> float | None:
    selected = [plan for plan in plans if plan.plan_type == plan_type]
    if not selected:
        return None
    return sum(_plan_ltv(plan, retention, horizon) for plan in selected) / len(selected)


def calculate(
    plans: list[Plan],
    monthly_installs: float,
    cr_to_purchase: float | None = None,
    trial_start_rate: float | None = None,
    trial_to_paid_rate: float | None = None,
    cpi: float = 2.50,
    apple_fee: float = 0.15,
    custom_retention: dict[PlanType, dict[str, float]] | None = None,
) -> CalculatorResult:
    """Run full unit-economics calculation."""
    if not plans:
        raise ValueError("Provide at least one plan")

    for plan in plans:
        _validate_plan(plan)

    if monthly_installs < 0:
        raise ValueError(f"monthly_installs must be >= 0, got {monthly_installs}")
    if cpi < 0:
        raise ValueError(f"cpi must be >= 0, got {cpi}")
    if not 0 <= apple_fee < 1:
        raise ValueError(f"apple_fee must be between 0 and 1, got {apple_fee}")

    if cr_to_purchase is not None:
        _validate_rate("cr_to_purchase", cr_to_purchase)
    if trial_start_rate is not None:
        _validate_rate("trial_start_rate", trial_start_rate)
    if trial_to_paid_rate is not None:
        _validate_rate("trial_to_paid_rate", trial_to_paid_rate)

    total_dist = sum(plan.distribution for plan in plans)
    if abs(total_dist - 1.0) > 0.01:
        raise ValueError(f"Plan distributions must sum to 1.0, got {total_dist:.3f}")

    retention = custom_retention or DEFAULT_RETENTION
    _validate_retention(retention)

    effective_cr = _effective_cr(cr_to_purchase, trial_start_rate, trial_to_paid_rate)

    blended_arppu: dict[str, float] = {}
    for horizon in TIME_HORIZONS:
        blended_arppu[horizon] = sum(
            _plan_ltv(plan, retention, horizon) * plan.distribution for plan in plans
        )

    arpu_net = {
        horizon: blended_arppu[horizon] * (1 - apple_fee) for horizon in TIME_HORIZONS
    }
    revenue = {
        horizon: monthly_installs * effective_cr * arpu_net[horizon]
        for horizon in TIME_HORIZONS
    }

    if cpi == 0:
        roas = {
            horizon: math.inf if effective_cr * arpu_net[horizon] > 0 else 0.0
            for horizon in TIME_HORIZONS
        }
        cac = 0.0
        ltv_to_cac_4yr = math.inf if arpu_net["4yr"] > 0 else 0.0
    else:
        roas = {
            horizon: (effective_cr * arpu_net[horizon]) / cpi for horizon in TIME_HORIZONS
        }
        cac = cpi / effective_cr if effective_cr > 0 else math.inf
        ltv_to_cac_4yr = arpu_net["4yr"] / cac if cac > 0 else 0.0

    breakeven_horizon = next(
        (horizon for horizon in TIME_HORIZONS if roas[horizon] >= 1.0),
        None,
    )

    grades = {
        "Effective CR": f"{effective_cr*100:.2f}% — {grade_cr(effective_cr)}",
        "Breakeven": grade_breakeven(breakeven_horizon),
        "LTV:CAC (4yr)": f"{ltv_to_cac_4yr:.2f}:1 — {grade_ltv_cac(ltv_to_cac_4yr)}"
        if not math.isinf(ltv_to_cac_4yr)
        else f"inf:1 — {grade_ltv_cac(ltv_to_cac_4yr)}",
    }
    if trial_start_rate is not None:
        grades["Trial Start Rate"] = (
            f"{trial_start_rate*100:.2f}% — {grade_trial_start(trial_start_rate)}"
        )
    if trial_to_paid_rate is not None:
        grades["Trial-to-Paid"] = (
            f"{trial_to_paid_rate*100:.2f}% — {grade_trial_to_paid(trial_to_paid_rate)}"
        )

    advice: list[str] = []
    if ltv_to_cac_4yr < 2:
        advice.append(
            f"LTV:CAC of {ltv_to_cac_4yr:.2f}:1 is unprofitable. "
            "Don't increase UA spend. Fix pricing, plan mix, or retention first."
        )
    elif ltv_to_cac_4yr < 3:
        advice.append(
            f"LTV:CAC of {ltv_to_cac_4yr:.2f}:1 is marginal. "
            "Test +20-30% on highest-distribution plan. Pricing has 45.5% A/B win rate (Adapty)."
        )
    elif math.isinf(ltv_to_cac_4yr):
        advice.append(
            "CPI is $0, so paid-UA ROAS is not the limiting factor. "
            "Focus on activation, retention, and absolute revenue per install."
        )
    elif ltv_to_cac_4yr > 5:
        advice.append(
            f"LTV:CAC of {ltv_to_cac_4yr:.2f}:1 is strong — likely underinvesting in growth. "
            f"You could increase CPI to ${arpu_net['4yr']/3:.2f} and still maintain healthy 3:1."
        )

    annual_share = sum(plan.distribution for plan in plans if plan.plan_type == "annual")
    monthly_share = sum(plan.distribution for plan in plans if plan.plan_type == "monthly")
    annual_4yr = _average_plan_ltv(plans, "annual", retention, "4yr")
    monthly_4yr = _average_plan_ltv(plans, "monthly", retention, "4yr")
    if (
        annual_share < 0.20
        and monthly_share > 0.30
        and annual_4yr is not None
        and monthly_4yr is not None
        and monthly_4yr > 0
    ):
        annual_ratio = annual_4yr / monthly_4yr
        advice.append(
            f"Only {annual_share*100:.0f}% choose annual; annual plans deliver ~{annual_ratio:.1f}x "
            "4-year gross ARPPU vs monthly. Default annual + savings callout. "
            "Plan duration A/B win rate: 58.7% (Adapty)."
        )

    has_weekly = any(plan.plan_type == "weekly" for plan in plans)
    if (breakeven_horizon is None or breakeven_horizon in ("3yr", "4yr")) and not has_weekly:
        advice.append(
            f"Breakeven slow ({breakeven_horizon or 'never'}). "
            "Test a weekly plan with free trial — weekly captures 55.5% of all subscription revenue. "
            "Weekly+trial 12-mo LTV $49.27."
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
            "Paywall not compelling. Test stronger benefit copy, video background, or harder gate timing."
        )

    if trial_to_paid_rate is not None and trial_to_paid_rate < 0.20:
        advice.append(
            f"Trial-to-Paid {trial_to_paid_rate*100:.1f}% well below 27.8% benchmark. "
            "Check trial length, first-session value delivery, and pre-expiry reminder coverage."
        )

    return CalculatorResult(
        inputs={
            "plans": [asdict(plan) for plan in plans],
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
        advice=advice[:3],
    )


def _parse_plans(plan_specs: list[str]) -> list[Plan]:
    plans: list[Plan] = []
    for spec in plan_specs:
        parts = spec.split(":")
        if len(parts) != 3:
            raise ValueError(f"Invalid plan spec: {spec}. Format: type:price:distribution")
        plans.append(Plan(parts[0], float(parts[1]), float(parts[2])))
    return plans


def _build_parser() -> argparse.ArgumentParser:
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
    parser.add_argument("--cr", type=float, help="CR to purchase (0-1), e.g. 0.06")
    parser.add_argument("--trial-start", type=float, help="Trial start rate (0-1)")
    parser.add_argument("--trial-paid", type=float, help="Trial-to-paid rate (0-1)")
    parser.add_argument(
        "--cpi", type=float, default=2.50, help="Cost per install (USD), default $2.50"
    )
    parser.add_argument(
        "--apple-fee",
        type=float,
        default=0.15,
        help="Apple fee (0.15 SBP or 0.30), default 0.15",
    )
    parser.add_argument("--stdin", action="store_true", help="Read JSON config from stdin")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of text")
    return parser


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    return _build_parser().parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    try:
        if args.stdin:
            config = json.load(sys.stdin)
            plans = [
                Plan(plan["type"], plan["price"], plan["distribution"])
                for plan in config["plans"]
            ]
            result = calculate(
                plans=plans,
                monthly_installs=config["installs"],
                cr_to_purchase=config.get("cr"),
                trial_start_rate=config.get("trial_start"),
                trial_to_paid_rate=config.get("trial_paid"),
                cpi=config.get("cpi", 2.50),
                apple_fee=config.get("apple_fee", 0.15),
                custom_retention=config.get("custom_retention"),
            )
        else:
            if not args.plan or args.installs is None:
                _build_parser().print_help()
                return 1

            plans = _parse_plans(args.plan)
            result = calculate(
                plans=plans,
                monthly_installs=args.installs,
                cr_to_purchase=args.cr,
                trial_start_rate=args.trial_start,
                trial_to_paid_rate=args.trial_paid,
                cpi=args.cpi,
                apple_fee=args.apple_fee,
            )
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result.to_json_dict(), indent=2))
    else:
        print(result.summary())
    return 0


if __name__ == "__main__":
    sys.exit(main())
