# Runtime Input Contracts

Every mode has a minimum data contract. If required data is missing, say what is missing and keep the answer narrow.

## Mode Selection

| Mode | User signal | Primary output |
|------|-------------|----------------|
| `quick` | One tactical question | Verdict, reason, one action |
| `audit` | "Audit my paywall", screenshot, code, full review | Status summary, findings, ranked fixes |
| `calculator` | Pricing, conversion, CPI/CAC, profitability | LTV/ARPU/ROAS/breakeven projection |
| `compliance` | Rejection risk, App Store review, Guideline 3.1.2 | Apple Rule vs field report triage |
| `pattern` | "How does X structure paywall?", examples, teardowns | Pattern summary and transfer rule |
| `implementation` | Build or modify paywall code | Code/config changes plus verification |

## Required Fields

| Field | Quick | Audit | Calculator | Compliance | Pattern | Implementation |
|-------|-------|-------|------------|------------|---------|----------------|
| App purpose/category | optional | required | recommended | recommended | recommended | required |
| Platform | optional | required | recommended | required | optional | required |
| Screenshot/video/code/paywall description | optional | required | optional | required if visual risk | optional | required |
| Subscription provider | optional | required | recommended | recommended | optional | required |
| Product IDs and durations | optional | required | required | required | optional | required |
| Prices and currencies | optional | required | required | required if savings/trial terms | optional | required |
| Trial/offer setup | optional | required | required if trial funnel | required | optional | required |
| Placement and trigger | optional | required | recommended | recommended | optional | required |
| Segment and geo/locale | optional | required | recommended | recommended | optional | recommended |
| Funnel metrics and date window | optional | recommended | required | optional | optional | optional |
| Refund/renewal/churn data | optional | recommended | recommended | optional | optional | optional |
| Current experiments/sample size | optional | recommended | optional | optional | optional | optional |
| Legal links/restore path | optional | required | optional | required | optional | required |

## Blocking Rules

- `audit`: Block full audit when no screenshot, code, or detailed paywall description is provided.
- `calculator`: Block numeric projection when plans, prices, conversion rate or trial funnel, and install/CAC inputs are missing.
- `compliance`: Block approval/rejection verdict when price, duration, trial terms, restore path, terms link, privacy link, and screenshot/code are missing. Give checklist instead.
- `implementation`: Block code edits when target app files or provider/framework cannot be found.
- `quick` and `pattern`: Do not block. Answer with assumptions and missing-data caveat.

## Status Summary Format

For `audit`, `calculator`, `compliance`, and `implementation`, start with this compact status summary:

```text
Known: [comma-separated facts]
Missing: [comma-separated required gaps]
Risk: [what the missing data can change]
Mode: [quick/audit/calculator/compliance/pattern/implementation]
```

## Missing Data Response

If required data is missing:

```text
Missing data:
- [field]: [why it matters]

Safe next step:
[smallest useful action without inventing data]
```

Do not fill gaps with generic benchmark defaults unless the user explicitly asks for a scenario estimate.
