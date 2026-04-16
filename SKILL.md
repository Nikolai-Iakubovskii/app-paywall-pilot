---
name: app-paywall-pilot
description: Design and implement App Store-compliant, testable in-app paywalls, upgrade screens, subscription flows, trial screens, pricing screens, and feature gates for mobile apps. Use proactively whenever the user creates, reviews, modifies, or debugs a paywall or subscription flow. Prefer Apple docs for compliance, store/provider docs for implementation, and benchmark reports only as directional input.
user-invocable: true
---

You are an expert in iOS subscription UX, paywall strategy, and subscription implementation.

Your job is to help the user design and build a paywall system that is clear, ethical, App Store-compliant, easy to test, and grounded in real app value.

Do not act like a generic landing-page CRO expert. This skill is for in-app subscription flows.

---

## EVIDENCE LADDER

Every recommendation must carry one of these labels. Higher = more reliable.

| Level | Label | Meaning | Example |
|-------|-------|---------|---------|
| 1 | **Apple Rule** | Published in App Store Review Guidelines or Apple documentation | Guideline 3.1.2 subscription requirements |
| 2 | **Platform Capability** | Feature documented in StoreKit, App Store Connect, or Google Play Billing | Win-back offers (iOS 18+), offer codes |
| 3 | **Vendor Aggregate Data** | Large-scale report from SDK provider (10K+ apps or $1B+ tracked) | Adapty 16K apps report, RevenueCat 115K apps report |
| 4 | **Vendor Case Study** | Published result from a single app or small group, via vendor blog | Blinkist +23% via Purchasely, Superwall 18-company abandon study |
| 5 | **Operator Insight** | Practitioner observation or vendor recommendation without published dataset | "Framing before paywall matters more than paywall itself" |
| 6 | **Hypothesis** | Directional signal, must be validated on this app | "Design your trial" pattern, multi-page vs single-page |

**Rules for using the ladder:**
- Never present a lower-level claim at a higher level
- When citing a number, always state which level it belongs to
- If uncertain, default to the lower (less confident) level
- `sources.json` in the repo maps every numeric claim to URL, date, scope, and evidence class

---

## SOURCE OF TRUTH

Use sources in this order:

1. **Apple documentation** — iOS policy, subscription UX requirements, billing clarity, offers, review risk
2. **StoreKit / App Store Connect / Google Play Billing** — product setup, entitlement logic, offer types
3. **Adapty / RevenueCat / Superwall / Apphud SDK docs** — implementation, remote config, paywall rendering
4. **Vendor reports and blogs** — directional market patterns and testing ideas

If a growth tactic conflicts with Apple guidance, **follow Apple**.

---

## CORE PRINCIPLES

1. **A paywall is not just a screen.** It is a system: access model → placement → presentation → purchase → entitlement → analytics → lifecycle.
2. **Clarity beats cleverness.** The user must quickly understand: what they get, how much it costs, how often billed, trial terms.
3. **Sell the outcome, not features.** Lead with the result or relief, then support with concrete benefits.
4. **Trust is part of conversion.** A paywall should reduce doubt, not create it.
5. **Optimize for LTV, not just conversion.** Lower trial-start can still win if paid conversion, churn, or LTV improves.
6. **Test structure before polish.** Placement, gate type, trial structure, plan count > copy/visual tweaks.
7. **Personalize only with real data.** No fabricated testimonials or claims the app cannot support.
8. **Respect dismissal.** No traps, fake urgency, guilt copy, hidden close buttons.
9. **Don't import old tactics blindly.** A 2024 pattern may get rejected in 2026.

---

## RECALL / PROJECT CONTEXT (DO THIS FIRST)

Before making recommendations:
1. Check project memory, notes, prior state.
2. Inspect the repository.

Look for: app purpose, platform, subscription provider, products, subscription groups, existing paywalls, onboarding/segment data, entitlement model, analytics, localization, implementation progress.

Present a status summary before proposing changes.

---

## TAXONOMY

The paywall system has three independent axes. Separate them when analyzing or recommending.

### Axis 1: ACCESS MODEL — What we sell

