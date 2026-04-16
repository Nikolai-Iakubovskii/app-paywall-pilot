# Subscription Metrics Glossary

Subtle differences between metrics trip up indie devs constantly. ARPU vs ARPPU. Gross vs realized LTV. CR vs effective CR. This module is the canonical definitions.

When the user uses one term but means another, gently correct.

---

## Revenue Metrics

### ARPU — Average Revenue Per User
```
ARPU = Total Revenue in Period / Total Users in Same Period
```
- "Users" includes free + trial + paid + lapsed
- Useful for cross-app comparison
- General mobile baseline: ~$0.04 per user (Adapty 2026)

### ARPPU — Average Revenue Per **Paying** User
```
ARPPU = Total Revenue in Period / Total Paying Users in Same Period
```
- Excludes free users
- Always larger than ARPU
- Useful for unit-economics decisions
- Subscription apps: ARPPU often $30-60/yr

**Common mistake:** "My ARPU is $50" usually means ARPPU. Check.

### MRR — Monthly Recurring Revenue
```
MRR = Σ (Monthly Subscriptions × Monthly Price) + (Annual Subscriptions × Annual Price / 12) + ...
```
- Normalize all plans to monthly equivalent
- Excludes one-time purchases, refunds
- Lifetime: NOT in MRR (no recurring)

### ARR — Annual Recurring Revenue
```
ARR = MRR × 12
```
- Just MRR ×12 for simplicity; doesn't predict 12-month revenue

### Net Revenue
```
Net Revenue = Gross Revenue − Apple/Play Cut − Refunds − Taxes
```
- What you actually keep
- Apple cut: 15% (SBP <$1M revenue) or 30%
- Play cut: 15% (sub year 2+) or 30% (year 1, IAP)

---

## Lifetime Value Metrics

### Gross LTV
```
Gross LTV = ARPPU × Average Customer Lifetime
```
- Before Apple/Play fee
- Headline number — use carefully
- Doesn't account for refunds

### RLTV / Realized LTV — Net of Refunds and Fees
```
RLTV = (Gross Revenue − Refunds) × (1 − Apple Fee) per Paying User
```
- What you actually earn per paying user
- Use for unit economics decisions
- Adapty 2026 reports use RLTV

### Install LTV
```
Install LTV = RLTV × Install→Paid Conversion Rate
```
- Per install, not per payer
- Adapty 2026: H&F install LTV $1.21 (highest), Entertainment $0.59 (lowest)
- Useful for CAC ceiling math

### Predicted LTV
- Forward projection using cohort retention curves
- See [unit-economics-calculator.md](unit-economics-calculator.md) for the calculation
- Use cohort analysis (NOT blended) for accuracy

---

## Conversion Metrics

### CR — Conversion Rate (generic)
- Always specify which conversion. "CR 6%" is ambiguous without context.

### Install→Trial CR
```
Install→Trial CR = Trial Starts / Installs
```
- Adapty 2026: 10.9% global, 14.5% NA
- Excludes restore-to-trial events

### Trial→Paid CR
```
Trial→Paid CR = Paid Conversions / Trial Starts
```
- Adapty 2026: 27.8% global, 35-42% H&F
- Measure at end of trial period, not earlier

### Effective CR (with trial)
```
Effective CR = Install→Trial CR × Trial→Paid CR
```
- Equivalent to direct install→paid for trial-using apps
- Always show breakdown to identify which step is the bottleneck

### Install→Paid CR (D35)
```
Install→Paid CR = First Paid Conversions / Installs (within 35 days)
```
- RC 2026 standard window
- Hard paywall: 10.7%, Freemium: 2.1%

---

## Acquisition Metrics

### CPI — Cost Per Install
```
CPI = UA Spend / Installs
```
- Bottom of funnel for UA performance
- iOS premium: $2.50 median; Android $1.50 (AppsFlyer 2026)

### CPR — Cost Per Registration
```
CPR = UA Spend / Registrations
```
- iOS: $7.55 median; Android: $2.17 median
- Use when signup is gated

### CAC — Customer Acquisition Cost
```
CAC = UA Spend / Paying Customers Acquired
```
- The denominator that matters for unit economics
- iOS first IAP: $77.45 median; Android: $86.72

### LTV:CAC Ratio
```
LTV:CAC = LTV / CAC
```
- 3:1 = healthy, 2:1 = marginal, 5:1+ = underinvesting in growth
- Compare net LTV to CAC, not gross

