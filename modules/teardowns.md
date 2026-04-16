# Big-App Paywall Teardowns

Annotated breakdowns of high-revenue subscription apps. Each: structure, copy patterns, pricing, key takeaway, source. Use as design reference, not as copy-paste blueprint — every app's audience is different.

All patterns observed via independent operator analyses, paywall screenshot libraries, and case-study disclosures. Marked by Evidence Class.

---

## 1. Calm

**Category:** Health & Fitness / Mindfulness
**Revenue scale:** ~$100M+/year
**Sources:** [Kristen Berman analysis](https://kristenberman.substack.com/p/how-calm-uses-premium-to-motivate), [Adapty Library](https://adapty.io/paywall-library/calm/), [ScreensDesign](https://screensdesign.com/showcase/calm)
**Evidence Class:** operator + screenshot reference

### Structure
- **Single subscription plan** (annual) — eliminates choice paralysis
- Dark gradient hero; benefits list pops via contrast
- 7-day free trial framed transparently
- Family plan upsell visible (£40.99/year for 6 accounts)

### Copy
- Headline: outcome-led, calm voice
- Benefits: 3–4 bullets, sleep/anxiety/focus
- CTA: "Try Calm Premium Free"
- Trust line: "7-day free trial, then $X. Cancel anytime."

### Pricing pattern
- Annual price as anchor ($69.99/year)
- Per-month breakdown subordinate ("$5.83/month")
- Strikethrough monthly price for visual contrast

### Key takeaway
**Single-plan paywalls work when the value is universal** (meditation = same for everyone). When you don't have meaningful tier differentiation, don't fake it — one plan + Family upsell is cleaner than 3 weak tiers.

### Apple compliance notes
✅ Trial terms clear, billed amount prominent, Restore + Terms + Privacy present.

---

## 2. Duolingo

**Category:** Education / Language Learning
**Revenue scale:** ~$25M+/month subscription revenue
**Sources:** [Adapty Library](https://adapty.io/paywall-library/duolingo/), [Motley Fool 2025 analysis](https://www.fool.com/investing/2025/08/08/duolingos-pushy-paywall-play-smart-or-risky/), [paywallscreens.com](https://www.paywallscreens.com/apps/duolingo-mobile-paywall-4820)
**Evidence Class:** operator + screenshot reference

### Structure
- Brand-consistent design (signature green gradient, mascot)
- Two plans: Family vs Individual (NOT trial vs no-trial)
- 7-day free trial
- Multiple paywall touchpoints in single new-user session (~7+ surfaces)

### Copy
- Personalized first benefit bullet based on entry placement
- CTA: **"Start my free week"** — possessive ("my") + action verb + outcome
- Decline: "Maybe later"

### Pricing pattern
- Family plan default (Cialdini: social/unity lever)
- Individual fallback
- Annual default to anchor

### Key takeaway
**Brand consistency at paywall raises trust.** Same colors, mascot, voice as the rest of the app = paywall doesn't feel like a stranger walked in. CTA pattern "Start my free week" outperforms "Subscribe" because it activates ownership.

### Weakness
Doesn't always explain what "Super" includes (no offline / ad-removal call-out on every variant). Test variant: explicit feature list might lift conversion for users who don't know.

### Apple compliance notes
✅ Compliant. Aggressive frequency (7+ paywalls/session) has not triggered rejections to date.

---

## 3. Noom

**Category:** Health & Fitness / Weight Loss
**Revenue scale:** Public mid-stage company, $400M+ ARR
**Sources:** [Paddle Fix That Funnel](https://www.paddle.com/studios/shows/fix-that-funnel/noom), [Retention.blog longest onboarding](https://www.retention.blog/p/the-longest-onboarding-ever), [ScreensDesign](https://screensdesign.com/showcase/noom-weight-loss-food-tracker)
**Evidence Class:** operator + case study

### Structure
- **77-step onboarding quiz** (~7 min) before paywall
- "Personalized plan reserved" intermediate screen
- Local currency via geo-IP detection
- 15-min countdown timer for "your reserved plan"
- 7-day free trial on **2-month plan** (unusual — trial NOT on annual)

### Copy
- Heavy use of "your" possessive throughout
- Outcome-led headlines ("You'll lose 0.5lb/week")
- Empathy + identity ("Built for people like you")
- Loading screen: "Analyzing your preferences, building your plan…"

### Pricing pattern
- $17.42/month equivalent for 12-month plan
- 2-month plan as primary (trial-on-2mo is the unusual choice)
- Local currency from start

### Key takeaway
**Long onboarding = effort investment that primes commitment** (Cialdini commitment + consistency). By the time user reaches paywall, they've invested 7 minutes. Plus geo-currency = instant trust signal.

### Caution
15-min countdown timer is fake-urgency adjacent — verify it actually expires (Apple Rule on misleading marketing). If timer resets every visit, it's a violation.

### Apple compliance notes
⚠️ Countdown timer must be real. Otherwise compliant.

---

## 4. Cal AI

**Category:** AI / Calorie Tracking
**Revenue scale:** ~$1.4M/month gross profit (CNBC, 2025), 30M+ downloads
**Sources:** [ScreensDesign](https://screensdesign.com/showcase/cal-ai-calorie-tracker), [Adapty Library](https://adapty.io/paywall-library/cal-ai-food-calorie-tracker/), [Adapty Newsletter #22](https://adapty.io/blog/paywall-newsletter-22/)
**Evidence Class:** operator + media coverage

### Structure
- **Hard paywall**: card required before app use
- Demo video at onboarding start
- Deep personalization throughout (animations, interactions)
- Mid-onboarding review prompt
- Personalized plan generation
- Annual heavily pushed via "75% off" framing

### Copy
- Outcome: "Track calories with one photo"
- Benefits: AI-driven, time-to-value emphasized
- CTA: action-led

### Pricing pattern
- Range $2.99/week to $29.99/year
- "75% off" anchor on annual
- Weekly fallback for low-intent

### Key takeaway
**Hard paywall + obsessive personalization + single core action = repeatable AI-app formula.** Built by 2 teenagers — proof that execution beats resources.

### Caution
"75% off" requires legitimate reference price (Apple Rule). If the "regular" price is fictional, it's a violation. Verify the annual at $29.99 is genuinely a discount from a higher reference.

### Apple compliance notes
⚠️ Verify reference pricing for "75% off" claim.

---

## 5. Tinder

**Category:** Dating
**Revenue scale:** ~$2B+/year (Match Group)
**Sources:** [StartupSpells Tinder Gold](https://startupspells.com/p/tinder-gold-conversion-strategy-blur-to-reveal-paywall-ux), [Sub Club Podcast Tinder Dynamic](https://subclub.com/episode/dynamic-paywalls-that-drove-millions-in-new-revenue-shawn-gong-tinder)
**Evidence Class:** operator + podcast disclosure

### Structure
- **Curiosity-driven blur-to-reveal**: blurred matches → "Who liked you?" → paywall
- ~8% upgrade conversion specifically to unblur
- ML-driven dynamic paywall: predicts best product per user, surfaces only that one
- A la carte fallback if user rejects subscription
- Tier ladder: Plus → Gold → Platinum

### Copy
- Curiosity hooks ("Someone liked you")
- Tier-specific benefit lists
- Outcome-led ("Get more matches")

### Pricing pattern
- 7-day Passport priced equal to 7-day Plus → makes Plus look better value (decoy effect, Ariely)
- Subscription first, a la carte second (revenue maximization)
- Geo-priced

### Key takeaway
**Zeigarnik effect (incomplete-task tension)** as deliberate paywall trigger. Tinder doesn't sell features — it sells the **release** of curiosity it created. Plus: dynamic paywall = personalization at choice level, not just copy.

### Apple compliance notes
✅ Compliant. ML-driven personalization is allowed.

---

## 6. Strava

**Category:** Health & Fitness / Running & Cycling
**Revenue scale:** Mid-stage public-adjacent
**Sources:** [Year in Sport paywall](https://gadgetsandwearables.com/2025/12/20/strava-year-in-sport/), [Top Fitness Paywalls](https://dev.to/paywallpro/top-fitness-app-paywalls-ux-patterns-pricing-insights-2868)
**Evidence Class:** operator + press

### Structure
- Slow gradual paywalling of features (2024–2026 trend)
- Year in Sport now subscriber-only ($80/year)
- **30-day full-access trial without credit card** (very unusual — ultimate trust signal)
- Inline subscription CTAs in main UI (not modal interruption)
- Contextual feature gates per locked feature

### Copy
- Athlete identity-led ("Train smarter")
- Outcome bullets (route planning, segment analysis)
- Authority via partnership (Garmin, etc.)

### Pricing pattern
- Monthly $11.99 vs annual $79.99 = $144 anchor, makes annual a clear bargain
- Single annual price globally (limited geo-pricing)

### Key takeaway
**No-CC trial = ultimate trust signal.** Most apps fear free trials without payment because it lowers conversion to paid; Strava's data suggests for high-engagement-required products (training), the lift in trial starts compensates.

### Caution
**Aggressive paywalling of historically-free features risks brand backlash** (2025 Year in Sport caused major Reddit/Twitter pushback). Only paywall a previously-free feature when value is clearly post-aha and you can withstand the PR cycle.

### Apple compliance notes
✅ Compliant.

---

## 7. Headspace

**Category:** Health & Fitness / Mindfulness
**Revenue scale:** ~$120M+/year
**Sources:** [Sub Club Podcast](https://subclub.com/episode/how-headspace-optimized-revenue-by-gating-content-shreya-oswal-and-keya-patel-headspace), [NamiML](https://www.namiml.com/paywalls/headspace-mindful-meditation), [RevenueCat top apps](https://www.revenuecat.com/blog/growth/how-top-apps-approach-paywalls/)
**Evidence Class:** operator + podcast disclosure

### Structure
- Day/night theme adaptive paywall (auto-switches by time)
- 100% locked content library after free preview
- Kept 1–2 free items per category (retention hook)
- Monthly + annual equal prominence (intentional)
- Segmented messaging by user interest (sleep / stress / focus)

### Copy
- Headline: "Cancel anytime. No commitment." (transparency-led)
- Segment-specific benefits per quiz answer
- Minimalist — short sentences

### Pricing pattern
- $12.99/month, $69.99/year
- Equal-prominence plans (NOT annual-first)

### Key takeaway
**Equal-prominence plans are sometimes optimal** — annual default is not universal best practice. Headspace's data: monthly subscribers stay loyal because they "pay attention" each month, contributing to brand engagement.

### Plus
Day/night theming = lightweight personalization with measurable lift. Easy to implement — single conditional based on `hour of day`.

### Apple compliance notes
✅ Compliant.

---

## 8. Blinkist

**Category:** Education / Books
**Revenue scale:** ~$30M+/year (mid-2020s)
**Sources:** [Purchasely case study](https://www.purchasely.com/blog/blinkist-paywall-transformation-revolutionizes-app-user-engagement), [Growth.Design](https://growth.design/case-studies/trial-paywall-challenge), [Funnel Teardowns](https://www.funnelteardowns.net/teardown/blinkist), [B2B Pricing Insights](https://b2bpricinginsights.substack.com/p/4-min-read-how-blinkists-new-paywall)
**Evidence Class:** **case_study** (single company, methodology disclosed)

### Structure
- **"Free Trial Timeline" paywall** — visual: Today → Day 5 reminder → Day 7 charge
- Driver for change: exit survey said users didn't subscribe because they didn't know when they'd be charged
- 7-day free trial standard

### Copy
- Timeline labels: "Today: Get full access" / "Day 5: We'll remind you" / "Day 7: Trial ends, billing begins"
- Outcome bullets focused on time saved ("Read 1,000 books in 15 min summaries")

### Pricing pattern
- Single annual prominent
- Per-day breakdown subordinate

### Disclosed results
- **+23% trial signups**
- **−55% customer complaints**
- **+4% trial retention**
- **+1,200% notification opt-in (6% → 74%)**

### Key takeaway
**Transparency converts.** Visual timeline beats text disclosure of trial terms. Standardized as "STEPS" template in Purchasely. **The single most-cited trial-anxiety solution in the industry.**

### Apple compliance notes
✅ Compliant — actually exceeds Apple's transparency requirements.

---

## 9. Flo

**Category:** Health & Fitness / Period Tracking
**Revenue scale:** ~$6M/month subscription revenue (~$72M ARR)
**Sources:** [ScreensDesign](https://screensdesign.com/showcase/flo-period-pregnancy-tracker), [H&F paywall examples](https://dev.to/paywallpro/effective-paywall-examples-in-health-fitness-apps-2025-3op9)
**Evidence Class:** operator + screenshot reference

### Structure
- 70-screen onboarding (~7 min)
- Personalization via name + empathy ("you're not alone")
- 14-day free trial (longer than category norm)
- Yearly default; monthly + family on scroll
- Core cycle tracking remains free (preserves brand trust)

### Copy
- Personalized greeting using user's name
- Empathy framing ("you're not alone")
- Outcome bullets focused on insights, predictions, AI assistant

### Pricing pattern
- $49.99/year Premium
- Family option in scroll
- 60–80% of purchases at first app use

### Key takeaway
**Long onboarding consistently appears in highest-revenue H&F apps.** Free core + premium tier = trust + monetization balance.

### Caution
Reported design uses a toggle for the 14-day trial. **Toggle paywalls are subject to Apple rejections since Jan 2026** (Guideline 3.1.2). If shipping a Flo-style paywall today, replace the toggle with a separate plan card or trial-on-annual-only structure.

### Apple compliance notes
⚠️ Toggle pattern at risk — verify current production version.

---

## 10. ChatGPT (OpenAI)

**Category:** AI / Productivity
**Revenue scale:** $X+B (private)
**Sources:** [OpenAI pricing](https://openai.com/business/chatgpt-pricing/), [GetAIPerks 2026 guide](https://www.getaiperks.com/en/articles/openai-pricing)
**Evidence Class:** apple_docs / OpenAI public pricing

### Structure
- 6 tiers: Free, Go ($8), Plus ($20), Business, Enterprise, Edu
- Geo-tier (Go) launched India first then global expansion
- Plus is the consumer mass-market tier
- Enterprise = sales-led

### Copy
- Tier names communicate scope (Free / Go / Plus / Business / Enterprise)
- Plus benefits: priority access, GPT-5.3, image gen, deep research
- Minimalist — feature-led for technical audience

### Pricing pattern
- $20/mo became the AI consumer baseline
- $8/mo geo-tier for emerging markets
- Annual discount available

### Key takeaway
**ChatGPT made $20/mo the AI baseline.** Other AI apps inherit this ceiling whether they like it or not. Pricing above $20 requires demonstrably more value (Adapty 2026: 59.8% of AI apps use monthly billing — short purchase cycle, high price tolerance).

**Geo-tier pricing for emerging markets** (Go @ $8) = increasingly important pattern. Adapty 2026 H&F data: 4.4x pricing variance across markets. EU/US/AU at top, IN/TR/ID at bottom.

### Apple compliance notes
✅ Compliant.

---

## 11. AI Companion Pattern (Replika, Character.AI, etc.)

**Category:** AI / Companion / Entertainment
**Sources:** RevenueCat AI category data (large_scale_report), Adapty AI section
**Evidence Class:** vendor_aggregate

### Common structure
- Hard paywall on advanced relationship features
- Voice/video unlocked via Pro
- Often weekly + monthly + annual ladder
- Higher price tolerance than non-AI ($15–25/mo norm)

### Aggregate data
- AI churns ~30% faster than category average (RevenueCat 2026)
- 59.8% of AI apps use monthly billing as primary plan
- Higher absolute pricing tolerated

### Key takeaway
**AI = high price tolerance + high churn.** Optimize for first-month conversion, not long retention. Annual + trial is the LTV anchor. Test reverse trial for low-intent users.

---

## Cross-App Patterns

### What top apps share

1. **Personalization signal at paywall** — name, location, plan reserved for "you"
2. **Outcome-led headline** — never "Premium Features"
3. **Clear trust block** — trial terms, billed amount, restore, terms, privacy
4. **Real social proof** — never inflated user counts
5. **Annual-first defaults** — except Headspace (deliberate equal prominence)
6. **Single-screen layout** without forced scroll for primary CTA
7. **Transparent decline** — "Maybe later", not guilt copy

### What they avoid

- Toggle paywalls (post Jan 2026)
- Delayed close buttons (>5s)
- Pricing fonts <16pt
- Multiple full paywalls back-to-back
- Fake urgency / countdown not tied to real expiry
- Generic CTAs ("Subscribe", "Buy")

---

## Source Library

Use these for ongoing pattern research:

| Library | URL | What |
|---------|-----|------|
| Adapty Paywall Library | https://adapty.io/paywall-library/ | 100+ apps, screenshots + commentary |
| Mobbin | https://mobbin.com | UX teardowns including paywalls |
| ScreensDesign | https://screensdesign.com | Curated app screen library |
| Paywallscreens.com | https://www.paywallscreens.com | 10K+ paywall screenshots indexed |
| NamiML | https://www.namiml.com/paywalls/ | Operator-level commentary |
| Growth.Design | https://growth.design/case-studies/ | Case studies with annotations |
| Funnel Teardowns | https://www.funnelteardowns.net | Onboarding + paywall flow analysis |

Refresh quarterly — top apps iterate paywalls every 6–8 weeks on average (Adapty 2026 vendor_blog).
