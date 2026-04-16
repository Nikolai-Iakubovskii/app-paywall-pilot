# Example Audit: Productivity App

Worked example for a Productivity category app. Productivity has the **counter-intuitive trial economics**: direct buyers worth more than trial buyers ($56.95 vs $49.13 RC 2026).

For comparison: [audit-h-and-f-app.md](audit-h-and-f-app.md), [audit-ai-app.md](audit-ai-app.md).

---

## Input

**Hypothetical app:** "TaskMaster" — task management with smart prioritization. iOS only, US + EU.

**Current state:**
- Onboarding: 4 screens (welcome, primary use case, theme, name)
- Paywall: post-onboarding, 3 plans (monthly $4.99, annual $39.99, family $79.99) all with 14-day trial
- Free tier: limited to 10 active tasks
- Markets: US 70%, EU 30%
- Metrics: install→trial 11%, trial→paid 19%, monthly churn 9%, refund rate 4.8%

---

## Audit Output

### 1. Current state

Productivity category, freemium-with-meter, 3-plan paywall, 14-day trial on all plans. Pricing **below category benchmark** (Productivity median monthly $10, annual $44.99 per Adapty 2026). Trial→paid 19% is **below benchmark** (27.8% global) — common in Productivity where trial users are lower-intent than direct buyers.

### 2. Main problem or opportunity

**Two issues compounding:**

1. **Trial subsidizes lower-LTV users.** RC 2026: Productivity direct buyers $56.95 vs trial $49.13 12-mo LTV. Your trial-on-all-plans is collecting the wrong cohort.

2. **Pricing too low for category.** Adapty 2026: Productivity median monthly $10, annual $44.99. Your $4.99/$39.99 leaves 15-30% revenue on table. Productivity audience is sophisticated and price-tolerant.

### 3. Recommended access model

Counter-intuitive for category: **soft paywall (freemium) without trial as default**, OR **hard paywall direct-to-paid for high-intent**. Test both.

- Freemium without trial: lets users prove value to themselves; converters are higher-LTV
- Hard paywall direct: filters for committed users immediately

Reverse trial as alternative for low-intent users (RC Operator Insight for Productivity).

### 4. Recommended placements

- **Post-aha paywall (primary):** after user creates 5 tasks AND completes 3. The aha moment in task apps is when you actually complete things, not just create them.
- **Feature gate (secondary):** locked features (smart prioritization, integrations, calendar sync) trigger contextual paywall.
- **Usage limit (tertiary):** at 10 active tasks limit.
- **Plan upgrade:** monthly subscribers offered annual at end of month 2.

### 5. Recommended presentation

**Comparison table** (Free vs Pro vs Family) — Productivity audience reads tables.

```
┌──────────────────────────────────────────┐
│ [X close]                                │
│                                          │
│ Get more done with Pro.                  │
│ Built for serious task management.       │
│                                          │
│ ★★★★★ 4.8 — Used by 25K+ teams         │
│                                          │
│ ┌───────────┬──────────┬──────────┐      │
│ │           │  Free    │  Pro     │      │
│ ├───────────┼──────────┼──────────┤      │
│ │ Tasks     │  10      │  ∞       │      │
│ │ Projects  │  3       │  ∞       │      │
│ │ Smart Pri │  —       │  ✓       │      │
│ │ Calendar  │  —       │  ✓       │      │
│ │ Integr.   │  —       │  ✓       │      │
│ │ Family    │  —       │  ✓ (6×)  │      │
│ └───────────┴──────────┴──────────┘      │
│                                          │
│ ┌────────────────────┐                   │
│ │ ✓ Annual $59.99/yr │  ← raised price  │
│ │   $4.99/mo billed  │                   │
│ │   No trial         │                   │
│ └────────────────────┘                   │
│                                          │
│ ┌────────────────────┐                   │
│ │   Monthly $7.99    │                   │
│ └────────────────────┘                   │
│                                          │
│ [Get Pro]                                │
│                                          │
│ Continue with Free                       │ ← keep free explicit
│                                          │
│ Restore · Terms · Privacy                │
└──────────────────────────────────────────┘
```