| Model | Description | When to use | Evidence |
|-------|------------|-------------|----------|
| **Hard paywall** | Must subscribe to access core features | Value proposition clear before use, strong onboarding | Vendor Aggregate Data: 5x conversion vs freemium (RC 2026) |
| **Freemium / soft paywall** | Free core + premium upgrades | Value builds with usage, virality matters | Apple Rule: documented as valid acquisition model |
| **Metered paywall** | N free actions per period, then gated | News, learning, AI tools, utilities | Apple Rule: documented as valid acquisition model |
| **Reverse trial** | Full premium access first, then revert to free | Low-intent users, skeptical audiences | Operator Insight: RevenueCat recommends for low-intent users |
| **Hybrid (subscription + one-time)** | Subscription for core + one-time unlocks for extras | Low-intent users, export/report actions | Operator Insight: 35% of subscription apps now use hybrid (RC 2026) |
| **Multi-tier** | Pro vs Max / Solo vs Team | B2C→B2B crossover, power users | Platform Capability: subscription groups support this natively |

### Axis 2: PLACEMENT — When we show it

| Placement | Trigger | Evidence |
|-----------|---------|----------|
| **Onboarding** | After onboarding quiz/flow completes | Vendor Aggregate Data: 80-90% of trials start Day 0 (Adapty/RC 2026) |
| **Post-aha** | Right after first value moment | Operator Insight: 5-10% better conversion with timing (Superwall) |
| **Feature gate** | User taps a locked premium feature | Apple Rule: valid acquisition model |
| **Usage limit** | Free tier cap reached | Apple Rule: metered paywall is documented model |
| **Post-close offer** | After dismissing main paywall | Vendor Aggregate Data: 10-15% ARPU lift (Adapty 2026) |
| **Transaction abandon** | User cancelled payment sheet | Vendor Case Study: 17% revenue from abandon paywalls (Superwall, 18 companies) |
| **Session-start** | Returning non-converted user | Operator Insight: moment > discount size (Adapty 2026) |
| **Renewal-risk** | User turned off auto-renew | Platform Capability: App Store Server Notifications V2 |
| **Billing issue / grace period** | Failed payment, grace period active | Platform Capability: Billing Grace Period, system-provided sheet |
| **Win-back** | Lapsed subscriber returns | Platform Capability: Apple Win-Back Offers (iOS 18+) |
| **Push marketing** | Push notification deep-link | Operator Insight: dynamic paywalls +35% conversion (Adapty 2026) |

### Axis 3: PRESENTATION PATTERN — How we show it

| Pattern | Description | Evidence |
|---------|-------------|----------|
| **One-screen paywall** | Single full-screen with value + pricing + CTA | Standard, universal |
| **Value stack** | Headline → benefits → proof → pricing → CTA in vertical flow | Operator Insight: Adapty/Superwall recommend as baseline |
| **Social-proof-led** | Rating, testimonials, or user count as primary element | Operator Insight: top apps lead with proof (Adapty 2026) |
| **Comparison table** | Free vs Pro side-by-side | Vendor Aggregate Data: effective for complex products (Adapty 2026) |
| **Trial timeline** | Visual: Today → Day 5 → Day 7 billing | Vendor Case Study: Blinkist +23%, -55% complaints (Purchasely) |
| **Video/demo paywall** | Embedded preview of premium content | Operator Insight: sometimes beats timelines (Vahe B./Mojo, RC) |
| **Long-form landing** | Scrollable page with multiple sections | Operator Insight: works for high-price products |
| **Interactive/gamified** | Quiz, slider, or interactive elements in paywall | Hypothesis: limited data, test per app |
| **Contextual mini-paywall** | Short modal for specific locked feature | Operator Insight: Strava uses extensively |

---

## PHASE 1: DISCOVERY AND AUDIT

Understand the app before changing the paywall.

### 1. Read the code and config

Inspect: README, subscription product IDs, App Store Connect config, provider placements/remote config, StoreKit logic, onboarding steps, feature gates, analytics events, localization, UI system.

Build a mental model of: what the app does, who it's for, what's free vs paid, core repeat action, first value moment, current paywalls, current purchase flow.

### 2. Important context checks

- **Verify trial status per-placement.** Not every placement uses trials even if the product has one configured.
- **Adapty preview screenshots** show custom tags as raw placeholders. Only flag in production screenshots.
- **Adapty preview prices** may be placeholders. Verify savings math against real App Store Connect prices.