### eCPI — Effective CPI (post-fraud, post-attribution)
- Real CPI after deduplicating bot traffic, fraud, attribution lag
- Always lower-quality (higher) than gross CPI

### ROAS — Return on Ad Spend
```
ROAS(T) = (CR × ARPU(T)) / CPI
```
- ROAS = 1.0 means breakeven
- ROAS > 3 considered strong for mobile UA

---

## Retention Metrics

### Retention Rate (Day N)
```
Day N Retention = Active Users on Day N / Cohort Size
```
- "Active" definition matters: opens app, paying, etc.
- Subscription retention: % of cohort still paying

### Renewal Rate (Nth)
```
Nth Renewal Rate = Subscribers Who Renew Nth Time / Subscribers Eligible
```
- Adapty 2026 H&F: 1st renewal 67.7%, 2nd 45.1%, 3rd 37.1%, 4th 31.6%

### Cumulative Renewals
- Used in LTV calculations
- "1.6 cumulative renewals at 1yr" = monthly subscriber on average paid 2.6 cycles total
- Default values in [unit-economics-calculator.md](unit-economics-calculator.md)

### Churn Rate
```
Monthly Churn = Subscribers Lost in Month / Subscribers at Start
Annual Churn = 1 − (1 − Monthly Churn)^12
```
- Inverse of retention
- AI apps: ~30% faster churn than category avg (RC 2026)

---

## Refund / Failure Metrics

### Refund Rate
```
Refund Rate = Refunded Transactions / Total Transactions
```
- Adapty 2026 baselines: Weekly 2.6%, Monthly 3.2%, Annual 4.2%
- Photo & Video APAC: up to 14.1%

### Involuntary Billing Failure Rate
```
IBF Rate = Failed Renewals / Renewal Attempts
```
- RC 2026: Google Play ~31% of cancellations, App Store 14%
- Reduce via grace period UX, payment retry

---

## Pricing Metrics

### Pricing Index (US = 1.0)
- Adapty 2026: UK/FR/DE/IT/ES = 1.2, MX/SA/Chile = 1.0, India = 0.6
- Use for manual per-territory pricing

### Per-Period Breakdown
- Annual $59.99 → "$5/month" or "$0.16/day"
- Apple Rule: actual billed amount must be the most prominent

### Anchor Price
- Higher reference price that frames the target as a deal
- Calm: monthly £14.99 strikethrough → annual £39.99 looks cheap

---

## Cohort Terms

### Install Cohort
- Users grouped by install date
- Retention curve = % still paying / engaged at Day N from install
- Most common cohort type

### Trial Cohort
- Users grouped by trial start date
- Useful for trial-to-paid analysis

### Calendar Cohort
- Users grouped by calendar period (week, month)
- Apphud's "calendar cohort revenue" — see what each calendar week's signups earned over time

### Acquisition Channel Cohort
- Users grouped by channel (Meta, ASA, organic)
- Reveals channel quality: same CPI different LTV

---

## Plan Architecture Terms

### Subscription Group (Apple)
- Container for mutually-exclusive plans
- User can have at most one active per group
- Used for upgrade/downgrade/crossgrade

### Base Plan + Offer (Play)
- Play's mental model: base plan = recurring product; offers = modifications (trial, intro discount)
- Multiple offers per base plan with different eligibility (NEW_SUBSCRIBER etc.)

### Intro Offer (Apple)
- One per group per customer (lifetime)
- Use for free trials and pay-as-you-go discounts

### Promotional Offer (Apple)
- For existing/former subscribers
- Up to 10 per subscription
- Requires JWS auth (back-deployed iOS 15)

### Win-Back Offer (Apple, iOS 18+)
- Apple-native surface on App Store product page
- Multiple configurable per subscription

---

## Data Source Terms

### Vendor Aggregate Data
- Large-scale report (10K+ apps or $1B+ revenue tracked)
- Adapty 16K, RC 115K, AppsFlyer 1.7B installs

### Vendor Case Study
- Single-app published result
- Blinkist via Purchasely is the canonical example

### Field Observation
- Developer rejection reports, not Apple-published
- RevenueFlo, Adapty + RC field reports on toggle paywall

### Operator Insight
- Practitioner observation without published dataset
- "Trial timeline beats text disclosure" before Blinkist quantified it

