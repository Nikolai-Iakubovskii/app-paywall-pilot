# Decision Trees

When you face a common paywall problem, follow the tree. Each node references the relevant taxonomy axis and benchmark from SKILL.md or other modules.

---

## Tree 1: Choosing an Access Model

```
Q: Is the core value of your app obvious in <30 seconds without using premium features?
├── YES → Q: Does first-time use require premium to demonstrate value?
│         ├── YES → HARD PAYWALL
│         │        Source: RC 2026 — Hard paywall D35: 10.7% vs Freemium 2.1%
│         │        Best for: H&F, AI tools, Education with assessment
│         │
│         └── NO → REVERSE TRIAL or SOFT PAYWALL
│                  Source: RC Operator Insight — Reverse trial for low-intent
│                  Best for: Productivity, Lifestyle, Photo editors
│
└── NO → Q: Does usage have natural metering (queries, exports, actions)?
          ├── YES → METERED PAYWALL
          │        Apple Guidance: documented as valid acquisition model
          │        Best for: AI tools, news, learning, utilities
          │
          └── NO → FREEMIUM
                   Apple Guidance: documented as valid acquisition model
                   Best for: virality-required apps (social, dating, games)
```

---

## Tree 2: Diagnosing Low Trial Conversion

```
Symptom: Install→trial below benchmark (NA <12% per Adapty 2026)

Q: Is paywall placed before user understands the value?
├── YES → Move paywall to after first value moment
│         Source: Adapty Operator Insight — "framing before paywall > paywall itself"
│
└── NO → Q: Is the headline outcome-led or feature-led?
          ├── FEATURE-LED → Switch to outcome-led headline
          │                  See: copy-library.md → Headline Formulas #1, #3, #6
          │
          └── OUTCOME-LED → Q: Is there real social proof above the fold?
                            ├── NO → Add real rating + user count
                            │        Source: Cialdini → Social Proof = most influential
                            │
                            └── YES → Q: Is plan card clear (one default selected)?
                                      ├── NO → Pre-select annual; visually highlight
                                      │
                                      └── YES → Test trial structure (60% LTV win rate)
                                                Source: Adapty 2026 paywall experiments
```

---

## Tree 3: Diagnosing Low Trial-to-Paid Conversion

```
Symptom: Trial→paid below benchmark (global 25.6%, H&F 35–40% per Adapty/RC 2026)

Q: How long is your trial?
├── ≤4 days → Q: Is value obvious in this time?
│              ├── YES (gaming, fast utilities) → Trial length is OK
│              │
│              └── NO → Extend to 7 days
│                       Source: RC 2026 — 5–9 day trials: 37.4% conversion
│
├── 7 days → Trial length is OK; look elsewhere
│
└── 30 days → Q: Are you in low-intent or behavior-change category?
              ├── YES (Strava, Headspace) → Trial length is OK
              │
              └── NO → Shorten to 7 days
                       Source: RC 2026 — long trials = more chance to forget/cancel

If trial length OK:
Q: Do users get reminder before billing?
├── NO → Implement Day 5 push (Blinkist pattern: +1,200% notif opt-in)
│        Source: Blinkist case study via Purchasely
│
└── YES → Q: Is it visible WHEN they'll be charged?
          ├── NO → Add Trial Timeline visual (Today → Day 5 → Day 7)
          │        Source: Blinkist case study — +23% trial signups, +4% retention
          │
          └── YES → Cancellation is by intent, not surprise. Look at:
                    - Pricing tier match for your audience (LTV by tier)
                    - Refund rate (if high, value didn't land in trial)
```

---

## Tree 4: Choosing Plan Architecture

```
Q: Does your value differ meaningfully across tiers?
├── NO → SINGLE PLAN (Calm pattern)
│        Source: Calm operator analysis
│        Pros: no choice paralysis
│        Cons: no decoy / anchor effect
│
└── YES → Q: How many MEANINGFULLY different tiers?
          ├── 2 tiers → 2-PLAN PAYWALL (41–60% of apps per RC 2026)
          │             Default presentation: annual + monthly
          │             Or: Family + Individual (Duolingo)
          │
          ├── 3 tiers → 3-PLAN PAYWALL (Travel: 27% of apps; Productivity: ~10%)
          │             Source: Superwall — 3 vs 2 = +44% conversion
          │             Caveat: ensure equal LTV across plans
          │
          └── 4+ tiers → Hide behind "More Plans"; surface 3 by default
                          Source: ChatGPT 6-tier with disclosure pattern
```

---

## Tree 5: Should You Run a Discount?

```
Q: Where in the lifecycle?
├── Onboarding paywall → NO DISCOUNT
│   Source: Adapty 2026 — 90% of subs sell at full price
│   Reason: trains discount expectation, erodes anchor
│
├── Post-close (just dismissed paywall) → YES, 20–30%
│   Source: Adapty 2026 — Post-close offers: 10–15% ARPU lift
│   Window: 24h
│
├── Transaction abandon (cancelled payment sheet) → YES, ALTERNATIVE OFFER
│   Source: Superwall 2024 — 17% of total revenue from abandon paywalls
│   Pattern: soft prompt with cheaper plan, not full second paywall
│   Apple field report: two full paywalls back-to-back = rejection risk
│
├── Renewal-risk (auto-renew off) → YES, 20–40%
│   Use: Apple Promotional Offer
│   Source: Platform Capability — Server Notifications V2
│
├── Win-back (lapsed) → YES, 30–50% one-time
│   Use: Apple Win-Back Offer (iOS 18+)
│   Source: Platform Capability
│
└── Random in-app prompt → NO
    Reason: trains users to wait for discount
```

