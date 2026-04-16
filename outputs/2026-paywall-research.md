# 2026 Paywall Benchmark Research Brief

**Date:** 2026-04-16
**Purpose:** Source manifest and synthesis for app-paywall-pilot SKILL.md v3.2 update.
**Method:** WebSearch + WebFetch on primary vendor reports, academic papers, and operator blogs. Cross-referenced where possible.

---

## Executive Summary

The 2026 vendor benchmarks (Adapty 16K apps, RevenueCat 115K apps, AppsFlyer 1.7B installs across 2,900 apps) converge on a clear picture: weekly plans now drive ~55% of revenue, hard paywalls outperform freemium ~5x in conversion and ~21% in LTV per subscriber, 80–90% of trial starts happen Day 0, and apps that systematically test earn 18–40x more revenue. The biggest single A/B-test win category remains **localization** (62.3% LTV win rate), not visual or copy tweaks (34.6%) [1][3].

Apple began enforcing Guideline 3.1.2 against toggle paywalls in mid-January 2026, citing "confusing" design that obscures auto-renewal commitments [6][7]. This is the most consequential compliance shift of the year.

Pricing psychology has 30+ years of academic backing — Tversky & Kahneman (1981) on framing [15], Anderson & Simester (2003) on $9 endings [17], Ariely on decoy effects [16] — but isolated mobile-paywall data on these specific tactics remains scarce. Treat academic principles as **Operator Insight** when applied to mobile, not as Vendor Aggregate Data.

---

## 1. Adapty State of In-App Subscriptions 2026

**URL:** https://adapty.io/state-of-in-app-subscriptions/
**Date:** 2026-03-14
**Scope:** 16,000 apps, $3B subscription revenue tracked, 500M transactions, 105,000 paywalls compared, 50+ countries, 20+ sub-categories
**Evidence Class:** large_scale_report

### Verified findings

| Metric | Value | Notes |
|--------|-------|-------|
| Global median weekly price | $7.48 | Range $5.71–$8.94 by region |
| Global median monthly price | $12.99 | |
| Global median annual price | $38.42 | EU 29–39% above NA |
| Weekly plans share of revenue | 56% (55.5%) | Up from 43.3% in 2023 |
| Install→trial global | 10.9% | NA: 14.5% |
| Trial→paid global | 25.6% | H&F: 35.0%; Entertainment: 19.1% |
| Day 0 trial starts | 90% | 89.4% on first-session paywall |
| Hard paywall LTV uplift vs soft | +21% per subscriber | |
| 50+ experiments per year revenue uplift | 40x vs non-experimenters | "Operator Insight" — correlation, methodology not open |
| Top 10% capture revenue share | 94.5% | |
| Median app monthly revenue | $492 | 59.3% under $1K total |
| Annual trial subscriber D380 retention | 19.9% | Monthly: 14.2%, Weekly: 5.5% |
| Trial vs direct buyer retention | 1.4–1.7x better | |
| Utilities first-renewal retention | 58.1% | Highest |
| H&F first-renewal retention | 30.3% | Lowest |
| Utilities trial 12-mo LTV | $68.90 | |
| Weekly+trial 12-mo LTV | $49.27 | |

### Adapty A/B test win rates [3]

(Vendor-blog evidence — Adapty platform experiments, methodology not open)

| Test category | LTV win rate |
|---------------|-------------|
| Localization | 62.3% |
| Trial structure | 59.6% |
| Plan duration | 58.7% |
| Number of plans | 57.1% |
| Price changes | 45.5% |
| Visual / copy | 34.6% |

### Adapty H&F deep-dive [4]

**URL:** https://adapty.io/blog/health-fitness-app-subscription-benchmarks/

- Annual plans dominate: 61% of category revenue (only category where this holds)
- Install LTV $1.21 (highest of any category)
- 86.1% of conversions Day 0; secondary peak Days 4–7 at 2.6%
- 4.4x pricing variance across markets (DE/JP/CH high; TR/IN/ID low)
- High-priced annuals: 4.5x LTV vs budget annuals
- Onboarding paywalls with trials: 1.78% install→paid

---

## 2. RevenueCat State of Subscription Apps 2026