### 6. Screen content

**Headline (Outcome-led, audience-aware):**
- "Get more done with Pro."
- Sub: "Built for serious task management."

**Comparison table format** (5-7 rows max):
- Tasks: 10 / ∞
- Projects: 3 / ∞
- Smart prioritization: — / ✓
- Calendar sync: — / ✓
- Integrations (Slack, GitHub): — / ✓
- Family Sharing (6 accounts): — / ✓

**Pricing block:**
- Annual default $59.99/yr — raised from $39.99 (15% increase test)
- Per-month subordinate: "$4.99/mo billed annually"
- Monthly secondary: $7.99/mo
- **No trial** — controlled test for category

**CTA:**
- Primary: "Get Pro"
- Decline: "Continue with Free" (Productivity users actually use free; honor that)

### 7. Copy variants

**Variant A (current outcome-led):**
- Headline: "Get more done with Pro."

**Variant B (identity-led):**
- Headline: "Built for the way you actually work."

**Variant C (job-to-be-done):**
- Headline: "Stop forgetting things. Start finishing them."

### 8. Layout sketch

Above-fold: close X, headline, social proof, comparison table top rows. Scroll: rest of comparison, plan cards, CTA, decline, legal. Comparison table is the unique element for Productivity.

### 9. Localization notes

- Top 3 markets: US, UK, DE.
- Pricing per Adapty 2026 index:
  - US: $59.99/yr
  - UK: £49.99/yr
  - DE/FR: €54.99/yr (1.2x EU pricing index)
- Tone: Productivity audiences read formality differently — German "Sie" likely OK (technical/professional), French "vous" required.
- CTA length: "Get Pro" (6 char) fits everywhere.

### 10. Tests to run

| # | Hypothesis | Primary metric | Guardrail |
|---|-----------|---------------|-----------|
| 1 | Removing 14-day trial lifts LTV per cohort (Productivity direct > trial) | 12-mo cohort LTV | Install→paid CR |
| 2 | $59.99/yr vs $39.99/yr (15% increase) | RPI | Refund rate |
| 3 | Comparison table vs benefit bullets | Install→paid | LTV |
| 4 | Post-aha placement (after 5+3 tasks) vs post-onboarding | LTV per install | Install→trial |
| 5 | Reverse trial (7-day premium then revert) for low-intent test | LTV | Engagement during trial |

### 11. iOS review risks

**Compliant ✓:**
- Plan structure clear (no toggle) ✓
- Billed amount most prominent ✓
- Restore + Terms + Privacy ✓

**Watch:**
- ⚠️ When removing trial, existing trial-using subscribers must keep access (Apple Rule on previously-purchased)
- ⚠️ Comparison table must be accessible (VoiceOver labels per row)
- ⚠️ "No trial" framing — make sure annual card is clear that there's no free period

### 12. Android delta

Currently iOS-only. Android Productivity audience is similar (price-tolerant, desktop-app-comparable expectations). When expanding:
- Android typically 15-20% lower ARPU than iOS for same SKU — Productivity is one category where this holds
- AppsFlyer 2026: Android growth 4x iOS — Productivity opportunity is real
- Match pricing 1:1 (don't discount Android — audience is similar)

---

## Calculator Output

### Current state
- CR: 11% × 19% = 2.09%
- 12-mo ARPU: ~$45 (mix of monthly + annual + family)
- LTV:CAC at $2 CPI: ~1.0:1 (marginal)

### Recommended (no trial, +15% pricing)
- CR direct: ~3.5% (without trial filter)
- 12-mo ARPU: ~$58 (Productivity direct buyer benchmark)
- LTV:CAC at $2 CPI: ~1.7:1

### After full optimization
- Post-aha placement + comparison table + pricing optimization
- CR: ~4.2%, ARPU: ~$62
- LTV:CAC: ~2.1:1; breakeven ~6 months

### Top 3 actions
1. **Remove trial from default flow.** RC 2026 evidence supports direct purchase for Productivity.
2. **Raise pricing to category median** ($59.99/yr from $39.99).
3. **Move paywall post-aha** (after user completes 3 tasks) instead of post-onboarding.