---

## Tree 6: Which Surface Should Render the Paywall?

```
Q: Do you need full design control + custom interactions?
├── YES → CUSTOM IN-APP (Flutter/SwiftUI/UIKit) with Adapty/RC product data
│         Best for: brand-led apps, A/B testing, custom layouts
│
└── NO → Q: Do you iterate paywalls weekly without app update?
          ├── YES → ADAPTY/RC PAYWALL BUILDER (remote-configured)
          │         Best for: rapid iteration, localization at scale
          │
          └── NO → Q: Is it a settings/upgrade screen with simple merchandising?
                    ├── YES → STOREKIT VIEWS (SubscriptionStoreView, iOS 17+)
                    │         Best for: Apple-native look, fast localization
                    │
                    └── NO → SYSTEM SHEET (billing problem, price increase, offer sheet)
                              Best for: failed renewal recovery, required consent

Special cases:
- Lapsed user reactivation → APP STORE WIN-BACK SURFACE (iOS 18+)
- Transaction abandon → SYSTEM-PROVIDED SHEET or custom soft prompt
- US-only commission avoidance → WEB CHECKOUT (post Epic v. Apple, May 2025+)
```

---

## Tree 7: When to Test What

Use Adapty's 2026 win-rate ranking. Tests with low base rates are not worth running until structural tests are exhausted.

```
1. Is your paywall localized for top 5 revenue markets?
   ├── NO → LOCALIZE FIRST (62.3% LTV win rate)
   │         Includes: language + currency + regional pricing
   │
   └── YES ↓

2. Have you tested trial length and structure?
   ├── NO → TEST TRIAL STRUCTURE (59.6% win rate)
   │         e.g., trial-on-annual-only, 3 vs 7 days, intro offer
   │
   └── YES ↓

3. Have you tested plan duration (weekly vs monthly vs annual default)?
   ├── NO → TEST PLAN DURATION (58.7% win rate)
   │
   └── YES ↓

4. Have you tested number of plans (1 vs 2 vs 3)?
   ├── NO → TEST PLAN COUNT (57.1% win rate)
   │         Source: Superwall — 1→2: +61%, 2→3: +44%
   │
   └── YES ↓

5. Have you tested pricing levels?
   ├── NO → TEST PRICE (45.5% win rate)
   │         Caution: requires App Store Connect SKU per variant
   │
   └── YES ↓

6. Now (and only now) test visual/copy (34.6% win rate)
```

**Sample size minimum:** 200 subscriptions per variant (Adapty 2026, vendor_blog).

---

## Tree 8: Compliance Triage (When You Get Rejected)

```
Q: Apple cited Guideline 3.1.2?
├── YES → Q: Do you use a toggle for free trial on/off?
│          ├── YES → TOGGLE PAYWALL — REPLACE
│          │        Source: RC + Adapty Feb 2026 mass rejections
│          │        Replace with: separate plan cards OR trial-on-annual-only
│          │
│          └── NO → Check: misleading savings, fake urgency, fake reviews,
│                   missing trial terms, price not most prominent
│
├── Q: "Confusing pricing" cited?
│   └── Check: per-week price larger than billed amount, savings math wrong,
│       trial duration unclear, post-trial price hidden
│
├── Q: "Misleading marketing" cited?
│   └── Check: fake "X% off" without reference, fake countdown timer,
│       fake user counts, fake testimonials
│
└── Q: "Aggressive monetization" cited?
    └── Check: two full paywalls back-to-back, multiple paywalls per session,
        forced re-entry to dismiss
```

**Don't fix-and-resubmit if pattern is structural.** A toggle paywall with cosmetic tweaks will likely re-reject. Replace the pattern.

---

## Tree 9: Diagnosing High Refund Rate

```
Symptom: Refund rate >5% (Apple iOS 2026 baseline ~2–3%)

Q: Is your trial length matched to value-delivery time?
├── NO (trial too short, user didn't see value) → Extend trial
│
└── YES → Q: Is your value claim verifiable in trial?
          ├── NO (overpromise) → Tone down claims to what trial actually delivers
          │
          └── YES → Q: Is your billing surprise-free?
                    ├── NO → Add Trial Timeline (Blinkist pattern: -55% complaints)
                    │
                    └── YES → Look at:
                              - Subscriber acquisition channel quality
                              - Paid traffic bot/fraud
                              - Wrong audience targeting (UA mismatch)
```

**APAC note:** Adapty 2026 — Photo & Video category has 14.1% refund rate in APAC, highest. Region-specific refund risk is real.

---

## Tree 10: Dealing with Conflicting Vendor Recommendations

```
Q: Do Adapty and RevenueCat agree on the metric?
├── YES → Use the cross-referenced number (e.g., Day 0 trial start ~80–90%)
│
└── NO → Q: Whose dataset is closer to your category/region?
          ├── Adapty is bigger in: Europe, H&F dataset (deep)
          ├── RC is bigger in: NA, broader category coverage
          └── Use the geographically/categorically closer one

Q: Does vendor data conflict with Apple guidance?
└── ALWAYS FOLLOW APPLE
    Source: SKILL.md SOURCE OF TRUTH section
```