**URL:** https://www.revenuecat.com/state-of-subscription-apps/
**Date:** 2026-03
**Scope:** 115,000+ apps, $16B+ revenue, 1B+ transactions
**Evidence Class:** large_scale_report

### Verified conversion data

**Download → Trial (D30 median):**
- Business: 9.1% (highest)
- Gaming: 4.4%
- North America: 7.1%
- IN/SEA: 3.0–3.7%

**Trial → Paid (median):**
- Travel: 43.5% (highest)
- Health & Fitness: 37.7%
- Photo & Video: 22.2% (lowest)
- 17–32 day trials: 42.5%
- ≤4 day trials: 25.5%

**Download → Paid (D35 median):**
- Hard paywall: 10.7%
- Freemium: 2.1%
- Health & Fitness: 2.9%
- North America: 2.8%
- IN/SEA: 0.7%

### Verified RPI

**D14 RPI (Hard paywall):** $2.32
**D60 RPI (Hard paywall):** $3.09
**D60 RPI (Freemium):** $0.27 → $0.38 (depending on cut)
**D14 RPI by category:** H&F $0.48, Gaming $0.08, NA $0.38, IN/SEA $0.08

### RLTV per payer

- 12-month by category: Business $35.48, H&F $35.64, Gaming $11.22
- 12-month by region: NA $32, WE $25, IN/SEA $14
- 12-month by tier: High $62.19, Mid $28.75, Low $10.69

### Trial cancellation timing

- 3-day trials: 55.4% cancel Day 0
- 7-day trials: 39.8% cancel Day 0

### Trial length distribution shift YoY

- ≤4 days: 46.5% (up from 42.1%)
- 5–9 days: 39.9% (down from 43.5%)
- 17–32 days: 5.0% (down from 6.1%)
- Gaming: 73% use ≤4 day trials
- H&F: 54% use 5–9 day trials

### Plan distribution

- 2-plan paywalls: 41–60% of apps (most common)
- 1-plan: 20–40% (Shopping leads at 40%)
- 3+ plans: 6–27% (Travel leads at 27%)

### UI elements used (median)

- Highlighted pricing: 74.5%
- Multi-plan: 59.2%
- Free trial messaging: 54.0%
- Testimonials: 5.9–16.9% by category
- Countdown timers: ≤1.4%

### Refunds

- Google Play involuntary billing failures: ~31% of cancellations
- App Store involuntary billing failures: 14% of cancellations

### Retention by plan duration (12-mo)

- Annual: 44.1%
- Monthly: 17.0%
- Weekly: 3.4%

### Market composition

- Jan 2026 launches: ~14,700/month (vs 2,000/month Jan 2022)
- iOS launches: 77% of total (up from 67% in 2023)
- Pre-2020 apps: 69% of all category revenue
- 2025+ launches: 3% of total revenue

---

## 3. Superwall Studies

### Product count study [8]

**URL:** https://superwall.com/blog/how-many-products-should-you-offer-on-your-paywall
**Scope:** 32,303,995 paywall opens, 383,889 conversions, 15 largest apps (each >10K paywall views), apps with ≥2 tests of different product counts
**Evidence Class:** aggregate_study

| Comparison | Lift |
|-----------|------|
| 1 → 2 products | +61% conversion |
| 2 → 3 products | +44% conversion |
| 4+ products | No data |

**Documented caveats:**
- Doesn't account for whether products are visually obvious or hidden behind "More Pricing"
- Doesn't control for price or duration
- Trial conversion and retention vary significantly by product mix
- Default selection effect not measured

**Author warning:** ensure equal LTV across products to avoid sacrificing long-term growth for conversion.

### Transaction abandon study [9]

**URL:** https://superwall.com/blog/17-revenue-boost-with-transaction-abandon-paywalls-a-case-study/
**Date:** 2024-08
**Scope:** 18 companies, 438,144 control users, 87,403 variant users (>1,000 users + >$0 revenue per group)
**Evidence Class:** aggregate_study

| Metric | Control | Variant (abandon) |
|--------|---------|-------------------|
| Conversions | 39,063 | 5,128 |
| Conv rate | 8.9% | 6.3% |
| Revenue | $394,960 | $80,590 |
| Refund rate | 6.8% | 3.3% |

