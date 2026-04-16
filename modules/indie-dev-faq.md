# Indie Dev FAQ

Direct-answer mode. When the user asks a single tactical question, give threshold + verdict + one action. No fluff. Each answer cites its data source.

For a full audit, use the SKILL.md DEFAULT OUTPUT FORMAT instead. For numerical projections, use [unit-economics-calculator.md](unit-economics-calculator.md).

---

## Pricing & Plans

### "Should I add a weekly plan?"
**Yes, if** you're in Productivity, Utilities, Photo & Video, AI, or H&F entry-tier. Weekly drives 55.5% of all subscription revenue (Adapty 2026). **Pair with a free trial** — day-30 retention jumps 23% → 42%. **No, if** your value compounds only over weeks (Education, behavior change apps with long aha) — short cycle won't show value before user cancels.

### "Should I raise my prices?"
Almost certainly yes. **High-priced apps earn 3x the LTV** of low-priced apps (Adapty 2026). For weekly plans, higher prices actually convert better (price signals quality). Pricing has 45.5% A/B win rate (Adapty). Action: test +20-30% on your highest-distribution plan first.

### "Should I have 2 or 3 plans?"
3 if your distribution % data shows people pick all three. Superwall data: 1→2 plans = +61% conversion, 2→3 = +44% additional. **But** equal LTV across plans is critical — don't let conversion gain come at LTV expense. **Default to 2** (annual + monthly) if you don't have data; add a 3rd only when you can articulate why each tier exists.

### "What's the right annual discount vs monthly?"
Adapty 2026: median annual = ~3x monthly. So if monthly is $9.99, annual ~$30 is the floor; $59.99 ($5/mo) is mid-market; $89.99 is premium. Frame as "save 50%" or "$5/month billed annually" — never lead with the annual total only.

### "Should I add a lifetime plan?"
Only if you have low-intent users who fear subscription fatigue. Apphud-style hybrid: 35% of subscription apps now offer lifetime alongside subs (RevenueCat 2026). Caveat: lifetime cuts your LTV ceiling; price it 2-3x your annual to avoid cannibalization.

### "Should I use charm pricing ($9.99 vs $10)?"
Yes by default. Anderson & Simester 2003 field experiment: $39 outsells $34 due to left-digit anchoring. App Store auto-tier already uses charm; matters more if you're manually setting prices. Exception: luxury positioning ($60 reads more premium than $59.99).

---

## Trials

### "Should I use a free trial?"
Depends on category:
- **Yes, strongly:** H&F, Education, Utilities (trial users +50.4% 12-mo LTV in Education)
- **No (or test direct):** Productivity ($56.95 direct vs $49.13 trial), Lifestyle (~21% direct premium)
- **Test both:** AI apps, Gaming

Source: RevenueCat 2026 + Adapty 2026.

### "How long should my trial be?"
Default: **7 days**. RevenueCat 2026 trial→paid: ≤4 days = 25.5%, 5-9 days = 37.4%, 17-32 days = 42.5%. Long trials convert better but more users forget to cancel = more refunds. 7-day is balanced. **Gaming exception:** 73% use ≤4-day trials (fast value moment).

### "Should the trial be on all plans or annual only?"
**Annual only.** Adapty Operator Insight: trial-on-annual-only is "one of the most consistent patterns". Math: trial-acquired weekly retains 5.5% D380 vs annual 19.9% — trial ROI is ~4x better for annual.

### "Why is my trial-to-paid so low?"
Sub-15% = poor (vs 27.8% global benchmark). Three checks:
1. **Trial too long** → users forget. Shorten to 7 days.
2. **No pre-expiry reminder** → Blinkist Day-5 push lifted notif opt-in 1,200% (6%→74%) and trial signups +23%.
3. **Value not hit in first 2-3 days** → audit onboarding-to-aha-moment time.

### "Reverse trial — when?"
For low-intent audiences (Photo, Lifestyle, Productivity). Give full premium for N days, then revert to free. RC Operator Insight. Not a StoreKit free trial — your app manages it. Don't claim "free trial" if you mean reverse trial (Apple Rule risk).

---

## Conversion & Funnel

### "Are my numbers good?"
Need 5 inputs to benchmark: category, plan type, install→paid (or →trial), day-30 retention, primary market. Then compare against [category-deep-dives.md](category-deep-dives.md). Or run [unit-economics-calculator.md](unit-economics-calculator.md).

