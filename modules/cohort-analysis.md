# Cohort Analysis

Cohort analysis is what separates "my app is doing OK" from "my app is on a trajectory to die." This module covers the three cohort types most indie devs misuse, how to read RC / Adapty / Apphud dashboards correctly, and the common cohort mistakes that hide retention problems.

For LTV projection from cohorts, see [unit-economics-calculator.md](unit-economics-calculator.md). For glossary on cohort terms, see [glossary.md](glossary.md).

---

## Why Cohorts Beat Blended Numbers

**Blended retention** says "30% of my users are still paying after 90 days."

**Cohort retention** says "30% of users I acquired in January are still paying at Day 90; 25% of users I acquired in February are still paying at Day 90 — retention is declining."

The blended number hides the trend. By the time blended numbers move, you've shipped 2 quarters of bad cohorts.

**Source:** Apphud's "calendar cohort revenue analysis" pattern. RevenueCat State 2026 reports use cohort throughout.

---

## The Three Cohort Types

### 1. Install Cohort (most common)

Group users by install date. Track retention/payment over time from Day 0 = install.

**When to use:**
- UA channel evaluation (which channel produces best D30/D90/D365 retention)
- Long-term LTV projection
- Default cohort type in most analytics tools

**Setup:**
- X-axis: days since install
- Y-axis: % of cohort still active/paying
- Each line: one install month

### 2. Trial Cohort

Group users by trial start date. Track trial-to-paid conversion + paid retention from trial start.

**When to use:**
- Trial design changes (length, copy, structure)
- Trial-to-paid funnel debugging
- Comparing trial-acquired vs direct-purchase LTV

**Setup:**
- X-axis: days since trial start
- Y-axis: % converted to paid AND % retained as paid
- Each line: trial structure variant

### 3. Calendar Cohort (Apphud signature)

Group users by calendar period (week or month). Track total revenue earned per cohort over time.

**When to use:**
- Revenue-per-cohort attribution
- Detecting if "good months" are actually good or just front-loaded
- Pricing change impact (compare pre/post cohorts)

**Setup:**
- X-axis: months since acquisition
- Y-axis: cumulative revenue per cohort
- Each line: calendar month of acquisition

**Why it matters:** A cohort acquired in November might earn $1.50 per install in month 1, but only $1.20 cumulative by month 12 (refunds + churn). Blended numbers hide this.

---

## Reading RC / Adapty / Apphud Dashboards

### RevenueCat
- **Cohorts** tab → install cohorts by month
- **Charts** tab → blended (use cautiously)
- **Subscription state** dashboard → snapshot of current paying base
- Key column: D30 / D90 / D365 retention curves

### Adapty
- **Cohort Analysis** → install + trial cohorts
- **Funnels** → trial-to-paid by trial structure
- **A/B Tests** → cohort comparison by variant

### Apphud
- **Cohorts** → install + calendar cohort revenue
- "What retention alone never could" — their core pitch is calendar cohort revenue analysis
- Use when you want revenue per cohort, not retention %

---

## Common Cohort Mistakes

### 1. Aggregating across UA channels
Mixing organic + paid cohorts hides paid channel quality. Always cut by channel for unit-economics decisions.

**Fix:** Apply MMP attribution as a cohort dimension (Channel + Install Month).

### 2. Not waiting for cohort maturity
A cohort acquired 2 weeks ago has no D90 data yet. Don't make 90-day decisions on 14-day data.

**Fix:** Only compare cohorts at the same age. "January D90 vs December D90" — not "January D90 vs December D45."

### 3. Mixing trial and direct cohorts
Trial-acquired cohorts have different conversion mechanics than direct-purchase. Mixing them in retention curves muddies signal.

**Fix:** Separate dashboards for trial-cohort vs direct-cohort.

### 4. Ignoring outlier months
A viral month skews the cohort. So does an Apple feature, a TikTok hit, a holiday season.

**Fix:** Annotate dashboards with major events. Compare "normal" months to "normal" months.

### 5. Using D30 as proxy for LTV
Some plans (annual) don't show meaningful retention by D30 because they haven't had a renewal opportunity yet. D30 retention says nothing about whether annual subscribers will renew at Day 365.