**Key finding:** ~17% of total revenue from abandon paywalls, despite only ~20% of paywalled users encountering them. Lower refund rate suggests users on these paywalls are more deliberate.

### Multi-page vs single-page (2025 review) [10]

**URL:** https://superwall.com/blog/superwall-ships-recap/

Mixed result. Superwall confirms multi-page paywalls work for storytelling and trial-anxiety reduction, but **single-page paywall outperformed multi-page in at least one test with significant yearly trial-start lift** in their 2025 dataset. Conclusion: pattern depends on app, not universal — keep as Hypothesis level.

---

## 4. AppsFlyer State of Subscriptions 2026

**URL:** https://www.appsflyer.com/resources/reports/subscription-marketing/
**Scope:** 1.7B paid installs, 2,900 subscription apps, 13 categories, $2.1B UA spend
**Evidence Class:** large_scale_report

### Verified findings

- Subscription UA spend grew 24% YoY; **Android growing 4x faster than iOS**
- Indian Subcontinent: 49% of net Android paid install growth; LATAM: 18%
- North America: essentially flat
- Short Drama: +155% YoY paid installs (fastest-growing category)
- OTT subscription-only share: 53% → 62% YoY (consolidating to pure sub)
- Short Drama ad-supported revenue: ~0% → 7.4% (moving away from pure sub)
- Top 5 apps per category control >90% of UA spend

**Implication:** UA cost economics now diverge sharply by geo. NA-only apps face flat user pool; emerging markets are where Android growth happens, with lower RLTV (~$14 vs NA $32).

---

## 5. Apphud

**URL:** https://apphud.com/blog/scale-app-revenue-with-apphud
**Evidence Class:** vendor_blog (no documented sample size in public posts)

Apphud publishes:
- 80% of free trials convert on Day 1
- Trial conversion benchmark 25–30%
- 99.9% data-match accuracy with App Store transactions on connected apps
- Case study: Trial→Sub improved 10% → 25% in 6 months (single partner)

**Note:** No published large-scale aggregate report comparable to Adapty/RevenueCat as of April 2026. Apphud benchmarks should be cited as vendor_blog unless a methodology page is found.

---

## 6. Apple Toggle Paywall Rejections (2026)

**Sources:**
- Adapty: https://adapty.io/blog/your-toggle-paywall-is-about-to-get-rejected/
- RevenueCat: https://www.revenuecat.com/blog/growth/r-i-p-toggle-paywall-we-hardly-knew-ye/
- RevenueFlo: https://revenueflo.com/blog/common-ios-paywall-rejections-and-the-fixes-that-work
- Apple Review Guidelines: https://developer.apple.com/app-store/review/guidelines/

### Verified facts

- **Timeline:** Mass rejections began mid-January 2026; Axel Le Pennec among first to publicly report
- **Apple's exact citation:** Guideline 3.1.2; Apple's reason quote: "The purchase screen includes a toggle to add or remove a free trial from the subscription purchase. This design is confusing and may prevent users from understanding that they are committing to an auto-renewing subscription."
- Specifically falls under **3.1.2(a)** anti-scam provision: "trick users into purchasing a subscription under false pretenses"
- **Scope:** iOS only. Android Play Store and web checkout unaffected.

### Other field observations from RevenueFlo

| Pattern | Risk |
|---------|------|
| Delayed close button >5s | High rejection correlation |
| Pricing font <16pt | Threshold for safer compliance |
| Two full paywalls back-to-back (e.g. main + abandon) | Aggressive monetization flag |
| Guilt-trip decline copy | High rejection correlation |
| Auto-renewal terms missing | Best practice, not yet hard rejection (April 2026) |

**Evidence Class:** field_observation (developer reports, not official Apple rule).

---

## 7. Big-App Paywall Teardowns

Sourced from independent operator analyses, screenshot libraries, and case studies. Each entry: **structure, copy pattern, key takeaway, source**.

### Calm [Sources: 18, 19, 20]

- Single subscription plan (annual) — eliminates choice paralysis
- Strikethrough monthly price as anchor; price-per-month breakdown subordinate to annual price
- Dark gradient background; benefits list pop
- Pre-selects yearly, labels "most popular"
- Family plan upsell: 6 accounts at £40.99/year
- Transparency line: "7-day free trial, then $X. Cancel anytime."
- **Takeaway:** simplicity > optionality when value is universal (meditation = same for everyone). Single-plan paywall = unusual but works for unsegmented value.

