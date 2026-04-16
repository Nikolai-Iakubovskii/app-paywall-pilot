# Migration: From Toggle Paywall to Compliant Pattern

Apple started rejecting toggle paywalls under Guideline 3.1.2 in mid-January 2026. If your app was caught in this wave, this is the migration playbook.

For taxonomy of paywall types, see SKILL.md PRESENTATION PATTERN. For specific rejection triage, see [decision-trees.md](../../modules/decision-trees.md) Tree 8.

---

## What Apple Said

**Guideline cited:** 3.1.2 (Business — Payments — Subscriptions)

**Apple's exact reason:**
> "The purchase screen includes a toggle to add or remove a free trial from the subscription purchase. This design is confusing and may prevent users from understanding that they are committing to an auto-renewing subscription."

**Sources:**
- RevenueCat: https://www.revenuecat.com/blog/growth/r-i-p-toggle-paywall-we-hardly-knew-ye/
- Adapty: https://adapty.io/blog/your-toggle-paywall-is-about-to-get-rejected/
- Multiple developer reports starting mid-January 2026

**Scope:** iOS only. Android Play Store and web checkouts are unaffected.

---

## What Got Rejected

The classic toggle paywall pattern:

```
┌─────────────────────────────────────────┐
│  Premium Annual                          │
│  $59.99/year                             │
│                                          │
│  Free trial:  [ON  /  OFF ]   ← Toggle  │
│                                          │
│  [Continue]                              │
└─────────────────────────────────────────┘
```

The toggle defaulted to **off**, meaning the user paid upfront without knowing they could have had a trial. Many users skipped the toggle interaction → revenue went up → Apple eventually flagged.

---

## Replacement Patterns

You have 4 compliant alternatives. Pick based on your existing data + product fit.

### Option 1: Separate Plan Cards (Most Common)

Two distinct plan cards — trial as one option, no-trial as another.

```
┌──────────────────────────────────────────┐
│  ✓  Annual + 7-day free trial            │
│     $59.99/year after trial              │
│     Cancel anytime during trial          │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│     Annual                                │
│     $59.99/year                           │
│     Pay now, no trial                     │
└──────────────────────────────────────────┘

[Continue]
```

**Pros:** Clearest user understanding. Apple-friendly.
**Cons:** Requires two SKUs configured in App Store Connect.

### Option 2: Trial-on-Annual-Only

Single plan card, trial bundled with annual. No choice = no confusion.

```
┌──────────────────────────────────────────┐
│  ✓  Premium Annual                       │
│     7-day free trial                     │
│     then $59.99/year                     │
│     Cancel anytime                       │
└──────────────────────────────────────────┘

[Start Free Trial]
```

**Pros:** Simplest implementation. Adapty Operator Insight: "one of the most consistent patterns."
**Cons:** Less optionality for users; some research suggests subset of users prefer no-trial direct purchase.

### Option 3: Multi-Plan Comparison

3-plan card layout with trial on one selected plan, no toggle.

```
┌─────────┐ ┌─────────────┐ ┌─────────┐
│ Weekly  │ │ ✓  Annual   │ │ Monthly │
│ $4.99   │ │   7-day FREE │ │ $9.99   │
│         │ │   then $59   │ │         │
└─────────┘ └─────────────┘ └─────────┘

[Start Free Trial]
```

**Pros:** Standard pattern, supports decoy effect (Ariely), works with Superwall product-count data (+44% from 3-plan layout).
**Cons:** More design work; needs equal-LTV math across plans.

### Option 4: Personalized / Conditional

Different default plan shown based on user segment. No toggle, but the "right" plan surfaces per user.

```
For low-intent user → Weekly plan default + trial
For high-intent user → Annual plan default + trial
```

**Pros:** Tinder-style ML-driven approach; highest LTV potential.
**Cons:** Engineering complexity; requires user segmentation infrastructure.

---

## Migration Steps

### Step 1: Configure App Store Connect

If switching to **separate plan cards**:
1. Create 2 subscription products in same Subscription Group:
   - `your_app_annual_trial` with 7-day free trial intro offer
   - `your_app_annual_direct` (no intro offer)
