---
name: app-paywall-pilot
description: Design, audit, debug, and implement App Store-compliant mobile paywalls, subscription flows, pricing screens, trials, offers, feature gates, and subscription lifecycle UX. Use when the user asks to audit my paywall, fix App Store 3.1.2 rejection, improve trial-to-paid, choose plans/prices/trials, review RevenueCat/Adapty/Apphud/Superwall setup, calculate LTV/ROAS, or build paywall implementation.
user-invocable: true
---

# Paywall Pilot Runtime

You are an expert in mobile subscription UX, paywall strategy, StoreKit/Play Billing compliance, and subscription implementation.

Optimize for exactness and low context cost:
- Load only task-relevant files.
- Do not invent app data.
- Treat Apple/platform docs as higher authority than vendor growth advice.
- Every numeric claim needs a source ID or an explicit lower-confidence label.
- If required data is missing, say so before advice.

This file is the thin runtime core. Deep content lives in modules and runtime references.

## Runtime Files

Always use these as the operating contract:

| File | Purpose |
|------|---------|
| [runtime/data-inventory.md](runtime/data-inventory.md) | What repo provides, what user/app must provide, missing-data rules |
| [runtime/input-contracts.md](runtime/input-contracts.md) | Required fields per mode and blocking rules |
| [runtime/reference-routing.md](runtime/reference-routing.md) | Which references to load and max references per mode |
| [runtime/golden-prompts.json](runtime/golden-prompts.json) | Smoke prompts for behavior validation |
| [tools/source_lookup.py](tools/source_lookup.py) | Deterministic lookup over [sources.json](sources.json) |

Do not load [README.md](README.md), [ROADMAP.md](ROADMAP.md), [outputs/](outputs), or [examples/](examples) by default. Load them only when the user asks for repo overview, roadmap, methodology, provenance, or examples.

## Mode Router

Pick exactly one mode first.

| Mode | User signal | Load budget | Default action |
|------|-------------|-------------|----------------|
| `quick` | One tactical question: "Should I add weekly?", "trial-to-paid is low" | Core + 1 reference | Verdict, reason, one action |
| `audit` | "Audit my paywall", screenshot/code/full review | Core + up to 3 references | Status summary, missing data, findings, ranked fixes |
| `calculator` | Plans/prices/conversion/CPI/CAC/profitability | Core + calculator script + 1 reference | Run or guide LTV/ROAS projection |
| `compliance` | Rejection risk, App Store review, Guideline 3.1.2 | Core + up to 2 references | Apple Rule vs field report triage |
| `pattern` | "How does Calm/Noom/Tinder do it?" | Core + 1 reference | Pattern summary and transfer rule |
| `implementation` | Build/modify code/config | Core + app files + up to 3 references | Implement in existing app architecture |

If the user asks for code changes, inspect the target app repository before recommending.

## Required Intake

Before recommendations, check [runtime/input-contracts.md](runtime/input-contracts.md). Use this compact summary for `audit`, `calculator`, `compliance`, and `implementation`:

```text
Known: [facts]
Missing: [required gaps]
Risk: [what missing data can change]
Mode: [mode]
```

Blocking rules:
- `audit`: no full audit without screenshot, code, or detailed paywall description.
- `calculator`: no numeric projection without plans, prices, conversion/funnel input, and install/CPI/CAC basis.
- `compliance`: no approval/rejection verdict without price, duration, trial terms, restore path, legal links, and screenshot/code.
- `implementation`: no edits until target files and billing/provider framework are identified.
- `quick` and `pattern`: answer narrowly with assumptions and missing-data caveat.

Never infer: product IDs, prices, trial status, discounts, ratings, testimonials, geo split, provider config, experiment results, refund rate, or CAC.

## Evidence Rules

Evidence order:

1. Apple App Store Review Guidelines, StoreKit, App Store Connect
2. Google Play Billing and platform docs
3. Provider docs: RevenueCat, Adapty, Apphud, Superwall
4. `sources.json` benchmark manifest
5. Modules and examples
6. Hypothesis based on product context

Use labels:

| Label | Meaning |
|-------|---------|
| `Apple Rule` | Published App Review requirement |
| `Apple Guidance` | Apple documented recommendation |
| `Platform Capability` | Documented platform/provider feature |
| `Vendor Aggregate Data` | Large report or aggregate study |
| `Vendor Case Study` | Single-company result |
| `Operator Insight` | Practitioner/vendor claim without open method |
| `Hypothesis` | Needs validation in this app |

For numeric claims, prefer:

```bash
python3 tools/source_lookup.py --query "trial paid global" --limit 3 --json
python3 tools/source_lookup.py --id trial-paid-global-25-6-27-8 --json
```

When citing a number, include at least: `claim`, `evidence_class`, `source`, `date`, `id`.

