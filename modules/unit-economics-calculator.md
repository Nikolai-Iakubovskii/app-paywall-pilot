# Unit Economics Calculator

Conversational LTV / ARPU / ROAS / breakeven calculator. Use this when the user asks "will my app be profitable?", "what's my LTV?", "should I scale?", or shares plans + pricing + funnel data.

Inputs are conversational. Defaults are cited (Adapty 2026 unless noted) so the user can swap in their own numbers when they have them.

For non-numerical decisions, see [decision-trees.md](decision-trees.md). For per-category benchmarks to compare results against, see [category-deep-dives.md](category-deep-dives.md).

---

## Step 1: Collect Inputs

Ask the user, conversationally:

### Subscription plans (one row per plan)
- **Plan type:** weekly / monthly / quarterly / annual / lifetime
- **Price** (USD)
- **Distribution %** — what share of paid subscribers picks this plan (must total 100%)

### Funnel
- **Monthly installs** (current or projected)
- **CR to Purchase** (install → paid %). Default: 6% (median across categories per Adapty 2026)
- **CPI** (cost per install). Default: $2.50 iOS / $1.50 Android (AppsFlyer 2026)

### Trial funnel (if user offers free trials)
- **Trial Start Rate** (install → trial %). Default: 11.2% global / 14.5% NA (Adapty 2026)
- **Trial-to-Paid Rate** (trial → paid %). Default: 27.8% global (Adapty 2026)

When trials are used: `Effective CR = Trial Start Rate × Trial-to-Paid Rate`. This replaces the direct CR input. **Always show the user this breakdown** so they see which part of the funnel to optimize.

### Apple / Play fee
- **Apple fee:** 15% (Small Business Program <$1M revenue) or 30%. Default: 15%
- **Play fee:** 15% (sub year 2+) or 30% (sub year 1, all IAP). Default: 15% if subscriber-mix-heavy

---

## Step 2: Default Retention Multipliers

When the user has no retention data, use these. "Cumulative renewals" means total payment cycles after the first purchase.

Source: Adapty 2026 + RevenueCat 2026 cross-referenced; weekly multiplied higher because weekly cycles are short.

| Plan | 1mo | 3mo | 6mo | 1yr | 2yr | 3yr | 4yr |
|------|-----|-----|-----|-----|-----|-----|-----|
| Weekly | 2.0 | 4.5 | 7.0 | 10.0 | 13.0 | 15.0 | 16.0 |
| Monthly | 0.4 | 0.7 | 1.0 | 1.6 | 2.0 | 2.2 | 2.3 |
| Quarterly | — | 0.15 | 0.2 | 0.35 | 0.4 | 0.45 | 0.42 |
| Annual | — | — | — | 0.1 | 0.13 | 0.15 | 0.16 |

Lifetime: no renewals. LTV = price at all horizons.

**For 7-day horizon:** use cumulative_renewals = 0 (just purchased).

---

## Step 3: Run Calculations

For each horizon T = {7d, 1mo, 3mo, 6mo, 1yr, 2yr, 3yr, 4yr}:

### Per-plan gross LTV
```
LTV_plan(T) = Price × (1 + cumulative_renewals_at_T)
```

### Blended ARPPU (Average Revenue Per Paying User)
```
Blended_ARPPU(T) = Σ [ LTV_plan_i(T) × distribution_i ]
```

### ARPU (net of store fee)
```
ARPU(T) = Blended_ARPPU(T) × (1 − store_fee)
```

### Projected revenue
```
Revenue(T) = Installs × CR_to_purchase × ARPU(T)
```

### Unit economics
```
CAC = CPI / CR_to_purchase
ROAS(T) = (CR_to_purchase × ARPU(T)) / CPI
Breakeven = first T where ROAS ≥ 1.0
LTV:CAC = ARPU(4yr) / CAC
```