2. Both at same price ($59.99/year)
3. Mark both as "ready for sale"

If switching to **trial-on-annual-only**:
1. Keep your existing annual product with intro offer
2. Remove the no-trial variant from the paywall (you can leave it active for legacy users)

### Step 2: Update Paywall UI

- Remove toggle component
- Add plan card layout (see options 1-4 above)
- Verify selected state is visually clear
- Verify trial terms appear next to the trial card

### Step 3: Update Analytics

- Add new event: `plan_card_selected` with plan_id
- Keep old `paywall_impression` events
- Track trial-on vs direct: are users splitting like you expect?

### Step 4: Test

- VoiceOver accessibility on all plan cards
- Dark mode rendering
- Localization (CTA might need to change: "Start Free Trial" vs "Subscribe")
- Restore Purchase still works for old toggle-paywall purchases

### Step 5: Submit Update

- Reference the rejection in your update notes if applicable
- Don't try to "sneak through" — Apple reviewers know this pattern

### Step 6: Monitor

For first 30 days post-launch, watch:
- Trial start rate (may drop slightly without toggle)
- Trial-to-paid rate (may rise — users who chose trial truly wanted it)
- Direct purchase rate (segment of users who DON'T want trial)
- Refund rate (should drop — fewer surprise charges)

---

## Expected Impact

Per Adapty / RevenueCat / RevenueFlo data:

| Metric | Pre-toggle-removal | Post-toggle-removal | Why |
|--------|--------------------|--------------------|-----|
| Trial start rate | ~14% (NA) | ~12-13% | Some "accidental" trial-skippers now skip the whole funnel |
| Trial-to-paid rate | ~28% | ~30-32% | Users who pick trial actually want trial |
| Direct purchase | high | drops | Some buyers actually wanted the trial they were missing |
| Refund rate | elevated | drops 10-30% | Fewer surprise charges |
| **Net LTV** | baseline | **roughly flat to +5%** | Lower revenue offset by lower refunds |

**Caveat:** Single-vendor data, your mileage may vary. Run cohort comparison post-launch (see [cohort-analysis.md](../../modules/cohort-analysis.md)).

---

## What NOT to Do

- ❌ **Don't ship a "subtle" toggle hoping Apple won't notice.** They will.
- ❌ **Don't bury the trial in a "Plans" submenu.** Apple wants trial visible at the same level as the plan.
- ❌ **Don't replace toggle with a popup that asks "do you want a trial?"** Same UX problem rebranded.
- ❌ **Don't remove the trial entirely as a "fix."** Trial-acquired subscribers retain 1.4-1.7x better.

---

## When You Get Re-Rejected

If you replace the toggle but still get rejected:

1. Check that the trial price is **clearly visible next to the trial plan** (Apple Rule)
2. Check that "Free trial then $X/year" reads clearly without scroll
3. Check that the close button isn't delayed >5s (Field Report risk)
4. Check that you don't have two full paywalls back-to-back (Field Report risk)
5. Use [decision-trees.md](../../modules/decision-trees.md) Tree 8 for full triage

---

## Migrations for Other Bans (Likely Future Patterns)

Apple's enforcement style suggests these patterns may face similar bans:

| Pattern | Risk |
|---------|------|
| "Hidden close" buttons (delayed >5s) | High — Field Report 2026 |
| Pricing fonts <16pt | Moderate — RevenueFlo field threshold |
| Two paywalls back-to-back | High — already cited as "aggressive monetization" |
| Fake countdown timers | Already explicit Apple Rule violation |

When in doubt, transparency is the safest design philosophy.

---

## Source

- RevenueCat R.I.P. Toggle Paywall: https://www.revenuecat.com/blog/growth/r-i-p-toggle-paywall-we-hardly-knew-ye/
- Adapty toggle paywall rejection alert: https://adapty.io/blog/your-toggle-paywall-is-about-to-get-rejected/
- RevenueFlo iOS rejections guide: https://revenueflo.com/blog/common-ios-paywall-rejections-and-the-fixes-that-work
- Apple App Store Review Guidelines 3.1.2: https://developer.apple.com/app-store/review/guidelines/#payments
