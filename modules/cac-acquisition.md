# CAC & Acquisition Economics

Customer Acquisition Cost is half the unit economics equation. Most paywall optimization fails because the LTV side gets fixed but CAC stays broken (or vice versa). This module covers CAC measurement, channel benchmarks, and LTV:CAC math.

For LTV projection, see [unit-economics-calculator.md](unit-economics-calculator.md). For per-category benchmarks, see [category-deep-dives.md](category-deep-dives.md).

---

## CAC Formula

```
CAC = Total Marketing & Sales Spend / Number of New Customers Acquired
```

### Variants by what you measure

| Metric | Formula | When to use |
|--------|---------|-------------|
| **CPI** (Cost Per Install) | Spend / Installs | Top-of-funnel measurement |
| **CPR** (Cost Per Registration) | Spend / Registrations | When signup is gated |
| **CAC for paying customer** | Spend / Paying customers | Unit economics decision-making |
| **eCAC** (effective) | Spend / (Installs × CR_to_paid) | Forward projection |

**Most indie devs misuse "CAC" by reporting CPI.** Always specify which CAC you mean.

---

## Mobile App CAC Benchmarks (2026)

Source: AppsFlyer 2026 + Adapty CAC guide. Costs vary by region, network, category — these are central tendencies.

### iOS (premium markets — US, UK, DE, JP, AU)

| Target | Median CPI | Range |
|--------|-----------|-------|
| App install | $2.50 | $1.50–$5.00 |
| Registration | $7.55 | $4–$15 |
| First in-app purchase | $77.45 | $40–$200+ |
| Trial start | $20–$30 | $10–$50 |

### Android (premium markets)

| Target | Median CPI | Range |
|--------|-----------|-------|
| App install | $1.50 | $0.80–$3.00 |
| Registration | $2.17 | $1–$5 |
| First in-app purchase | $86.72 | $40–$250+ |

### Emerging markets (IN, SEA, LATAM)

| Target | Median CPI iOS | Median CPI Android |
|--------|---------------|-------------------|
| App install | $0.80–$1.50 | $0.30–$0.80 |

**AppsFlyer 2026:** Indian Subcontinent = 49% of net Android paid install growth, LATAM = 18%. Cheap CPIs but lower RLTV per payer ($14 vs NA $32). Math still works only with high volume + low payment friction.

---

## Channel CPI Benchmarks (iOS, US/EU)

Approximate central CPIs by channel. Real cost varies by category, creative quality, audience.

| Channel | Typical CPI | Notes |
|---------|------------|-------|
| Apple Search Ads (branded) | $0.50–$2 | Cheapest, intent-rich |
| Apple Search Ads (category) | $2–$5 | Discovery |
| Meta (Facebook + Instagram) | $2–$8 | Broad reach, creative-dependent |
| TikTok | $1.50–$6 | Younger demo, viral creative |
| Google App Campaigns | $2–$6 | Cross-channel |
| Snapchat | $2–$5 | Younger, ephemeral |
| Reddit | $3–$10 | Niche communities |
| Twitter/X | $3–$8 | Lower scale, declining |
| Influencer (per install equivalent) | $2–$15 | Wildly variable |
| ASA (broad keywords) | $5–$15 | Discovery + branding |

### What the 2026 data says

- **ASA users have higher trial start rate** than paid social (Adapty/RC field reports). Intent matters more than volume.
- **TikTok creative shelf life** is 7-14 days vs Meta 30-60. TikTok needs constant creative refresh.
- **Top 5 apps per category control >90% of UA spend** (AppsFlyer 2026) — competitive auctions are crushed.

---

## LTV:CAC Ratio

The single most important unit-economics metric for indie devs.

```
LTV:CAC = LTV (12-mo or 4yr, your choice) / CAC for paying customer
```

### Thresholds

| Ratio | Verdict | Action |
|-------|---------|--------|
| > 5:1 | **Strong** — likely underinvesting in growth | Increase UA spend; you can afford higher CPI |
| 3:1 – 5:1 | **Healthy** — sustainable economics | Maintain; iterate on margin |
| 2:1 – 3:1 | **Marginal** — optimize before scaling | Fix retention, plan mix, or pricing |
| < 2:1 | **Unprofitable** — fix before paid UA | Stop spending, fix LTV side first |

### Quick math rule

12-month LTV ÷ 2 = max sustainable CAC at 3:1 ratio.

Example: ARPU 12mo = $40 → max CAC = $20 → at 6% CR, max CPI = $1.20.

---

## Diagnosing CAC Problems

### High CAC

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| CPI rising in same channel | Saturation OR creative fatigue | Refresh creative, expand to adjacent channels |
| CPI fine but CAC bad | Low CR | Fix paywall (see SKILL.md DEFAULT OUTPUT FORMAT) |
| One channel disproportionately expensive | Wrong audience targeting | Audit interest/behavior targets |
| LTV:CAC < 2:1 | UA outspending what app earns | Cut spend until unit economics work |

### Low CAC but slow growth

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Cheap channels exhausted | Limited audience reach | Expand to higher-CPI channels you can now afford |
| Organic dominates | Underinvesting in paid | Test paid scale at LTV:CAC > 5:1 |
| Single market | Geographic constraint | Expand to high-LTV markets (see [localization.md](localization.md)) |

---

## Channel Mix Strategy by Stage