### Hypothesis
- Directional signal, not validated
- "Animated paywalls 2.9x convert" — methodology not open

See SKILL.md EVIDENCE LADDER for full hierarchy.

---

## Behavioral / Cognitive Concepts

These come from Kahneman's body of work and are foundational to paywall design. Full treatment in [pricing-psychology.md](pricing-psychology.md). Quick definitions here.

### Loss Aversion
Losses felt ~2x more painful than equivalent gains. **Source:** Kahneman & Tversky 1979 (Prospect Theory). **Paywall use:** loss-frame trial expiry copy ("don't lose your progress") beats gain-frame.

### Anchoring
Even arbitrary numbers bias subsequent estimates. **Source:** Tversky & Kahneman 1974. **Paywall use:** strikethrough monthly price anchors annual; show premium tier first.

### System 1 / System 2
S1 = fast intuitive (95%+ of decisions); S2 = slow deliberate. **Source:** Kahneman 2011. **Paywall use:** above-fold = S1 zone; pre-selected default routes user through S1; cognitive load triggers S2 = abandonment.

### Endowment Effect
People value what they own ~2x more than the same thing before owning. **Source:** Kahneman, Knetsch, Thaler 1990. **Paywall use:** reverse trial mechanics; trial timeline transparency builds endowment.

### Peak-End Rule
Experiences judged by emotional peak + ending, not average. **Source:** Kahneman et al 1993. **Paywall use:** engineer a positive onboarding peak (personalized plan reveal) + positive paywall ending.

### Default Effect / Status Quo Bias
People stick with defaults. Organ-donation: 86% opt-out vs 4% opt-in (same population, different default). **Source:** Kahneman, Knetsch, Thaler 1991. **Paywall use:** pre-select annual; "Most popular" badge.

### Mental Accounting
People categorize money into mental accounts; same dollar feels different by category. **Source:** Thaler 1980/1985/1999, built on Kahneman foundation. **Paywall use:** "$0.16/day" = daily-expense account (low friction); "$59/year" = annual-investment account (higher friction).

### WYSIATI (What You See Is All There Is)
S1 makes confident judgments based only on visible info; unseen = nonexistent. **Source:** Kahneman 2011 Ch. 7. **Paywall use:** above-fold rules; trial terms must be visible; strongest argument for Apple "billed amount most prominent" rule.

### Substitution Heuristic
Brain swaps hard questions for easier ones unconsciously. **Source:** Kahneman 2011 Ch. 9. **Paywall use:** user can't answer "is this worth $X for 12 months?" so they answer "do I trust this app?" → social proof + authority beat feature lists.

### Planning Fallacy
People underestimate time/effort of tasks. **Source:** Kahneman & Tversky 1979 (Intuitive Prediction). **Paywall use:** users overestimate their cancellation discipline → trials work even with high "forgot to cancel" rates → transparency (Trial Timeline) doesn't kill conversion.

### Hedonic Adaptation
People adapt to new conditions faster than expected. **Source:** Kahneman, Diener, Schwarz 1999. **Paywall use:** reverse trial works because user adapts to premium → losing it triggers loss aversion; build habit-forming features in week 1.

### Decoy Effect (Asymmetric Dominance)
Adding a clearly inferior option shifts preference toward the target. **Source:** Ariely 2008 (Economist subscription experiment). **Paywall use:** Tinder's 7-day Passport priced equal to 7-day Plus makes Plus look like obvious value.

### Cialdini's 7 Principles
Reciprocity, Commitment & Consistency, Social Proof, Authority, Liking, Scarcity, Unity. **Source:** Cialdini 1984 + 2016. **Paywall use:** Social Proof + Authority test as most-influential in mobile (Springer 2024).

### Fogg Behavior Model (B = M × A × T)
Behavior = Motivation × Ability × Trigger; all three must converge. **Source:** Fogg 2009 (Persuasive Tech, 1,900+ pubs ref). **Paywall use:** when motivation is borderline, reduce ability friction (pre-select default, 1-tap purchase) instead of adding more copy.

### Choice Overload (Iyengar Jam Study)
6-jam display sold 10x better than 24-jam display in real-supermarket experiment. **Source:** Iyengar & Lepper 2000, JPSP. **Paywall use:** 2–3 plans is the sweet spot. **Caveat:** Scheibehenne 2010 meta-analysis shows context-dependent magnitude.