### Effective CR (if trial funnel)
```
Effective_CR = Trial_Start_Rate × Trial_to_Paid_Rate
```
Use this in all formulas above. Show the breakdown so the user sees which step is the bottleneck.

---

## Step 4: Present Results

```
| Metric         | 7d   | 1mo  | 3mo  | 6mo  | 1yr  | 2yr  | 3yr  | 4yr  |
|----------------|------|------|------|------|------|------|------|------|
| Blended ARPPU  | $X   | $X   | $X   | $X   | $X   | $X   | $X   | $X   |
| ARPU (net)     | $X   | $X   | $X   | $X   | $X   | $X   | $X   | $X   |
| Revenue        | $X   | $X   | $X   | $X   | $X   | $X   | $X   | $X   |
| ROAS           | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx |
```

Below the table state:
- **CAC:** $X
- **Breakeven:** Tmonth (or "Not reached within 4 years")
- **LTV:CAC ratio (4yr):** X:1

---

## Step 5: Performance Grading

Compare the user's metrics against these thresholds and give a verdict for each.

### Effective CR to Purchase

| CR | Verdict |
|----|---------|
| ≥ 8% | Excellent |
| 5–8% | Good (above average) |
| 3–5% | Average |
| < 3% | Below average — paywall needs work |

### Trial Start Rate (if applicable)

| Rate | Verdict |
|------|---------|
| ≥ 14% | Excellent (NA benchmark) |
| 10–14% | Good |
| 7–10% | Average (global range) |
| < 7% | Below average — paywall not compelling |

### Trial-to-Paid Rate (if applicable)

| Rate | Verdict |
|------|---------|
| ≥ 40% | Excellent |
| 28–40% | Good (above 27.8% global) |
| 15–28% | Average — trial too long or value unclear |
| < 15% | Poor — users not finding value in trial |

### ROAS Breakeven Timeline

| Timeline | Verdict |
|----------|---------|
| < 3 months | Exceptional — scale aggressively |
| 3–6 months | Excellent — healthy economics |
| 6–12 months | Normal — sustainable but watch retention |
| 12–24 months | Warning — long payback, risky for paid UA |
| > 24 months / never | Critical — unit economics broken |

### LTV:CAC Ratio (4-year)

| Ratio | Verdict |
|-------|---------|
| > 5:1 | Strong — likely underinvesting in growth |
| 3:1–5:1 | Healthy — sustainable economics |
| 2:1–3:1 | Marginal — optimize before scaling |
| < 2:1 | Unprofitable — fix pricing / retention / CPI before paid UA |

### ARPU vs Category Benchmarks

Compare 12-month ARPU to [category-deep-dives.md](category-deep-dives.md). State whether above, at, or below category median.

---

## Step 6: Expert Advice Engine

Pick the **2–3 most impactful issues** from the user's results. Don't overwhelm.

### If blended ARPPU below category median
> "Your blended ARPPU of $X is below the [category] median of $Y. High-priced apps earn 3x the LTV of low-priced apps (Adapty 2026). Test a 20–30% price increase on your highest-distribution plan. Adapty A/B data: pricing tests have 45.5% LTV win rate — second-highest test category after localization."

### If CAC exceeds 12-month ARPU (ROAS < 1.0 at 1yr)
> "CAC of $X needs $X net LTV to break even, but 1-year ARPU is $Y. Three levers: (a) reduce CPI (target < $Z), (b) improve effective CR (current X% vs benchmark Y%), (c) raise prices."

### If plan mix suboptimal (annual share <20% and annual LTV ≥2x monthly)
> "Only X% choose annual but it delivers Nx the LTV of monthly. Restructure paywall to default annual + savings callout. Adapty A/B win rate for plan duration: 58.7%."

### If breakeven > 12 months
> "ROAS hits 1.0 only at [T]. Add a weekly plan with free trial to front-load revenue — weekly captures 55.5% of all subscription revenue (Adapty 2026). Weekly+trial 12-mo LTV is $49.27, comparable to annual+trial in many categories."

