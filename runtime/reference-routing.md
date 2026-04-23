# Runtime Reference Routing

Load the smallest set of references that answers the task. Do not load README or research briefs by default.

## Context Budgets

| Mode | Max references | Default files |
|------|----------------|---------------|
| `quick` | 1 | [modules/indie-dev-faq.md](../modules/indie-dev-faq.md) or one task-specific module |
| `audit` | 3 | [runtime/input-contracts.md](input-contracts.md), plus up to two modules selected by issue |
| `calculator` | 1 + script | [modules/unit-economics-calculator.md](../modules/unit-economics-calculator.md), [tools/ltv-calculator.py](../tools/ltv-calculator.py) |
| `compliance` | 2 | [modules/decision-trees.md](../modules/decision-trees.md), [docs/audit-checklist.md](../docs/audit-checklist.md) |
| `pattern` | 1 | [modules/teardowns.md](../modules/teardowns.md) or one pattern module |
| `implementation` | 3 | [runtime/input-contracts.md](input-contracts.md), billing/provider docs from target app, one domain module |

## Routing Map

| Need | Load |
|------|------|
| One tactical benchmark answer | [modules/indie-dev-faq.md](../modules/indie-dev-faq.md) |
| Source-backed numeric claim | Run [tools/source_lookup.py](../tools/source_lookup.py) |
| Plan/pricing/category economics | [modules/category-deep-dives.md](../modules/category-deep-dives.md) |
| LTV/ROAS/breakeven | [modules/unit-economics-calculator.md](../modules/unit-economics-calculator.md) and script |
| App Store risk | [modules/decision-trees.md](../modules/decision-trees.md), [docs/audit-checklist.md](../docs/audit-checklist.md) |
| Toggle-paywall migration | [docs/migrations/from-toggle-paywall.md](../docs/migrations/from-toggle-paywall.md) |
| Copy variants | [modules/copy-library.md](../modules/copy-library.md) |
| Layout/accessibility | [modules/screen-anatomy.md](../modules/screen-anatomy.md) |
| Localization/geo-pricing | [modules/localization.md](../modules/localization.md) |
| Android parity | [modules/android-parity.md](../modules/android-parity.md) |
| Acquisition/CAC | [modules/cac-acquisition.md](../modules/cac-acquisition.md) |
| Onboarding handoff | [modules/onboarding-paywall-handoff.md](../modules/onboarding-paywall-handoff.md) |
| Notifications/lifecycle | [modules/notifications-lifecycle.md](../modules/notifications-lifecycle.md) |
| Refunds | [modules/refund-management.md](../modules/refund-management.md) |
| Cohorts | [modules/cohort-analysis.md](../modules/cohort-analysis.md) |
| Academic mechanism | [modules/pricing-psychology.md](../modules/pricing-psychology.md) |
| Acronyms/definitions | [modules/glossary.md](../modules/glossary.md) |

## Source Lookup

Use lookup for numeric claims instead of loading benchmark tables.

```bash
python3 tools/source_lookup.py --query "trial paid global" --limit 3 --json
python3 tools/source_lookup.py --id trial-paid-global-25-6-27-8 --json
```

Required output fields for cited numeric claims:

```text
claim, evidence_class, source, date, url, scope, id
```

## Research Briefs

Load [outputs/2026-paywall-research-v2.md](../outputs/2026-paywall-research-v2.md) only when the user asks for methodology, provenance, or deep research. Prefer [sources.json](../sources.json) plus lookup for normal answers.