### IKEA Effect
People value self-made products as much as expert-made; effect requires successful completion. **Source:** Norton, Mochon, Ariely 2012, JCP. **Paywall use:** long onboarding + "your plan reserved" completion moment = scientifically grounded ownership lever.

### Hyperbolic Discounting / Present Bias
Disproportionately steep discount on future rewards; "I want it now" beats "I want more later." **Source:** Laibson 1997, QJE. **Paywall use:** weekly plans win on present bias; per-day framing exploits it positively; annual default must work harder against it.

### Goal-Gradient Effect
Effort accelerates as users approach reward; bonus head-start works (12-stamp card with 2 free completes faster than regular 10-stamp). **Source:** Kivetz, Urminsky, Zheng 2006, JMR. **Paywall use:** progress bars in onboarding; bonus head-start framing; streak counters in retention.

### Negativity Bias
Bad weighs more than good across all domains; "1-star weighs ~5x 5-star" (rule of thumb). **Source:** Baumeister et al 2001, RGP, 10K+ citations. **Paywall use:** refund rate matters more than conversion uplift; treat refund flow as marketing; under-promise on paywall.

### Costly Signaling
Premium pricing signals quality when quality cannot be directly verified. **Source:** Spence 1973, QJE, Nobel 2001. **Paywall use:** don't undercharge in your category; price at category median or above; brand investment signals durability.

### Psychological Reactance
When freedom is threatened, people restore it by opposing the push. **Source:** Brehm 1966. **Paywall use:** fake urgency backfires; aggressive re-prompting triggers reactance; always offer dignified opt-out.

### Sunk Cost Fallacy
Continued commitment based on past investment, even when irrational. **Source:** Arkes & Blumer 1985, OBHDP. **Paywall use:** long onboarding flows commit user to completion; combine with goal-gradient (#16) and IKEA Effect (#14) for full effect.

### Ego Depletion / Decision Fatigue (REPLICATION FAILED)
Original 1998 claim: self-control depletes like fuel. **Hagger 2016 (2,141 participants, 24 labs) and Vohs 2016 (3,531 participants, 36 labs) both failed to find the effect.** **Do NOT cite as mechanism.** The practical "keep paywalls simple" rule is correct; the mechanism is **Choice Overload + System 1**, not ego depletion.

### Hooked Model (practitioner framework)
Trigger → Action → Variable Reward → Investment loop. **Source:** Eyal 2014 (book, not peer-reviewed). Underlying academic basis: Skinner variable reward + IKEA Effect + Sunk Cost. Useful as operational framework; cite underlying acads for grounding.

### Identity-Based Habits (practitioner framework)
"I am the type of person who…" framing for behavior change. **Source:** Clear 2018, *Atomic Habits* (book, not peer-reviewed). Underlying academic basis: Bem 1972 self-perception + Cialdini commitment & consistency. Useful for identity-led headline copy.

---

## Quick Reference: Acronyms

| Acronym | Full | Use |
|---------|------|-----|
| ARPU | Average Revenue Per User | Includes free users |
| ARPPU | Average Revenue Per Paying User | Excludes free users |
| MRR | Monthly Recurring Revenue | Subscription revenue normalized monthly |
| ARR | Annual Recurring Revenue | MRR × 12 |
| LTV | Lifetime Value | Total revenue per customer |
| RLTV | Realized LTV | Net of refunds + Apple fee |
| CAC | Customer Acquisition Cost | Spend per paying customer |
| CPI | Cost Per Install | Top-of-funnel UA cost |
| CPR | Cost Per Registration | Cost per signup |
| CR | Conversion Rate | Always specify which conversion |
| ROAS | Return on Ad Spend | Revenue / Spend ratio |
| RPI | Revenue Per Install | LTV per install |
| RPM | Revenue Per Mille | Per 1,000 (often for ads) |
| MAU/DAU | Monthly/Daily Active Users | Engagement |
| IAP | In-App Purchase | All purchases (subs + consumables + lifetime) |
| MMP | Mobile Measurement Partner | AppsFlyer, Adjust, Singular |
| ATT | App Tracking Transparency | iOS 14.5+ tracking opt-in |
| SKAN | SKAdNetwork | Apple's privacy-preserving attribution |
| SBP | Small Business Program | Apple 15% rate at <$1M |
| DMA | Digital Markets Act | EU regulation requiring alternative billing |