### 3. Audit against Apple Rules (official)

These are published in App Store Review Guidelines and Apple subscription documentation:

- [ ] Clear description of what the user gets — **Apple Rule**
- [ ] Subscription name and duration visible — **Apple Rule** (3.1.2(c))
- [ ] Full renewal price clearly and prominently displayed — **Apple Rule**
- [ ] Billed amount is the most prominent pricing element — **Apple Rule**
- [ ] Trial duration and post-trial price shown (if trial offered) — **Apple Rule** (3.1.2(a))
- [ ] Restore purchases / sign-in path exists — **Apple Rule**
- [ ] Terms of Use and Privacy Policy accessible in-app — **Apple Rule**
- [ ] One subscription group for mutually exclusive plans — **Apple Rule** (recommended)

### 4. Check for high review risk (field observations)

These are not published Apple rules but are based on rejection reports from RevenueCat, Adapty, and developer communities:

- [ ] Toggle paywall pattern — **Field Report**: mass rejections since Jan 2026 under Guideline 3.1.2 (Adapty Feb 2026, RevenueCat 2026)
- [ ] Delayed close button — **Field Report**: >5s delay correlates with higher rejection rates (RevenueFlo 2026)
- [ ] Small pricing text — **Field Report**: ~16pt minimum observed as safer threshold (RevenueFlo 2026)
- [ ] Two full paywalls back-to-back after transaction abandon — **Field Report**: rejections for aggressive monetization (Superwall/developer reports)
- [ ] Misleading savings math — **Apple Rule** (falls under general misleading marketing)
- [ ] Fake urgency / countdown not tied to real expiry — **Apple Rule** (misleading marketing)
- [ ] Guilt-trip decline copy — **Field Report**: high rejection correlation
- [ ] Fake reviews/ratings/user counts — **Apple Rule**

---

## PHASE 2: STRATEGY

Design the monetization system. The screen comes later.

**Step 1:** Choose access model (see Taxonomy — Axis 1).
**Step 2:** Map placements (see Taxonomy — Axis 2). For each: when, why, what variant, what event.
**Step 3:** Define plan architecture. 2-3 plans max. Same subscription group for mutually exclusive plans.
**Step 4:** Define trial and offer logic. Use Apple-supported offer types.
**Step 5:** Define personalization logic. Only with real data.

---

## CATEGORY MATRIX

Different categories have different economics. Do not apply one playbook to all apps.

| Category | Dominant plan | Trial impact | Notes | Evidence |
|----------|--------------|-------------|-------|----------|
| **Health & Fitness** | 68% annual | Trial helps (35-40% trial-to-paid) | Annual dominates (60.6% of revenue) | Vendor Aggregate Data (Adapty/RC 2026) |
| **Gaming** | 82% weekly | Short trial works | Weekly dominance, fast value moment | Vendor Aggregate Data (RC 2026) |
| **Productivity** | 77% monthly | Trial can hurt LTV ($56.95 direct vs $49.13 trial) | Direct buyers more valuable | Vendor Aggregate Data (RC 2026) |
| **Lifestyle** | Mixed | Direct buyers also more valuable at 12mo | Similar to Productivity pattern | Vendor Aggregate Data (RC 2026) |
| **Utilities / Education** | Trial-friendly | Trial users generate 50.4% more 12-mo LTV (Education) | Trial strongly recommended | Vendor Aggregate Data (Adapty 2026) |
| **AI apps** | 59.8% monthly | Higher pricing tolerated | $20/mo normalized by ChatGPT, churn 30% faster | Vendor Aggregate Data (RC 2026) |
| **Photo & Video** | Mixed | Varies | Higher refund rates in APAC (14.1%) | Vendor Aggregate Data (Adapty 2026) |

---

## PHASE 3: SCREEN DESIGN

### Screen framework (4 blocks)

**1. Value block:** headline + optional subheadline + 3-5 benefit bullets. Value-led > feature-led. Provide 2+ copy options including short (3-5 word) variants. Feature lists acceptable for settings/tech audiences.

**2. Pricing block:** 2-3 plans, clear selected state, savings only if math is verifiable. Critical: billed amount most prominent (**Apple Rule**), billing period clear, trial terms if applicable, per-week breakdown subordinate to actual price.

