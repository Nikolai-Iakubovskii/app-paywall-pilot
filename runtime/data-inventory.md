# Runtime Data Inventory

Use this file to decide what the agent can know from the repo, what it must ask the user for, and what should be treated as unavailable.

## Repo-Provided Data

These inputs can be read from this repository.

| Data | Location | Use |
|------|----------|-----|
| Runtime behavior | [SKILL.md](../SKILL.md), [input-contracts.md](input-contracts.md), [reference-routing.md](reference-routing.md) | Mode choice, required inputs, context budget |
| Benchmarks and source IDs | [sources.json](../sources.json), [tools/source_lookup.py](../tools/source_lookup.py) | Numeric claims with evidence class, date, URL, scope |
| Category guidance | [modules/category-deep-dives.md](../modules/category-deep-dives.md) | Category-specific plan, trial, pricing, geography guidance |
| Compliance guidance | [modules/decision-trees.md](../modules/decision-trees.md), [docs/audit-checklist.md](../docs/audit-checklist.md), [docs/migrations/from-toggle-paywall.md](../docs/migrations/from-toggle-paywall.md) | App Store review risk, migration from risky patterns |
| Copy and layout guidance | [modules/copy-library.md](../modules/copy-library.md), [modules/screen-anatomy.md](../modules/screen-anatomy.md) | Paywall copy, CTA, layout, accessibility |
| Economics tool | [tools/ltv-calculator.py](../tools/ltv-calculator.py), [modules/unit-economics-calculator.md](../modules/unit-economics-calculator.md) | LTV, ARPU, ROAS, breakeven |
| Worked examples | [examples/](../examples) | Output shape reference only; do not load by default |
| Research briefs | [outputs/](../outputs) | Methodology and provenance; load only when user asks for research depth |

## User/App-Provided Data

These inputs usually do not exist in this repo. Ask for them or mark them missing.

| Data | Needed for |
|------|------------|
| Paywall screenshot, video, or code | Any full audit or visual/layout recommendation |
| App category, purpose, audience, and core value moment | Access model, placement, copy, category benchmark selection |
| Platform and app framework | Implementation guidance, iOS/Android delta, StoreKit/Play Billing advice |
| Subscription provider and config | RevenueCat/Adapty/Apphud/Superwall implementation and remote config checks |
| Product IDs, subscription group, durations, prices, trial/offer setup | Compliance, savings math, plan architecture, entitlement checks |
| Placement IDs, variant IDs, trigger rules, and segments | Audit accuracy, experiment design, lifecycle mapping |
| Funnel metrics and date window | Conversion diagnosis and performance grading |
| Retention, renewal, refund, billing issue, and churn data | LTV, refund diagnosis, lifecycle recommendations |
| Geo, locale, currency, and pricing territory data | Localization and geo-pricing guidance |
| Acquisition mix, CPI/CAC, and campaign source | Unit economics and channel-level recommendations |
| Current experiments, sample sizes, and primary metrics | Test plan and winner/loser interpretation |
| Legal links and App Store Connect state | Compliance triage |

## Missing Data Rules

- If a required field is missing, list it in `Missing data` before recommendations.
- If the missing field changes the answer materially, do not produce a full recommendation. Give the smallest safe next step.
- Never infer product IDs, prices, trial status, discounts, ratings, testimonials, geo split, provider config, or experiment results.
- Benchmarks are fallback context. User/app data wins when it is real and current.