### If retention below benchmarks (custom data)
> "Your [plan] retention drops to X renewals at 1yr vs benchmark Y. Focus on week 2–4 engagement — faster time-to-value is the #1 retention lever. Trial Timeline visual (Blinkist pattern) increased trial retention by +4% and reduced complaints −55%."

### If LTV:CAC > 5:1
> "LTV:CAC of X:1 is very strong — likely underinvesting in growth. You could increase CPI by up to $X and still maintain healthy 3:1 economics."

### If Trial Start Rate < 10% (with trials)
> "Only X% of installs start a trial vs 11.2% global / 14.5% NA. Paywall not compelling. Test: stronger benefit copy, video backgrounds (8–15% conversion lift per Adapty), or hard paywall to force the decision."

### If Trial-to-Paid Rate < 20% (with trials)
> "X% trial-to-paid is well below 27.8% benchmark. Users start trials but don't convert. Check: trial too long (forget to cancel) → users forget to convert; value not hit in first 2–3 days; pre-expiry notification missing (Blinkist's Day-5 reminder lifted notif opt-in 1,200%)."

### If user has no trials but could benefit
> "You're converting directly without trials. For your category, trials boost LTV up to 64% (US) / 58% (EU) per Adapty. Day-30 retention on weekly: 42% with trial vs 23% without. Test 3-day or 7-day free trial."

### If Apple fee 30% and revenue < $1M
> "You're paying 30% but qualify for Apple's Small Business Program (15% rate) at <$1M annual revenue. Switching = +17.6% net ARPU instantly. Apply at https://developer.apple.com/app-store/small-business-program/"

### If Productivity / Lifestyle category with trial
> "Counter-intuitive: in Productivity ($56.95 direct vs $49.13 trial) and Lifestyle (~21% direct premium), trial users have LOWER LTV than direct buyers (RevenueCat 2026). Test removing trial entirely or moving it to annual-only."

### If single market only
> "You're shipping in [N] markets. Adapty H&F data: 4.4x pricing variance across markets, EU charges 29–39% more than NA. Manual per-territory pricing for top 5 markets typically lifts ARPU 15–25%. See [localization.md](localization.md)."

---

## Step 7: Scenario Modeling

After baseline, proactively offer 2–3 "what-if" scenarios tailored to the user's weakest metric.

### Common scenarios

- "What if you raise [most popular plan] by 30%?"
- "What if CR improves from X% to Y%?" (suggest realistic target based on grading)
- "What if you add a weekly plan at $X/week?"
- "What if you shift plan distribution to 50% annual?"
- "What if you reduce CPI from $X to $Y via better targeting?"
- "What if you qualify for Apple SBP (15% vs 30%)?"
- "What if you add a free trial and hit 11.2% / 27.8% benchmarks?"
- "What if you improve trial-to-paid from X% to Y% with better onboarding?"
- "What if you launch in DE/UK with manual pricing 30% above US?"
- "What if you implement Blinkist Trial Timeline (+23% trial signups)?"

Recalculate the full table for each. Compare side-by-side with baseline.

---

## Worked Example

**User:** "I have an app with annual ($89.99, 25%), quarterly ($39.99, 35%), monthly ($19.99, 35%), lifetime ($99, 5%). My CR is 6%, CPI is $3, 40k installs/month."

### Per-plan LTV at each horizon (gross)

| Plan | Dist | Price | 7d | 1mo | 3mo | 6mo | 1yr | 2yr | 3yr | 4yr |
|------|------|-------|-----|------|------|------|------|------|------|------|
| Annual | 25% | $89.99 | $89.99 | $89.99 | $89.99 | $89.99 | $98.99 | $101.69 | $103.49 | $104.39 |
| Quarterly | 35% | $39.99 | $39.99 | $39.99 | $45.99 | $47.99 | $53.99 | $55.99 | $57.99 | $56.79 |
| Monthly | 35% | $19.99 | $19.99 | $27.99 | $33.98 | $39.98 | $51.97 | $59.97 | $63.97 | $65.97 |
| Lifetime | 5% | $99.00 | $99.00 | $99.00 | $99.00 | $99.00 | $99.00 | $99.00 | $99.00 | $99.00 |