### Duolingo [Sources: 21, 22]

- Polished brand-consistent design (signature gradient, mascot)
- 7-day free trial framed as "Start my free week" — outcome CTA, not generic "Subscribe"
- Personalized first benefit bullet based on entry placement
- Two plans: Family vs Individual (NOT trial vs no-trial)
- 7+ paywall touchpoints in single new-user session (aggressive but works)
- ARPU rose 6% YoY in 2025 from Max tier upsell
- **Weakness:** doesn't always explain what "Super" includes (no ad-removal/offline call-out on every variant)
- **Takeaway:** brand consistency at paywall raises trust; CTA should match action ("Start my free week" > "Subscribe")

### Noom [Sources: 23, 24, 25]

- 77-step onboarding quiz (~7 min) before paywall
- "Personalized plan reserved" — commitment+consistency lever (Cialdini)
- Local currency via geo-IP detection
- 15-min countdown timer for "your reserved plan"
- 7-day free trial on 2-month plan (unusual: trial NOT on annual)
- $17.42/month equivalent for 12-month plan
- **Takeaway:** long onboarding = effort investment that primes commitment. Personalized preview of plan + scarcity timer = double Cialdini. Caution: 15-min timer is fake-urgency adjacent — verify it actually expires, otherwise Apple Rule violation.

### Cal AI [Sources: 26, 27, 28]

- Hard paywall: card required before app use
- Onboarding starts with demo video, deep personalization, animations
- Mid-onboarding review prompt
- Personalized plan generation
- Annual heavily pushed via "75% off" framing
- Pricing: $2.99/week to $29.99/year
- $1.4M/month gross profit (CNBC, 2025) on 30M+ downloads
- Built by 2 teenagers — proof that execution > resources
- **Takeaway:** hard paywall + obsessive personalization + single core action = repeatable formula. Caution: 75% off requires legitimate reference price under Apple Rule.

### Tinder [Sources: 29, 30]

- Curiosity-driven blur-to-reveal: blurred matches screen who liked you
- ~8% upgrade conversion specifically to unblur
- ML-driven dynamic paywall: predicts best product per user, surfaces only that one
- a la carte fallback if user rejects subscription
- 7-day Passport priced equal to 7-day Plus → makes Plus look better value (decoy)
- Tier ladder: Plus → Gold → Platinum
- **Takeaway:** **Zeigarnik effect (incomplete-task tension)** as deliberate paywall trigger. Dynamic paywall = personalization at choice level, not just copy.

### Strava [Sources: 31, 32]

- Slow gradual paywalling of features (2024–2026)
- Year in Sport now subscriber-only ($80/year) — caused 2025 backlash
- 30-day full-access trial without credit card (unusual transparency)
- Monthly $11.99 vs annual $79.99 = $144 anchor, makes annual a clear bargain
- Inline subscription CTAs in main UI (not modal interruption)
- **Takeaway:** no-CC trial = ultimate trust signal. But aggressive paywalling of historically-free features risks brand backlash; proceed only when value of locked feature is clearly post-aha.

### Headspace [Sources: 33, 34, 35]

- Day/night theme adaptive paywall (auto-switches by time)
- 100% locked content library after free preview
- Kept 1–2 free items per category as retention hook
- Monthly + annual equal prominence (intentional — monthly is preferred reminder for some segment)
- Segmented messaging by user interest (sleep vs stress vs focus)
- Headline "Cancel anytime. No commitment." for transparency
- **Takeaway:** segmentation at copy level, not just placement. Equal-prominence plans sometimes optimal — annual default is not universal best.

### Blinkist [Sources: 36, 37, 38, 39]

- "Free Trial Timeline" paywall: visual Today → Day 5 reminder → Day 7 charge
- Driver: exit survey said users didn't know when they'd be charged
- Results: +23% trial signups, -55% complaints, +4% trial retention, +1,200% notification opt-in (6%→74%)
- Single most-cited trial-anxiety solution
- Now standardized as "STEPS" template in Purchasely
- **Takeaway:** transparency converts. Visual timeline beats text disclosure.