### Pre-product-market-fit (PMF)
- 100% organic + ASA branded only
- CPI doesn't matter; you're learning, not scaling
- LTV unstable, can't compute LTV:CAC reliably

### Post-PMF, sub-$10K MRR
- Add ASA category keywords + small Meta tests
- Focus on cohort cleanliness (one channel = one cohort to analyze)
- Track LTV:CAC per channel

### $10K–$100K MRR
- Diversify: ASA + Meta + TikTok + Google
- 70/20/10 rule: 70% in proven channel, 20% in scaling channel, 10% in experimental
- Set CPI ceiling per channel based on LTV:CAC math

### $100K+ MRR
- All major channels active
- Custom audiences, lookalikes, retargeting
- Brand spend supplements performance

---

## Adjust / AppsFlyer / Singular: Attribution Choice

You need an MMP (mobile measurement partner) once you spend on >1 channel. Without it, you're flying blind.

| MMP | Pricing | Best for |
|-----|---------|----------|
| AppsFlyer | Free up to 12K NLOAS, then volume-based | Most indie devs, large dataset (1.7B installs in their 2026 report) |
| Adjust | Volume-based | Privacy-conscious, EU-heavy |
| Singular | Volume-based | Best UA reporting + creative analytics |
| RevenueCat (built-in) | Free | If RC is your subscription SDK already; basic attribution only |

### iOS attribution post-ATT

ATT (App Tracking Transparency, iOS 14.5+) means probabilistic attribution dominates. SKAdNetwork (SKAN) gives you deterministic install attribution but limited postback granularity. Don't expect 1:1 channel cleanliness.

### Google Play Install Referrer

Android keeps deterministic attribution. Easier to measure CPI by channel.

---

## Apple Search Ads Specifics

Often the highest-leverage channel for indie subscription apps.

### Why ASA wins for indie

- **Intent-rich** — users searching "calorie tracker" are pre-qualified
- **Lower CPI than paid social** for branded + category terms
- **Higher trial start rate** than paid social (field reports)
- **No creative production cost** (uses your App Store metadata)

### ASA campaign types

| Type | CPI | Use |
|------|-----|-----|
| Discovery (Apple suggests keywords) | $1–$3 | Find new keywords |
| Brand defense | $0.50–$2 | Keep competitors off your brand search |
| Category | $2–$5 | "Calorie tracker", "meditation app" |
| Competitor | $3–$10 | "MyFitnessPal alternative" — ethics check first |

### ASA optimization pattern
1. Start with Discovery to learn keywords
2. Move winners to Search Match campaigns with bids
3. Defend brand keywords always
4. Move to Custom Product Pages (iOS 15+) for top keywords — different App Store screenshots per ad group

---

## Web2App Strategy (Bypassing 30%)

Acquire users via web, monetize via web checkout. Pre Epic-Apple ruling (May 2025) this was Android-only; now iOS US-only too.

### Math

- Apple cut: 30% → you keep 70%
- Web checkout: 0% Apple cut, but +5% payment processing → keep 95%
- Conversion penalty: web typically 30-50% lower than in-app
- Net: works if your web-to-app channel can handle the conversion penalty

### Reported lifts

Some indie devs report **65-120% revenue increases** by adding web checkout (Apphud, Paddle case studies). Best for:
- Strong content marketing / SEO presence (Headspace, Calm, Noom)
- Existing brand awareness
- High-intent audience (knows what they're buying)

### Cost

- Engineering: medium (need web checkout, handle entitlement sync)
- Compliance: must disclose external purchase (post Epic ruling requirement)
- Attribution: messy (web channel → app activation)

---

## Common CAC Mistakes

| Mistake | Why it hurts |
|---------|------------|
| Using blended CAC instead of per-channel | Hides channel mix problems |
| Comparing CAC to gross LTV (not net) | Forgets Apple/Play 15-30% cut |
| Not factoring trial subsidization in CAC | A trial user costs the same to acquire but earns less |
| Optimizing for CPI not CAC | Cheap installs from wrong audience = wasted spend |
| Setting CPI ceiling without LTV:CAC math | Arbitrary; may underprice or overpay |
| Not refreshing creative quarterly | CTR decay → CPI rising → CAC rising |
| Ignoring SKAdNetwork postback delays | iOS attribution lag = 2-3 days; don't optimize hourly |

---

## When CAC Doesn't Apply

- **Pre-launch / soft launch** — you're not optimizing CAC, you're learning. Run small geo tests.
- **Sub-100 paying users** — CAC is noise. Focus on activation and retention.
- **Pure organic / viral apps** — CAC = $0 effectively. Optimize K-factor and ASO instead.
- **B2B / enterprise** — CAC measurement is per-seat or per-contract; very different math.

---

## Source Pointers

- AppsFlyer State of Subscriptions 2026: https://www.appsflyer.com/resources/reports/subscription-marketing/
- AppsFlyer benchmarks: https://www.appsflyer.com/benchmarks/
- Adapty CAC Guide: https://adapty.io/blog/customer-acquisition-cost/
- Adapty ARPU Guide: https://adapty.io/blog/average-revenue-per-unit-arpu/
- Adapty LTV Guide: https://adapty.io/blog/customer-lifetime-value-ltv/
- Apple Search Ads: https://searchads.apple.com/
- Apple SKAdNetwork: https://developer.apple.com/documentation/storekit/skadnetwork
- Apple Small Business Program: https://developer.apple.com/app-store/small-business-program/