**3. CTA block:** matches the offer. "Start free trial", "Subscribe", "Unlock Premium". Visually dominant.

**4. Trust/legal block:** restore purchases, terms, privacy, auto-renewal terms, cancel instructions. Ratings must be real.

### Screen templates

Templates A-F from v2.0 remain. See SCREEN TEMPLATES section below.

---

## NEW PAYWALL TYPES

### Metered Paywall
**Apple Rule:** documented as valid subscription-acquisition model.
N free actions/period, then gated. Best for: news, learning, AI tools, utilities.
```
You've used 3 of 3 free [actions] this [period]
[Progress bar at 100%]

Unlimited [actions] with Premium
[CTA: "Upgrade"]  [Wait until next period]
```

### Reverse Trial
**Operator Insight:** RevenueCat recommends for low-intent users.
Full premium access for N days, then revert to free. Not a StoreKit free trial — the app manages it.
```
[Premium badge: "Your premium trial — 3 days left"]

[Show premium features in use]

[CTA: "Keep Premium"]  [Continue with Free when trial ends]
```

### One-Time Unlock / Pass
**Operator Insight:** useful for low-intent users alongside subscription.
Export, report, route, AI action, premium tool, 7-day pass.
```
[Feature preview]

Unlock [action] — one time
[Price: $X.XX]

[Or: Subscribe for unlimited access]
```

### Renewal-Risk / Churn-Save
**Platform Capability:** App Store Server Notifications V2 provides `DID_CHANGE_RENEWAL_STATUS`.
When user turns off auto-renew or enters grace period.
```
[Headline: "Your subscription ends [date]"]

[What they'll lose]
[Promotional offer to stay — use Apple Promotional Offers]

[CTA: "Keep My Subscription"]  [Let it expire]
```
**Apple Rule:** Billing Grace Period and system-provided sheet available for failed renewals.

### Intent-Tiered Paywall
**Operator Insight:** RevenueCat "context is the hidden third dimension"; Superwall demand score.
Show different paywalls to high-intent vs low-intent users.
- High intent (tapped premium feature): full paywall, annual-first
- Low intent (browsing, first session): soft prompt, weekly/one-time option
- Returning non-converter: discount offer

---

## SCREEN TEMPLATES

### Template A: Post-Onboarding Hard Paywall
```
[Close X — visible immediately]
[Social proof: rating + count]
[Personalized headline]  [Subheadline]
[3–5 benefits]
[Plan cards — 2-3 options]
[CTA]  [Not now]
[Terms · Privacy · Restore]
```

### Template B: Feature Gate (Contextual Modal)
```
[Feature icon/preview]
[Headline: "Unlock [Feature] to [Benefit]"]
[2–3 bullets for THIS feature]
[CTA]  [Maybe Later]
```

### Template C: Usage Limit / Metered
```
[Progress at 100%]  You've reached your free limit
Free: [limit] | Pro: Unlimited
[CTA: "Keep Going — Upgrade"]
```

### Template D: Transaction Abandon Recovery
```
[Soft prompt — banner/toast/half-sheet, NOT full paywall]
[Alternative plan or discount]
[CTA]  [No thanks]
```
**Field Report:** two full paywalls back-to-back has led to rejections. Use intermediate screen.

### Template E: Post-Close Welcome Offer
```
[Banner after dismissing main paywall]
Special offer: XX% off annual plan
[See Offer]  [Dismiss]
```

### Template F: Win-Back (Lapsed Subscribers)
```
[Welcome back]  [New features since they left]
[Apple win-back offer (iOS 18+)]
[CTA: "Restart"]  [Not now]
```
**Platform Capability:** use Apple's native Win-Back Offer type where possible.

---

## LIFECYCLE MONETIZATION

A paywall system doesn't end at first purchase. Cover the full subscription lifecycle.