### Flo [Sources: 40, 41]

- 70-screen onboarding (~7 min)
- Personalization via name + empathy ("you're not alone")
- 14-day free trial toggle (NOTE: this is a toggle pattern — likely needs review against new 2026 Apple guidance)
- Yearly default, monthly+family on scroll
- $49.99/year Premium
- $6M/month subscription revenue from ~1M downloads/month
- 60–80% of purchases at first app use
- Core cycle tracking remains free (preserves brand trust)
- **Takeaway:** **long onboarding consistently appears in highest-revenue H&F apps**. Free core + premium tier = trust + monetization balance.

### ChatGPT (OpenAI) [Sources: 42, 43]

- 6 tiers as of March 2026: Free, Go ($8 emerging-markets price), Plus ($20), Business, Enterprise, Edu
- $20/mo anchor normalized industry pricing for AI apps
- Geo-tier (Go) launched India first then global expansion
- Plus offers: priority access, GPT-5.3, image gen, deep research
- **Takeaway:** ChatGPT made $20/mo the AI baseline. Other AI apps inherit this ceiling whether they like it or not. Geo-tier pricing for emerging markets = growing pattern.

### Replika / similar AI companion (industry pattern)

- Hard paywall on advanced relationship features
- Voice/video unlocked via Pro
- Often weekly+monthly+annual ladder
- Higher price tolerance than non-AI ($15–25/mo norm)
- Higher churn (RC: AI churns ~30% faster than category avg)
- **Takeaway:** AI = high price tolerance + high churn. Optimize for first-month conversion, not long retention. Annual+trial is the LTV anchor.

---

## 8. Pricing Psychology — Academic + Mobile Adaptation

### Tversky & Kahneman (1981) — Framing [15]

**URL:** https://www.science.org/doi/10.1126/science.7455683
Published in Science, 17,000+ citations.

Same factual decision presented with different framing produces predictable preference reversals. Direct application:
- "Save $40/year" (gain frame) vs "Lose $40 if you choose monthly" (loss frame)
- Loss aversion typically wins ~2:1 in decision experiments
- Mobile paywall application: frame trial as "lose access on Day 7" vs "keep access" — operator data inconclusive but theoretically loss-frame should perform better

### Anderson & Simester (2003) — $9 Endings [17]

**Citation:** Quantitative Marketing and Economics, 1, 93–110.
Field experiment: same product priced $39 vs $44 vs $34. **$39 outsold $34** in their catalog test (controlling for the .99 effect distinct from price level).

### Thomas & Morwitz (2005) — Left-Digit Effect

Consumers encode prices left-to-right. "$9.99" anchors on "9", not interpolated to ~$10. Brain compresses the cents into noise.

### Ariely Decoy Effect [16]

The Economist subscription test (n=100 MIT students):
- 3 options (with print-only $125 decoy): 84% chose combo $125
- 2 options (decoy removed): 32% chose combo, 68% chose online-only $59
- ~30% revenue increase from decoy presence

**Caveat (cited in research community):** when retested with real (non-hypothetical) money on different populations, decoy effect is weaker. Treat as Operator Insight in mobile paywall context, not as hard quantitative law.

### Cialdini — 7 Principles

Originally 6 (Influence, 1984); Pre-Suasion (2016) added Unity.

| Principle | Mobile paywall expression |
|-----------|---------------------------|
| Reciprocity | Free trial, free preview content |
| Commitment & Consistency | Long onboarding quiz, personalized plan reserved |
| Social Proof | "300K+ users", testimonials, rating stars, "Most popular" badge |
| Authority | Expert endorsements, academic citations, "Recommended by doctors" |
| Liking | Brand voice, personalized greeting, mascot/character |
| Scarcity | Limited-time offer, countdown timer (must be real per Apple Rule) |
| Unity | "Built for runners by runners", in-group framing |

Research note: Social Proof and Authority test as **most influential** principles; Scarcity as **least but still significant** in 2024 mobile-app studies.

---

## Open Questions / Unresolved