### "What's a good install-to-trial conversion rate?"
Adapty 2026 global: 10.9%. NA: 14.5%. APAC: 7.6%. Below 7% = paywall not compelling. Above 14% in NA = excellent. Check [category-deep-dives.md](category-deep-dives.md) for category-specific.

### "What's a good install-to-paid (D35)?"
RevenueCat 2026: Hard paywall 10.7% / Freemium 2.1% globally. NA: 2.8%. IN/SEA: 0.7%. Hard paywall ~5x freemium.

### "Why is my install-to-trial so low?"
Sub-7% = paywall not earning the install. Three checks:
1. **Placement** — paywall before user understands value? Move post-aha.
2. **Headline outcome-led?** "Sleep better in 7 nights" beats "Premium Features".
3. **Real social proof above fold?** User count, ratings — Cialdini's most-influential principle (Springer 2024).

### "My CR is great but ARPU is low — what's wrong?"
Either pricing too low (raise it; high-priced apps 3x LTV) or plan mix wrong (more weekly than annual; weekly retains 5.5% D380 vs annual 19.9%). Run calculator to see which lever moves more.

---

## Retention & Churn

### "My churn is high"
Depends on plan:
- **Weekly:** 65% cancel month 1 is normal. Track LTV not month-1 retention.
- **Monthly:** 43% at D90 is benchmark. Below that = fix value delivery weeks 2-4.
- **Annual:** Spike at renewal expected. Add win-back flow 30 days before renewal (Apple Win-Back Offer iOS 18+).

### "What's a good 12-month retention?"
RevenueCat 2026: Annual 44.1%, Monthly 17.0%, Weekly 3.4%. By category — Utilities lead annual at 22.1%, Productivity leads overall at ~14% 1yr.

### "How do I reduce churn on my annual plan?"
1. **Day -30 win-back push** — give 30 days notice before renewal with re-engagement
2. **Apple Win-Back Offer (iOS 18+)** — Apple-native discount for lapsed
3. **Faster time-to-value** — #1 retention lever per Adapty
4. **Email + push series** during weeks 2-4 of new sub

### "Should I worry about my refund rate?"
Adapty 2026 baseline:
- Weekly (no trial): ~2.6%
- Monthly: ~3.2%
- Annual: ~4.2%
- Photo & Video APAC: up to 14.1%

Above 5% on annual = warning. Audit paywall copy for overpromising. Implement Trial Timeline (Blinkist: -55% complaints).

### "Google Play refunds higher than App Store?"
Yes, by ~2x. RevenueCat 2026: Play involuntary billing failures = 31% of cancellations vs App Store 14%. Implement payment retry UX. Use grace period notifications.

---

## Markets & Geography

### "Where should I expand?"
High-LTV markets often ignored: Switzerland ($28.5/yr), Qatar ($27.5), Israel ($27.0), Iceland ($23.9), UK ($23.6), Japan ($23.4) — all above US ($19.9). Source: Adapty 2026. **Also:** AppsFlyer 2026 shows IN/SEA driving 49% of net Android paid install growth — different play (low LTV but volume).

### "Should I localize prices?"
Yes. Pricing index US=1.0: UK/FR/DE/IT/ES = 1.2; Mexico/SA/Chile = 1.0; Indonesia/Turkey = 0.7; India = 0.6 (Adapty 2026). H&F annual: Germany charges 4.4x more than Turkey. Same-SKU-everywhere = leaving 30%+ on the table in Europe.

### "Should I have a separate SKU for India / emerging markets?"
Probably yes if >5% of installs. ChatGPT launched "Go" tier at $8 specifically for India. AppsFlyer 2026: emerging markets are where Android growth is. See [localization.md](localization.md).

### "Why is European LTV higher than NA?"
Adapty 2026: EU apps charge 29-39% more than NA AND EU subscribers stay longer. Both effects compound. If you ship the same SKU in EU as NA, you're using charm-rounded prices (auto-tier) but missing the price-elasticity surplus.

---

## Acquisition & UA

### "What's a healthy LTV:CAC ratio?"
**3:1 minimum**. Below 2:1 = unprofitable. Above 5:1 = underinvesting in growth. Quick rule: 12-month LTV ÷ 2 = your max sustainable CAC. See [cac-acquisition.md](cac-acquisition.md).

### "Should I increase my UA budget?"
Only if LTV:CAC > 3:1 with current channels. Above 5:1 = scale aggressively. Below 3:1 = fix unit economics first (price up, retention up, or CPI down). AppsFlyer 2026: top 5 apps per category control >90% of UA spend — tough market for new entrants.