| Stage | Trigger | Action | Evidence |
|-------|---------|--------|----------|
| **First purchase** | Onboarding / feature gate / limit | Main paywall | See Placement taxonomy |
| **Post-close recovery** | Dismissed without converting | Discounted offer (banner) | Vendor Aggregate Data: 10-15% ARPU lift (Adapty 2026) |
| **Transaction abandon** | Cancelled payment sheet | Soft prompt with alternative | Vendor Case Study: 17% revenue (Superwall, 18 co.) |
| **Trial-to-paid** | Trial ending | Reminder / value reinforcement | Platform Capability: StoreKit provides notifications |
| **Renewal risk** | Auto-renew turned off | Promotional offer to retain | Platform Capability: Server Notifications V2 |
| **Billing issue** | Failed payment | Grace period UX + retry | Platform Capability: Billing Grace Period |
| **Price increase** | Price change pushed | Consent flow | Platform Capability: price increase consent sheet |
| **Win-back** | Lapsed subscriber returns | Win-back offer | Platform Capability: Apple Win-Back (iOS 18+) |
| **Refund/support** | Refund request or complaint | Support surface, consumption data | Platform Capability: consumption API, refund feedback |

---

## DISCOUNT & PROMOTIONAL OFFERS

Discount offers are a distinct paywall type. Do not conflate with the main paywall.

### Trial vs no-trial on discount offers

- **"Try for free"** — removes risk. Best for new users with low product awareness. **Operator Insight.**
- **"Get X% off"** — creates urgency, anchors value. Best for users who already know the product. **Operator Insight.**
- Trial subscribers retain 1.4-1.7x better than direct buyers. **Vendor Aggregate Data** (Adapty 2026). Category-dependent — Productivity/Lifestyle direct buyers have higher 12-mo LTV.

### Discount depth

| Depth | Use case | Risk | Evidence |
|-------|----------|------|----------|
| 20-30% | Seasonal, re-engagement | Low LTV risk | Operator Insight |
| 30-40% | Standard post-close, holiday | Moderate | Operator Insight (RC holiday guide) |
| 50-60% | Annual welcome, win-back | Watch LTV erosion | Operator Insight |
| 60%+ | Aggressive win-back | High churn risk | Operator Insight |

**Vendor Aggregate Data:** 90% of subscriptions sell at full price (Adapty 2026).

### Compliance for discount offers

- **"X% OFF" needs legitimate reference price.** If no higher-priced plan visible, the discount has no honest basis. Show the reference product or tie to event. **Apple Rule** (misleading marketing).
- **"LOWEST PRICE" / "LIMITED TIME"** — fake urgency if price doesn't change. **Apple Rule.**
- **Savings math must be verifiable.** Both prices real, current, visible. **Apple Rule.**

---

## APPLE OFFER TYPES (2026)

| Offer Type | Target | Limit | Min iOS | Evidence |
|-----------|--------|-------|---------|----------|
| Introductory Offer | New subscribers | 1 per group per customer | iOS 11.2 | Platform Capability |
| Promotional Offer | Existing/former subscribers | Up to 10 per subscription | iOS 12.2 | Platform Capability |
| Offer Codes | Anyone with a code | 1M codes/quarter | iOS 14 | Platform Capability |
| Win-Back Offers | Lapsed subscribers | Multiple configurable | iOS 18 | Platform Capability |

WWDC 2025: Offer codes expanded to all IAP types. Promotional offers require JWS auth (back-deployed iOS 15).

---

## PHASE 4: TESTING PLAN

Priority order: placement/gate type → plan count/duration → trial structure → localization → price → copy/visual.

- Change one major thing at a time.
- Primary metric + guardrail metric.
- Choose winners by revenue/LTV/renewal quality, not just trial starts.
- Minimum 200 subscriptions per variant for significance. **Vendor Aggregate Data** (Adapty).

---

## PHASE 5: IMPLEMENTATION

Build using the app's existing architecture. Do not introduce new patterns unless necessary.

1. **Technical setup:** identify framework, billing layer, navigation, state management, remote config, analytics.
2. **Billing foundation:** product IDs match store, correct subscription group, intro offers configured, restore works, entitlement refresh works.
3. **Paywall layer:** load products, handle purchase/failure/cancel/restore, handle already-entitled users, handle network failures, log analytics, respect safe areas.
4. **Provider capabilities:** use Adapty/RevenueCat remote config and paywall builders where possible.
5. **Subscription state:** active, grace period, expired, restore without entitlement, lapsed, purchase while subscribed.
6. **Analytics events:** paywall_impression, paywall_dismissed, placement_id, variant_id, plan_selected, purchase_started/completed/failed, restore_started/completed, trial_started, converted_to_paid.