1. **Multi-page vs single-page paywalls:** Conflicting results. Speak4Me +27% multi-page, Stompers +X single-page. No universal verdict.
2. **Trial-on-annual-only vs all-plans:** Adapty consistently recommends annual-only; no isolated A/B data published.
3. **Animated vs static paywalls:** Adapty claims 2.9x conversion uplift for animated, but methodology not open. Treat as vendor_blog hypothesis, not verified.
4. **Personalization lift:** Adapty cites 15%+ from personalized headlines; methodology not open. Plausible given Cialdini commitment principle, but exact magnitude unverified.
5. **Reverse trial:** RevenueCat recommends for low-intent, no published quantitative data.
6. **Apphud aggregate report:** Apphud lacks a public 2026 large-scale report comparable to Adapty/RC. Their "80% Day-1 trial conversion" needs sample-size disclosure.
7. **Apple 16pt pricing minimum:** RevenueFlo cites it as observed threshold; Apple has not published a numeric minimum.
8. **Decoy pricing in mobile:** No published mobile-specific A/B confirming Ariely's catalog finding. Anecdotal only.

---

## Sources

[1] Adapty State of In-App Subscriptions 2026 — https://adapty.io/state-of-in-app-subscriptions/ (2026-03-14, 16K apps, $3B revenue, large_scale_report)

[2] RevenueCat State of Subscription Apps 2026 — https://www.revenuecat.com/state-of-subscription-apps/ (2026-03, 115K apps, $16B revenue, large_scale_report)

[3] Adapty Paywall Experiments Playbook — https://adapty.io/blog/paywall-experiments-playbook/ (2026, vendor_blog)

[4] Adapty Health & Fitness Benchmarks 2026 — https://adapty.io/blog/health-fitness-app-subscription-benchmarks/ (2026, large_scale_report subset)

[5] Adapty High-Performing Paywall 2026 — https://adapty.io/blog/high-performing-paywall-2026/ (2026, vendor_blog)

[6] Adapty Toggle Paywall Rejection — https://adapty.io/blog/your-toggle-paywall-is-about-to-get-rejected/ (2026-02, field_observation)

[7] RevenueCat R.I.P. Toggle Paywall — https://www.revenuecat.com/blog/growth/r-i-p-toggle-paywall-we-hardly-knew-ye/ (2026-02, field_observation)

[8] Superwall Product Count Study — https://superwall.com/blog/how-many-products-should-you-offer-on-your-paywall (2025, aggregate_study, 32M opens)

[9] Superwall Transaction Abandon Case Study — https://superwall.com/blog/17-revenue-boost-with-transaction-abandon-paywalls-a-case-study/ (2024-08, aggregate_study, 18 companies)

[10] Superwall 2025 Year in Review — https://superwall.com/blog/superwall-ships-recap/ (2025, vendor_blog)

[11] AppsFlyer State of Subscriptions 2026 — https://www.appsflyer.com/resources/reports/subscription-marketing/ (2026, large_scale_report, 2.9K apps)

[12] Apphud Subscription App Revenue Growth Guide — https://apphud.com/blog/scale-app-revenue-with-apphud (2025, vendor_blog)

[13] RevenueFlo Common iOS Paywall Rejections — https://revenueflo.com/blog/common-ios-paywall-rejections-and-the-fixes-that-work (2026, field_observation)

[14] Apple Review Guidelines — https://developer.apple.com/app-store/review/guidelines/ (current, apple_docs)

[15] Tversky & Kahneman, "The Framing of Decisions and the Psychology of Choice," Science 1981 — https://www.science.org/doi/10.1126/science.7455683 (academic, 17K citations)

[16] Ariely Decoy Effect Economist Experiment — https://thestrategystory.com/2020/10/02/economist-magazine-a-story-of-clever-decoy-pricing/ (secondary, behavioral econ)

[17] Anderson & Simester, "Effects of $9 price endings on retail sales: Evidence from field experiments," Quantitative Marketing and Economics 1 (2003): 93–110 — academic field study

[18] Calm paywall analysis (Kristen Berman) — https://kristenberman.substack.com/p/how-calm-uses-premium-to-motivate (operator)

[19] Calm via Adapty Paywall Library — https://adapty.io/paywall-library/calm/ (screenshot ref)

[20] Calm via ScreensDesign — https://screensdesign.com/showcase/calm (screenshot ref)

[21] Duolingo paywall via Adapty Library — https://adapty.io/paywall-library/duolingo/

