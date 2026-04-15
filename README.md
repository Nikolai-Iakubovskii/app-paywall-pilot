# App Paywall Pilot — Claude Code Skill

> Your AI copilot for designing, auditing, and implementing App Store-compliant in-app paywalls — with verified 2026 benchmark data.

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill that turns your AI coding assistant into a mobile subscription paywall expert. It guides you through the full paywall lifecycle — from strategy and compliance audit to screen design, A/B testing, and implementation — grounded in real data from Adapty, RevenueCat, Superwall, and Apple guidelines.

## Why this exists

Most paywall advice online is either:
- **Generic web CRO** repackaged for mobile (doesn't account for App Store rules)
- **Hype-driven** ("this one trick 10x'd our revenue!" — from a single app, no methodology)
- **Outdated** (tactics that worked in 2024 now get you rejected by Apple)

This skill fixes that by:
1. **Putting Apple compliance first** — every recommendation is checked against App Store Review Guidelines
2. **Labeling confidence levels** — each recommendation is marked as **Rule** (compliance), **Pattern** (observed across datasets), or **Hypothesis** (test it yourself)
3. **Citing sources with dates** — every benchmark number includes its source and publication date so you know if it's still current
4. **Covering the full system** — not just "make the button bigger" but placement, pricing architecture, trial structure, personalization, analytics, and implementation

## What's inside

### 6-Phase Process
1. **Discovery & Audit** — understand the app, audit existing paywall against rules and patterns
2. **Paywall Strategy** — choose access model, map trigger points, define plan architecture
3. **Screen Design** — design the paywall screen with value block, pricing block, CTA, trust/legal
4. **Testing Plan** — prioritize what to test (structure before polish)
5. **Implementation** — build it using Adapty, RevenueCat, StoreKit 2, or Google Billing
6. **iOS Compliance Checklist** — verify before shipping

### 6 Screen Templates
- Post-Onboarding Hard Paywall
- Feature Gate (Contextual Modal)
- Usage Limit Paywall
- Transaction Abandon Recovery
- Post-Close Welcome Offer
- Win-Back Paywall (Lapsed Subscribers)

### Verified Benchmark Tables (April 2026)
All data from published reports with source and date columns:
- **Conversion rates** — install-to-trial, trial-to-paid, hard paywall vs freemium (Adapty/RevenueCat, Mar 2026)
- **Trial length impact** — short vs long trial conversion rates (RevenueCat, Mar 2026)
- **Revenue per install** — hard paywall vs freemium at Day 14/60 (RevenueCat, Mar 2026)
- **Pricing medians** — weekly/monthly/annual by region (Adapty/RevenueCat, Mar 2026)
- **Plan architecture by category** — which plan type dominates in Gaming, H&F, Productivity, AI (RevenueCat, Mar 2026)
- **A/B test win rates** — localization > trial structure > plan duration > price > copy (Adapty, Mar 2026)
- **Superwall aggregate data** — transaction abandon, product count impact (Superwall, 2024-2026)
- **Regional data** — conversion and RPI by geography (RevenueCat, Mar 2026)

### Design Patterns with Evidence Labels
- Trial Timeline / "Honest Paywall" — **Proven** (Blinkist: +23% conversion, -55% complaints)
- Personalized Headline from Quiz — **Proven** (15%+ lift, Adapty 2026)
- Multi-Page Paywall — **Hypothesis** (conflicting results across apps)
- "Design Your Trial" — **Hypothesis** (Superwall claim, methodology unpublished)
- And more...

### Apple Compliance (Updated for 2026)
- Toggle paywall ban (killed Jan 2026, Guideline 3.1.2)
- Pricing prominence rules
- Trial terms requirements
- Apple Offer Types reference table (Introductory, Promotional, Offer Codes, Win-Back)
- WWDC 2025 StoreKit 2 updates

## Installation

### Option 1: Copy directly
```bash
mkdir -p ~/.claude/skills/paywall-upgrade-cro
curl -o ~/.claude/skills/paywall-upgrade-cro/SKILL.md \
  https://raw.githubusercontent.com/Nikolai-Iakubovskii/app-paywall-pilot/main/SKILL.md
```

### Option 2: Clone and symlink
```bash
git clone https://github.com/Nikolai-Iakubovskii/app-paywall-pilot.git
ln -s "$(pwd)/paywall-upgrade-cro" ~/.claude/skills/paywall-upgrade-cro
```

### Verify
Start Claude Code and run:
```
/paywall-upgrade-cro
```

## Usage

### Full audit
```
/paywall-upgrade-cro
```
Runs the complete 6-phase process starting with Discovery.

### Targeted tasks
```
/paywall-upgrade-cro audit my paywall screenshot
/paywall-upgrade-cro design a trial-focused paywall for a fitness app
/paywall-upgrade-cro check compliance before App Store submission
/paywall-upgrade-cro what should I test next on my paywall?
```

### Auto-trigger
The skill activates automatically when Claude Code detects paywall-related work — files referencing Adapty, RevenueCat, StoreKit, purchase flows, or subscription UI.

## Example output

When you run an audit, the skill produces a structured report:

```
1. Current state — what the app is doing now
2. Main problem or opportunity — plain language
3. Compliance audit — rules checked, flags raised
4. Value communication — copy and messaging quality
5. Strategy observations — plan architecture, triggers
6. Tests to run next — prioritized by impact
7. Immediate actions — what to fix now vs next sprint
```

Each finding is labeled: **Rule** (fix or risk rejection), **Pattern** (likely improvement), or **Hypothesis** (test it).

## Data sources

| Source | Dataset | Date |
|--------|---------|------|
| [Adapty](https://adapty.io/state-of-in-app-subscriptions/) | 16,000+ apps, $3B revenue | Mar 2026 |
| [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps/) | 115,000+ apps, $16B revenue | Mar 2026 |
| [Superwall](https://superwall.com/) | 100M+ monthly paywall views | 2024-2026 |
| [Apphud](https://apphud.com/) | Subscription analytics | 2025-2026 |
| [Apple](https://developer.apple.com/app-store/review/guidelines/) | App Store Review Guidelines | Current |
| [Sensor Tower](https://sensortower.com/) | State of Mobile reports | 2025-2026 |

## What this is NOT

- **Not a landing page optimizer** — this is for in-app subscription flows, not web pricing pages
- **Not a guarantee** — benchmarks are directional, results vary by category and audience
- **Not a dark patterns toolkit** — the skill flags anti-patterns and prioritizes user trust
- **Not affiliated** with Adapty, RevenueCat, Superwall, Apphud, or Apple

## Contributing

PRs welcome. Rules:

1. **Every benchmark must have a source and date.** No unsourced numbers.
2. **Label every recommendation** as Rule, Pattern, or Hypothesis.
3. **Check against App Store guidelines** before adding UI patterns.
4. **Keep SKILL.md lean.** Every line costs tokens in Claude Code's context window.
5. **Open an issue first** for major structural changes.

## Related skills

If you build Claude Code skills for mobile development, these pair well:
- **app-onboarding-questionnaire** — design the onboarding quiz that feeds data into personalized paywalls
- **ab-test-setup** — plan and implement A/B tests for paywall variants
- **ios-monetization-expert** — subscription pricing strategy and LTV optimization
- **analytics-tracking** — set up the funnel events your paywall needs

## License

[MIT](LICENSE)

---

Built by [Nikolai Iakubovskii](https://github.com/Nikolai-Iakubovskii) — indie developer shipping iOS/Android subscription apps with [MistyWay](https://apps.apple.com/app/id6499194956) and [AuroraMe](https://apps.apple.com/app/id6738029498).