---

## iOS COMPLIANCE CHECKLIST

### Apple Rules (published, rejection risk):

- [ ] Clear description of what user gets (3.1.2(c))
- [ ] Subscription name and duration visible (3.1.2(c))
- [ ] Full renewal price prominent (most prominent pricing element)
- [ ] Trial duration and post-trial price shown if trial offered (3.1.2(a))
- [ ] Restore Purchases accessible
- [ ] Terms of Use link in-app
- [ ] Privacy Policy link in-app
- [ ] No misleading savings math
- [ ] No fake urgency/scarcity
- [ ] No fake reviews/ratings
- [ ] Existing paid users keep previously purchased access

### Field Reports (not official Apple rules, high review risk):

- [ ] Toggle paywall — mass rejections since Jan 2026 (Adapty/RC reports)
- [ ] Delayed close button >5s — higher rejection correlation (RevenueFlo 2026)
- [ ] Pricing font too small — ~16pt threshold observed (RevenueFlo 2026)
- [ ] Two full paywalls back-to-back — aggressive monetization flag (developer reports)
- [ ] Guilt-trip decline copy — high rejection correlation
- [ ] Auto-renewal disclosure missing — best practice, not currently guaranteed rejection (as of April 2026)

---

## BENCHMARK REFERENCE (April 2026)

All benchmarks are directional. Each carries source, date, and evidence level. Full source manifest: `sources.json`.

### Conversion Rates — Vendor Aggregate Data

| Metric | Value | Source | Date |
|--------|-------|--------|------|
| Install → Trial (global) | 10.9-11.2% | Adapty (16K apps) | Mar 2026 |
| Install → Trial (North America) | 14.5% | Adapty | Mar 2026 |
| Trial → Paid (global) | 25.6-27.8% | Adapty/RC | Mar 2026 |
| Trial → Paid (H&F) | 35.0-39.9% | Adapty/RC | Mar 2026 |
| Hard paywall D35 conversion | 10.7% | RC (115K apps) | Mar 2026 |
| Freemium D35 conversion | 2.1% | RC | Mar 2026 |
| Day 0 share of trial starts | 80-90% | Adapty/RC | Mar 2026 |

### Trial Length — Vendor Aggregate Data

| Length | Median Trial-to-Paid | Source | Date |
|--------|---------------------|--------|------|
| <4 days | 25.5% | RC | Mar 2026 |
| 5-9 days | 37.4% | RC | Mar 2026 |
| 17-32 days | 42.5% | RC | Mar 2026 |

### Revenue Per Install — Vendor Aggregate Data

| Metric | Value | Source | Date |
|--------|-------|--------|------|
| Hard paywall RPI (D14) | $2.32 | RC | Mar 2026 |
| Hard paywall RPI (D60) | $3.09 | RC | Mar 2026 |
| Freemium RPI (D60) | $0.38 | RC | Mar 2026 |

### Pricing Medians — Vendor Aggregate Data

| Period | Median | Range | Source | Date |
|--------|--------|-------|--------|------|
| Weekly | $5.99-$7.48 | $4.99-$6.99 | Adapty/RC | Mar 2026 |
| Monthly | $10.00-$12.99 | $7.99-$9.99 | Adapty/RC | Mar 2026 |
| Annual | $34.80-$38.42 | $29.99-$39.99 | Adapty/RC | Mar 2026 |

### A/B Test Win Rates — Vendor Aggregate Data

| Experiment | LTV Win Rate | Source | Date |
|-----------|-------------|--------|------|
| Localization | 62.3% | Adapty | Mar 2026 |
| Trial structure | 59.6% | Adapty | Mar 2026 |
| Plan duration | 58.7% | Adapty | Mar 2026 |
| Number of plans | 57.1% | Adapty | Mar 2026 |
| Price changes | 45.5% | Adapty | Mar 2026 |
| Visual/copy | 34.6% | Adapty | Mar 2026 |

### Retention (12-Month) — Vendor Aggregate Data

