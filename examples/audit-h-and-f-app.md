# Example Audit: Health & Fitness App

This is a worked example of running the full SKILL.md DEFAULT OUTPUT FORMAT on a fictional H&F app. Use as reference for what a complete audit looks like.

For Productivity audit, see [audit-productivity-app.md](audit-productivity-app.md). For AI app audit, see [audit-ai-app.md](audit-ai-app.md).

---

## Input

**Hypothetical app:** "FitTrack" — habit-tracking app for runners. iOS, US-only.

**Current state:**
- Onboarding: 3 screens (welcome, goal, name)
- Paywall: post-onboarding, single annual plan $79.99/year, no trial
- Free tier: limited to 3 runs / week
- Plans in App Store Connect: 1 (annual)
- Localization: English only
- Markets: US (95%), CA (4%), AU (1%)
- Metrics: install→trial 8% (no trial offered), install→paid D35 4.2%, refund rate 6.1%, monthly churn 12% (annual subscribers)

---

## Audit Output

### 1. Current state

H&F category, hard-paywall variant (3 free runs then locked), $79.99/year single-plan, no trial. US-dominant market mix. ~4.2% install→paid D35 conversion is **above category baseline** (H&F D35: 2.9%) — current product hooks well. Refund rate 6.1% is **above benchmark** (H&F annual: ~4.2%) — surprise factor on the table.

### 2. Main problem or opportunity

Two compounding issues:
- **No trial → leaving 30-50% of LTV on table.** H&F is the highest-impact category for trials (Adapty 2026: H&F trial→paid 35-42%; trial subscribers retain 1.4-1.7x better).
- **Refund rate 6.1% above 4.2% baseline.** Annual paid upfront with no trial = surprise/regret cycle. Adding a trial typically reduces refund rate even as it shifts revenue timing.

Localization is the third compounding issue: English-only in a category where EU/JP/CH have 20-30% higher willingness to pay (Adapty 2026 H&F).

### 3. Recommended access model

**Hard paywall + 7-day free trial** (Adapty 2026: trials work strongly in H&F). Keep the 3-free-runs structure as a "free preview" that demonstrates value before paywall — this is the H&F sweet spot.

### 4. Recommended placements

- **Onboarding paywall (primary):** after 3-screen onboarding, show paywall with trial. 86.1% of H&F conversions are Day 0 (Adapty).
- **Feature gate (secondary):** after the 3rd run completes, show a "you've completed your free week — keep going" paywall with personalization (run count, mile total).
- **Renewal-risk:** push notification 30 days before annual renewal with continued-value summary.
- **Win-back (lapsed):** Apple Win-Back Offer (iOS 18+) for users who let subscription expire. 50% off first year.

### 5. Recommended presentation

**Trial Timeline paywall** (Blinkist pattern, +23% trial signups, -55% complaints). H&F users have anxiety about charge surprises; visual timeline addresses this directly.

```
┌────────────────────────────────────┐
│ [X close]                          │
│                                    │
│ Run smarter. Recover faster.       │ ← outcome headline
│ Personalized for runners like you. │
│                                    │
│ ★★★★★ 4.8 — 12K runs this week   │ ← real social proof
│                                    │
│ ✓ Daily personalized run plan      │ ← outcome bullets
│ ✓ Recovery insights                │
│ ✓ Heart rate zone training         │
│ ✓ Family sharing (up to 6)         │ ← Apple Family lever
│                                    │
│ ┌────────────────────────────┐     │
│ │ Today: Get full access     │     │ ← Trial Timeline
│ │ Day 5: We'll remind you    │     │
│ │ Day 7: Trial ends — $79/yr │     │
│ └────────────────────────────┘     │
│                                    │
│ [Start my free week]               │ ← action+benefit CTA
│                                    │
│ Maybe later                        │ ← neutral decline
│                                    │
│ Restore · Terms · Privacy          │
└────────────────────────────────────┘
```

### 6. Screen content

**Headline (Outcome-led, Rung 1):**
- Primary: "Run smarter. Recover faster."
- Sub: "Personalized for runners like you."

**Benefit bullets (3-5, verb-led):**
- Daily personalized run plan
- Recovery insights between runs
- Heart rate zone training
- Live route tracking with offline mode
- Family Sharing (up to 6 accounts)

**Pricing block:**
- $79.99/year billed annually
- Per-week breakdown subordinate: "$1.54/week · billed annually"
- 7-day free trial messaging on the plan card itself

**CTA:**
- Primary: "Start my free week"
- Decline: "Maybe later"

**Trust line:**
- "7-day free trial. Cancel anytime. Then $79.99/year. Family Sharing supported."
- Restore Purchase · Terms · Privacy

### 7. Copy variants (2-3)

**Variant A (current outcome-led):**
- Headline: "Run smarter. Recover faster."
- CTA: "Start my free week"