### "Should I focus iOS or Android first?"
Indie dev: iOS first (higher LTV per payer: $32 NA vs Android lower; iOS = 77% of new app launches per RC 2026). **But** AppsFlyer 2026: Android subscription UA is growing 4x faster than iOS — Android is the growth lane long-term, especially in IN/SEA/LATAM.

### "Apple Search Ads worth it?"
Generally yes for branded/category keywords (intent-rich). CPI lower than Meta/TikTok. Adapty/RC field reports: ASA-acquired users have higher trial start rate than paid social. See [cac-acquisition.md](cac-acquisition.md).

---

## Compliance & Apple

### "Will my paywall get rejected?"
Run through SKILL.md iOS COMPLIANCE CHECKLIST. Top causes of 2026 rejections (RevenueFlo): toggle paywall (mass-rejected since Jan 2026), pricing font <16pt, delayed close >5s, two paywalls back-to-back, guilt decline copy.

### "I'm using a toggle paywall — am I in trouble?"
Yes. **Apple cited reason (Jan 2026):** "This design is confusing and may prevent users from understanding that they are committing to an auto-renewing subscription." Replace with separate plan cards or trial-on-annual-only. Migration guide planned in [docs/migrations/](../docs/migrations/).

### "Can I qualify for Apple's 15% Small Business Program?"
If your annual revenue across all your apps is under $1M, yes. Apply at https://developer.apple.com/app-store/small-business-program/. Switching from 30% → 15% = **+17.6% net ARPU instantly**. No-brainer if eligible.

### "Can I avoid the 30% commission via web checkout?"
US only post-Epic ruling (May 2025). Some indie devs report 65-120% revenue increases bypassing the cut, but mobile-web conversion is lower. Best for apps with strong content marketing / search traffic. Disclose: "External purchase — handled by [you], not Apple."

---

## Strategy & Growth

### "Should I run more A/B tests?"
Yes. Adapty 2026: apps running 50+ experiments earn 18-40x more revenue (correlation, but directional). Minimum 200 subs/variant for significance. Test order (Adapty win rates): localization 62.3% → trial structure 59.6% → plan duration 58.7% → plan count 57.1% → price 45.5% → visual/copy 34.6%. Don't start with copy.

### "Should I switch from freemium to hard paywall?"
Probably yes if CR is the bottleneck. Hard paywalls: 78% trial starts week 1 vs 45% for freemium (Adapty 2026). 5x D35 conversion advantage. **But** brand backlash risk if you previously had free features. See Strava 2025 Year-in-Sport paywall PR cycle for reference (in [teardowns.md](teardowns.md)).

### "Should I add web checkout?"
Yes if (a) you have meaningful web traffic OR (b) you're US-only and can take advantage of post-Epic ruling. 65-120% revenue increases reported. Engineering complexity = medium. Don't replace App Store — supplement it.

### "How often should I redesign my paywall?"
Top apps iterate every 6-8 weeks (Adapty 2026 vendor_blog). But: redesign means structural change (new placement, new plan mix, new trial structure). Cosmetic visual refresh is the LOWEST-leverage test (34.6% win rate). Don't conflate iteration with redesign.

### "What's the single highest-leverage change I can make?"
Localization. 62.3% LTV win rate (Adapty 2026). Manual per-territory pricing for top 5 markets typically lifts ARPU 15-25%. Most indies skip this entirely — biggest under-served opportunity in the data.

---

## When the Question Is Outside This FAQ

If the user's question doesn't fit a single threshold-and-action answer, switch to:
- Full audit → SKILL.md DEFAULT OUTPUT FORMAT
- Numerical projection → [unit-economics-calculator.md](unit-economics-calculator.md)
- Compliance triage → [decision-trees.md](decision-trees.md) Tree 8
- Pattern reference → [teardowns.md](teardowns.md)
- Copy or layout → [copy-library.md](copy-library.md) / [screen-anatomy.md](screen-anatomy.md)

---

## Source Pointers

- Adapty 2026: https://adapty.io/state-of-in-app-subscriptions/
- RevenueCat 2026: https://www.revenuecat.com/state-of-subscription-apps/
- AppsFlyer 2026: https://www.appsflyer.com/resources/reports/subscription-marketing/
- Superwall studies: https://superwall.com/blog/
- Apple SBP: https://developer.apple.com/app-store/small-business-program/
- Adapty growth-expert-skill (FAQ format inspiration): https://github.com/adaptyteam/growth-expert-skill