[22] Duolingo Pushy Paywall (Motley Fool) — https://www.fool.com/investing/2025/08/08/duolingos-pushy-paywall-play-smart-or-risky/

[23] Noom Lean Web2App (Paddle) — https://www.paddle.com/studios/shows/fix-that-funnel/noom

[24] Noom long onboarding analysis (Retention.blog) — https://www.retention.blog/p/the-longest-onboarding-ever

[25] Noom via ScreensDesign — https://screensdesign.com/showcase/noom-weight-loss-food-tracker

[26] Cal AI via ScreensDesign — https://screensdesign.com/showcase/cal-ai-calorie-tracker

[27] Cal AI via Adapty Library — https://adapty.io/paywall-library/cal-ai-food-calorie-tracker/

[28] Cal AI via Adapty Newsletter #22 — https://adapty.io/blog/paywall-newsletter-22/

[29] Tinder Gold conversion (StartupSpells) — https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux

[30] Tinder Dynamic Paywalls (Sub Club Podcast) — https://subclub.com/episode/dynamic-paywalls-that-drove-millions-in-new-revenue-shawn-gong-tinder

[31] Strava Year in Sport paywall — https://gadgetsandwearables.com/2025/12/20/strava-year-in-sport/

[32] Top Fitness App Paywalls — https://dev.to/paywallpro/top-fitness-app-paywalls-ux-patterns-pricing-insights-2868

[33] Headspace Sub Club Podcast — https://subclub.com/episode/how-headspace-optimized-revenue-by-gating-content-shreya-oswal-and-keya-patel-headspace

[34] Headspace via NamiML — https://www.namiml.com/paywalls/headspace-mindful-meditation

[35] How Top Apps Approach Paywalls (RevenueCat) — https://www.revenuecat.com/blog/growth/how-top-apps-approach-paywalls/

[36] Blinkist via Purchasely — https://www.purchasely.com/blog/blinkist-paywall-transformation-revolutionizes-app-user-engagement

[37] Blinkist Growth.Design Case Study — https://growth.design/case-studies/trial-paywall-challenge

[38] Blinkist Funnel Teardown — https://www.funnelteardowns.net/teardown/blinkist

[39] Blinkist 1,200% notif opt-in — https://b2bpricinginsights.substack.com/p/4-min-read-how-blinkists-new-paywall

[40] Flo via ScreensDesign — https://screensdesign.com/showcase/flo-period-pregnancy-tracker

[41] Effective H&F paywall examples — https://dev.to/paywallpro/effective-paywall-examples-in-health-fitness-apps-2025-3op9

[42] OpenAI ChatGPT pricing — https://openai.com/business/chatgpt-pricing/

[43] OpenAI Pricing Guide 2026 — https://www.getaiperks.com/en/articles/openai-pricing

[44] Cialdini 7 Principles 2026 — https://www.cognitigence.com/blog/cialdini-7-principles-of-persuasion

[45] Cialdini persuasion mobile app study (Springer) — https://link.springer.com/chapter/10.1007/978-3-031-59465-6_17

[46] Decoy Effect (Wikipedia summary, references academic) — https://en.wikipedia.org/wiki/Decoy_effect

[47] Psychological Pricing (Wikipedia, references Anderson-Simester, Thomas-Morwitz) — https://en.wikipedia.org/wiki/Psychological_pricing

[48] Subscription Trends Benchmarks 2026 (RC) — https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026/

[49] Funnel Fox H&F paywall examples — https://blog.funnelfox.com/effective-paywall-screen-designs-mobile-apps/

[50] Paywallscreens.com library — https://www.paywallscreens.com/

---

## Provenance

**Sources consulted:** 60+ searches and fetches.
**Sources accepted:** 50 (all listed above).
**Sources rejected:** undated SEO listicles, AI-generated content without primary backing, single-Quora answers without verifiable basis.
**Cross-references made:** Adapty + RC (5 metrics overlap and agree within ±2pp); Superwall (only vendor with disclosed methodology for paywall structure tests); RevenueFlo + Adapty + RC for toggle paywall (3 independent confirmations).
**Weak signals flagged:** Apphud (no methodology disclosure), animated paywall claim, decoy effect mobile applicability.