**Fix:** Match cohort age to plan duration. Weekly: D30+ meaningful. Monthly: D60+. Annual: D365+.

### 6. Using blended D30 retention as a North Star
You'll optimize for short-term metric and miss long-term LTV.

**Fix:** Track at minimum D30, D90, D180, D365. Make D365 the North Star for annual-heavy apps; D90 for monthly-heavy.

### 7. Not refreshing benchmarks
Adapty/RC publish 2026 cohort benchmarks. Comparing your 2026 data to 2024 benchmarks is wrong (industry rates have shifted).

**Fix:** Re-pull benchmarks at least quarterly.

---

## What Healthy Cohort Curves Look Like

### Subscription D30/D90/D365 retention (annual plan)

```
100% ┤●
     │ ●
 80% ┤  ●●●●●●● ← steady at ~90% until renewal
     │         ●
 60% ┤          ●●● ← annual renewal cliff
     │             ●●●●●●●●● ← steady at ~45% (Adapty H&F 2nd renewal benchmark)
 40% ┤
     │
 20% ┤
     │
  0% ┴────────────────────────────────────
     0    30    90    180   365   730  days
```

A healthy annual cohort drops at the renewal point and stabilizes around 40-50%. If your renewal cliff drops below 30%, you have a renewal-risk problem.

### Monthly cohort

```
100% ┤●
     │ ●●●●●  ← month-1 churn (~30-40% normal)
 60% ┤      ●●●●●  ← gradual decline
     │            ●●●●● ← stabilizes at ~17% Y1 (RC 2026)
 30% ┤
     │
  0% ┴────────────────────────────────────
     0    30    90    180   365  days
```

### Weekly cohort

```
100% ┤●
     │ ●●  ← brutal week-1 churn (~65% normal per Adapty)
 30% ┤   ●●●  ← stabilizes ~30% at Day 30 with trial (Adapty)
     │      ●● ← steady ~10% at 1yr
 10% ┤
  0% ┴────────────────────────────────────
     0    7    30    90    180   365  days
```

If your weekly cohort doesn't stabilize at ~30% D30 (with trial) or ~23% D30 (without), engagement is the problem.

---

## Cohort Comparison: Pre vs Post Change

When you ship a meaningful change (price increase, paywall redesign, new onboarding), cohort comparison is the only honest measurement.

### Setup

| Cohort | Acquired | Compare at age |
|--------|----------|---------------|
| Pre-change baseline | 60 days before launch | Day N |
| Post-change variant | 60 days after launch | Day N |

Wait at least N days post-change before drawing conclusions. For trial impact: N >= trial length + 30 days.

### Common comparison errors

- Comparing pre-change Day 90 to post-change Day 30 (apples vs oranges)
- Including the launch month itself (mixing pre + post)
- Single-month comparison (one month of noise can look like signal)

---

## Cohort Tooling

| Tool | Best for cohorts | Pricing |
|------|------------------|---------|
| RevenueCat | Subscription cohorts, D30/D90/D365 | Free tier generous |
| Adapty | A/B + cohort cuts | Free <$5K MRR |
| Apphud | Calendar cohort revenue (signature feature) | Free tier |
| Amplitude | Behavioral + cohort cross-cuts | Free <10M events |
| Mixpanel | Behavioral cohorts | Free <100K MTUs |
| Custom (BigQuery + Looker) | Full control | $$$ infra cost |

For most indie devs: RC or Adapty as primary, Amplitude/Mixpanel for behavioral cuts.

---

## When Cohorts Don't Help

- **Pre-PMF / very early** — cohorts are too small to be meaningful (<100 users)
- **Single-day conversion product** — gaming with one-time IAP, lifetime-only products
- **Very long sales cycles** — B2B with 6-month sales cycles need different framing

---

## Source Pointers

- RevenueCat cohort docs: https://www.revenuecat.com/docs/dashboard-and-metrics/cohorts
- Adapty cohort analysis: https://adapty.io/blog/customer-cohort-analysis/
- Apphud calendar cohort revenue: https://apphud.com/blog (search "Calendar Cohort Revenue Analysis")
- AppsFlyer cohort guide: https://www.appsflyer.com/glossary/cohort-analysis/
- See also [glossary.md](glossary.md) for cohort term definitions