### Blended ARPPU = Σ(LTV × distribution)

- 7d: 22.50 + 14.00 + 7.00 + 4.95 = **$48.44**
- 1mo: 22.50 + 14.00 + 9.80 + 4.95 = **$51.24**
- 1yr: 24.75 + 18.90 + 18.19 + 4.95 = **$66.79**
- 4yr: 26.10 + 19.88 + 23.09 + 4.95 = **$74.01**

### ARPU net (×0.85 for Apple SBP):

| Horizon | ARPU |
|---------|------|
| 7d | $41.18 |
| 1mo | $43.56 |
| 3mo | $47.12 |
| 6mo | $49.50 |
| 1yr | $56.77 |
| 2yr | $60.32 |
| 3yr | $62.49 |
| 4yr | $62.91 |

### Revenue = 40,000 × 0.06 × ARPU

| Horizon | Revenue |
|---------|---------|
| 7d | $98,826 |
| 1yr | $136,248 |
| 4yr | $150,990 |

### ROAS = (0.06 × ARPU) / $3

| Horizon | ROAS |
|---------|------|
| 7d | 0.82 |
| 1mo | 0.87 |
| 6mo | 0.99 |
| 1yr | 1.14 |
| 4yr | 1.26 |

### Summary

- **CAC:** $3 / 0.06 = **$50.00**
- **Breakeven:** ~6 months
- **LTV:CAC (4yr):** $62.91 / $50.00 = **1.26:1**

### Assessment

LTV:CAC of **1.26:1 is below healthy 3:1 threshold**. While ROAS breaks even ~6 months (Normal grade), long-term unit economics are **Marginal**.

### Top-3 actions

1. **Raise prices on quarterly + monthly by 25%.** They're 70% of distribution but anchor too low. Adapty: pricing tests have 45.5% LTV win rate.
2. **Shift plan mix to 40% annual** via paywall default + savings callout. Annual delivers Nx LTV; current 25% share is leaving LTV on the table.
3. **Reduce CPI via channel mix audit.** Target $2 CPI to bring breakeven into 3-month window.

### Scenarios offered

- "What if quarterly+monthly +25%, annual +10%?" → expected LTV:CAC ~1.7:1
- "What if shift to 40% annual via redesign?" → expected LTV:CAC ~1.6:1
- "What if CPI to $2 via better targeting?" → expected LTV:CAC ~1.9:1
- "Combine all three?" → expected LTV:CAC ~3.5:1, breakeven ~3 months

---

## When to Skip the Calculator

- User has <100 paying subs total → numbers are noise. Use [decision-trees.md](decision-trees.md) instead, focus on first principles.
- User is pre-launch → no real CR/retention data. Run with category-median defaults from [category-deep-dives.md](category-deep-dives.md), label as projection.
- User asks a single tactical question ("which plan first?") → use [indie-dev-faq.md](indie-dev-faq.md) instead, faster.

---

## Source Pointers

- Adapty State of In-App Subscriptions 2026: https://adapty.io/state-of-in-app-subscriptions/
- Adapty default retention multipliers: derived from 16K-app dataset
- RevenueCat State 2026 (cross-reference): https://www.revenuecat.com/state-of-subscription-apps/
- Apple Small Business Program: https://developer.apple.com/app-store/small-business-program/
- Adapty growth-expert-skill (LTV calculator inspiration): https://github.com/adaptyteam/growth-expert-skill
- For Python implementation: [tools/ltv-calculator.py](../tools/ltv-calculator.py)