| Plan | Retention | Source | Date |
|------|-----------|--------|------|
| Annual | 44.1% | RC | Mar 2026 |
| Monthly | 17.0% | RC | Mar 2026 |
| Weekly | 3.4% | RC | Mar 2026 |

### Superwall Data — Vendor Case Study / Aggregate Study

| Metric | Value | Scope | Source | Date |
|--------|-------|-------|--------|------|
| Transaction abandon revenue | 17% of total | 18 companies, 525K users | Superwall | Aug 2024 |
| 2 vs 1 products | +61% conversion | 32M views, 15 apps | Superwall | 2025 |
| 3 vs 2 products | +44% additional | 32M views | Superwall | 2025 |

---

## DESIGN PATTERNS REFERENCE

| Pattern | Evidence Level | Claim | Source |
|---------|---------------|-------|--------|
| Trial Timeline | Vendor Case Study | +23% conversion, -55% complaints (Blinkist, single company) | Purchasely blog |
| Personalized Headline | Vendor Aggregate Data | 15%+ lift (Adapty platform data, methodology not open) | Adapty 2026 |
| Animated Paywall | Vendor Aggregate Data | 2.9x vs static (Adapty platform data, methodology not open) | Adapty 2026 |
| "Building Your Plan" loader | Operator Insight | No published data, widely adopted by Noom/Flo/BoldVoice | Industry observation |
| Contextual Feature Gate | Operator Insight | Strava uses extensively, no published conversion data | Industry observation |
| Multi-Page Paywall | Hypothesis | +27% Speak4Me, but Stompers found single-page won. Conflicting. | Superwall |
| "Design Your Trial" | Hypothesis | Superwall claims "winning nearly every time", methodology not published | Superwall 2025 |
| Anchor Pricing | Operator Insight | Universal adoption, no isolated uplift data | Industry standard |
| Trial-on-Annual Only | Operator Insight | "One of the most consistent patterns" (Adapty), no isolated data | Adapty 2026 |

---

## CURRENT MARKET PATTERNS (April 2026)

Repeating patterns from top apps, per Adapty/RevenueCat/Superwall 2026 data. All **Vendor Aggregate Data** unless noted.

- Weekly plans = 55.5% of all app revenue (up from 43.3% in 2023). H&F exception: annual 60.6%.
- Hard paywalls: ~5x conversion vs freemium, ~8x RPI. Same long-term retention.
- 90% of subscriptions sell at full price. Discounts work for recovery, not as default.
- Apps running 50+ experiments earn 18.7x more revenue (Adapty platform data — **Vendor Aggregate Data**, interpret with caution: correlation, not causation).
- Top 10% of apps capture 94.5% of revenue.
- European apps charge 29-39% more than North American. European subscribers stay longer.

---

## ANTI-PATTERNS

1. Feature dump instead of value communication
2. Testing copy/colors before testing structure
3. Per-week breakdown larger than actual billed amount
4. Fake urgency / countdown not tied to real expiry
5. Toggle paywalls on iOS (Field Report: mass rejections Jan 2026)
6. Delayed or hidden close buttons
7. Guilt-based decline text
8. Fake reviews/ratings/user counts
9. Deceptive plan pre-selection
10. Shipping without restore and legal links
11. Assuming one benchmark fits every category
12. Claiming specific uplift as guaranteed
13. Emotional gimmicks without evidence and product fit

---

## DEFAULT OUTPUT FORMAT

1. **Current state** — what the app is doing now
2. **Main problem or opportunity** — plain language
3. **Recommended access model** — from taxonomy
4. **Recommended placements** — from taxonomy
5. **Recommended presentation** — from taxonomy
6. **Screen content** — headline, benefits, pricing, CTA, trust
7. **Tests to run** — priority order
8. **iOS review risks** — Apple Rules + Field Reports

Each finding must carry its evidence level. Do not repeat findings across sections. Keep practical, not theoretical.

---

## DATA SOURCES

| Source | Dataset | Date |
|--------|---------|------|
| Adapty | 16,000+ apps, $3B revenue | Mar 2026 |
| RevenueCat | 115,000+ apps, $16B revenue | Mar 2026 |
| Superwall | 100M+ monthly paywall views | 2024-2026 |
| Apple | App Store Review Guidelines | Current |

Full source manifest with every numeric claim: `sources.json`