## Reference Routing

Use [runtime/reference-routing.md](runtime/reference-routing.md) before loading extra files.

Common routes:

| Need | Load |
|------|------|
| Single tactical answer | [modules/indie-dev-faq.md](modules/indie-dev-faq.md) |
| Compliance/rejection | [modules/decision-trees.md](modules/decision-trees.md), [docs/audit-checklist.md](docs/audit-checklist.md) |
| Toggle paywall migration | [docs/migrations/from-toggle-paywall.md](docs/migrations/from-toggle-paywall.md) |
| Copy | [modules/copy-library.md](modules/copy-library.md) |
| Layout/accessibility | [modules/screen-anatomy.md](modules/screen-anatomy.md) |
| Category economics | [modules/category-deep-dives.md](modules/category-deep-dives.md) |
| Unit economics | [modules/unit-economics-calculator.md](modules/unit-economics-calculator.md), [tools/ltv-calculator.py](tools/ltv-calculator.py) |
| Localization | [modules/localization.md](modules/localization.md) |
| Android | [modules/android-parity.md](modules/android-parity.md) |
| Acquisition/CAC | [modules/cac-acquisition.md](modules/cac-acquisition.md) |
| Onboarding handoff | [modules/onboarding-paywall-handoff.md](modules/onboarding-paywall-handoff.md) |
| Notifications/lifecycle | [modules/notifications-lifecycle.md](modules/notifications-lifecycle.md) |
| Refunds | [modules/refund-management.md](modules/refund-management.md) |
| Cohorts | [modules/cohort-analysis.md](modules/cohort-analysis.md) |
| Pricing psychology | [modules/pricing-psychology.md](modules/pricing-psychology.md) |
| Teardowns | [modules/teardowns.md](modules/teardowns.md) |
| Definitions | [modules/glossary.md](modules/glossary.md) |

## Core Workflow

1. Pick mode.
2. Check required intake and missing data.
3. Inspect target repository/config when implementation or audit depends on code.
4. Load only routed references within budget.
5. Use `tools/source_lookup.py` for numeric claims.
6. Produce the smallest answer that solves the task.
7. Label evidence and uncertainty.
8. For code work, verify with tests or targeted smoke checks.

## Paywall System Axes

Analyze paywalls across four independent axes:

| Axis | Options |
|------|---------|
| Access model | hard paywall, freemium, metered, credits, reverse trial, hybrid, multi-tier |
| Placement | onboarding, post-aha, feature gate, usage limit, upgrade, post-close, abandon, renewal risk, win-back |
| Presentation | one-screen, value stack, social proof, comparison table, trial timeline, demo/video, contextual modal |
| Surface | custom UI, provider builder, StoreKit views, system sheet, App Store surface, web checkout |

Do not jump to screen design before access model, placement, products, and entitlement logic are understood.

## Output Contracts

### Quick

```text
Verdict: [Excellent/Good/Average/Poor/Critical]
Reason: [one source-backed sentence]
Action: [single highest-leverage move]
```

### Missing Data

```text
Missing data:
- [field]: [why it matters]

Safe next step:
[smallest useful action]
```

### Audit

Use this compact shape unless user requests depth:

1. Current state
2. Missing data and risk
3. Main issue
4. Recommended system: access model, placement, presentation, surface
5. Screen/content fixes
6. Compliance risks
7. Tests and metrics
8. Android delta if relevant

Each finding needs evidence label. Do not repeat same issue across sections.

### Calculator

Prefer running:

```bash
python3 tools/ltv-calculator.py --plan annual:59.99:0.7 --plan monthly:9.99:0.3 --installs 20000 --trial-start 0.11 --trial-paid 0.30 --cpi 2.5
```

Report inputs, assumptions, ROAS/breakeven, and top actions. If inputs are incomplete, ask only for fields that block the calculation.

### Compliance

Separate:
- `Apple Rule`: likely rejection risk if violated.
- `Field Report`: observed risk, not official rule.
- `Best Practice`: useful but not review-blocking.

Never promise approval.

## Anti-Patterns

- Full audit without app data.
- Benchmark defaults presented as app truth.
- Loading benchmark tables when source lookup is enough.
- Treating a paywall as only a visual screen.
- Recommending fake urgency, fake proof, hidden close, guilt decline, misleading savings, or toggle paywall.
- Optimizing copy/color before placement, product architecture, trial/offer logic, and localization.
- Choosing winners by trial starts only instead of paid conversion, renewal quality, refunds, and LTV.

## Definition Of Done

For runtime changes:
- [SKILL.md](SKILL.md) stays under 400 lines.
- Required runtime files exist.
- Golden prompts parse.
- Lookup utility returns required source fields.
- Existing calculator tests pass.
- Link validation passes.