**Variant B (identity-led):**
- Headline: "Become the runner you want to be"
- CTA: "Start training"

**Variant C (personalized):**
- Headline: "Your personalized 12-week running plan is ready"
- CTA: "Unlock my plan"

**Locale notes:**
- DE: "Klüger laufen. Schneller erholen." (CTA: "Kostenlos starten")
- JA: "賢く走り、速く回復。" (CTA: "無料で始める")

### 8. Layout sketch

See block diagram in section 5. Above-fold contains: close X, headline, social proof, top 3 benefits, plan card with timeline, CTA. Below fold: extended benefits, comparison Free vs Pro, FAQ, full Terms link.

### 9. Localization notes

- **Localize to top 5 H&F markets:** US, UK, DE, JP, CA (cover ~70% of H&F revenue per Adapty).
- **Pricing tier per market:**
  - US/CA/AU: $79.99/yr (current)
  - UK: £64.99/yr (~1.0x at FX-adjusted, slight premium)
  - DE/FR: €69.99/yr (1.2x via Adapty pricing index)
  - JP: ¥9,800/yr (~$67 at FX)
- **CTA length budget:** EN 25 char ("Start my free week" = 19 ✓), DE 35 char ("Kostenlose Woche starten" = 24 ✓), JA 18 char (testing required).

### 10. Tests to run

Following Adapty 2026 win-rate ranking (localization first, copy/visual last):

| # | Hypothesis | Primary metric | Guardrail | Min sample |
|---|-----------|---------------|-----------|------------|
| 1 | DE/UK/JP localized + 1.2x manual pricing lifts revenue per install in those markets | RPI per market | Refund rate | 200 subs/variant per market |
| 2 | Adding 7-day trial to annual lifts D35 install→paid + reduces refunds | D35 install→paid | Refund rate | 400 subs total |
| 3 | Trial Timeline visual lifts trial start rate vs plain plan card | Install→trial | Trial→paid | 300 subs/variant |
| 4 | 2-plan paywall (annual+monthly) vs 1-plan annual | Install→paid | LTV per cohort | 400 subs/variant |
| 5 | Personalized headline (uses entered name) vs generic | Install→trial | Trial→paid | 300 subs/variant |

Skip pricing tests until #2-4 land — pricing change confounds with structure changes.

### 11. iOS review risks

**Compliant ✓:**
- Billed amount most prominent ✓
- Trial duration + post-trial price visible ✓
- Restore + Terms + Privacy in trust line ✓
- Real ratings (no fakes) ✓
- Outcome-led copy, no banned words ✓

**Watch:**
- ⚠️ Per-week ($1.54/week) breakdown is small enough that it stays subordinate (✓), but verify pricing font size ≥16pt for the $79.99/year text
- ⚠️ When you add the trial, ensure trial card and direct annual aren't toggle-style (Jan 2026 ban)
- ✓ Family Sharing supported — call out as Apple Guidance trust lever

### 12. Android delta (when expanding)

Currently iOS-only. When/if you add Android:
- Play Billing v6+ uses Base Plan + Offer model — trial is an Offer attached to the Base Plan
- Higher involuntary billing failure rate (~31% vs iOS 14%) → implement payment retry UX
- EU DMA requires alternative billing exposure on Android in EU
- AppsFlyer 2026: Android subscription UA growing 4x faster than iOS (consider for emerging markets)

See [android-parity.md](../modules/android-parity.md) for full detail.

---

## Calculator Output (Predicted Impact)

Running [unit-economics-calculator.md](../modules/unit-economics-calculator.md) on the recommended state vs current:

### Current state
- Plans: 1 annual @ $79.99 (100%)
- CR: 4.2%, CPI: $3, Apple SBP 15%
- Result: 12-mo ARPU = $68; CAC = $71; LTV:CAC ≈ 1.0:1 (marginal)

### Recommended state (post-changes)
- Plans: 1 annual @ $79.99 with trial (100%)
- Trial start: 12% (NA benchmark for H&F), Trial-to-paid: 38% (H&F median)
- Effective CR: 4.6%
- Localized for top 5 markets, ~12% blended ARPU lift from EU/JP pricing
- Result: 12-mo ARPU = $76 (US) / $90 blended; CAC = $65; LTV:CAC ≈ 1.4:1

### After full optimization (next phase)
- Add 2nd plan (monthly $14.99 — captures non-annual buyers)
- Trial Timeline paywall + personalized headline
- Effective CR: 5.5%
- Result: 12-mo ARPU = $84; CAC = $54; LTV:CAC ≈ 1.6:1; breakeven ~7 months

**Top 3 actions in order:**
1. Add 7-day trial to annual (single biggest lift; expected +25-30% LTV)
2. Localize for DE/UK/JP with 1.2x pricing (+10-15% blended ARPU)
3. Implement Trial Timeline paywall + personalization (additional +5-10%)
