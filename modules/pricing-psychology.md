# Pricing Psychology

Academic foundations + mobile-paywall application. Use academic principles as **Operator Insight** when applied to mobile (academic studies on physical/web purchase don't always transfer cleanly to mobile in-app subscriptions).

**Daniel Kahneman is the foundational source.** His work (often co-authored with Tversky) won the 2002 Nobel Memorial Prize in Economics. Most of what we now call "behavioral pricing" derives from his findings. This module treats his concepts as the trusted base for paywall design decisions.

---

## Kahneman Foundations (Trusted Base)

These 8 concepts from Kahneman's body of work are the most-applicable to subscription paywall design. Each links a specific paper / book chapter to a concrete paywall design choice.

### 1. Prospect Theory & Loss Aversion (Kahneman & Tversky 1979)

**Citation:** Kahneman, D., & Tversky, A. (1979). Prospect Theory: An Analysis of Decision under Risk. *Econometrica*, 47(2), 263–291. **65,000+ citations.** Foundational paper that won the 2002 Nobel.

**Finding:** Losses are felt approximately **2x as painful** as equivalent gains. People are not rational utility-maximizers; they're loss-avoiders.

**Mobile paywall application:**
- **Trial-end framing:** "Don't lose your streak / progress / personalized plan" beats "Keep your access"
- **Renewal-risk push:** "Lose access in 2 days" beats "$X to renew"
- **Win-back:** "You're missing out on [feature]" beats "Come back for $X"
- **Free-tier limit hit:** "You've used 3 of 3" beats "Upgrade for unlimited"

**Design rule:** Frame the cost of NOT subscribing as a loss the user already has, not as a gain they could acquire. The free trial is a loss aversion machine — user takes possession, then losing it hurts.

---

### 2. Anchoring (Tversky & Kahneman 1974)

**Citation:** Tversky, A., & Kahneman, D. (1974). Judgment under Uncertainty: Heuristics and Biases. *Science*, 185(4157), 1124–1131.

**Finding:** Even **arbitrary numbers** anchor subsequent estimates. Famous spinner experiment: spin landing on 65 → estimates of African nations in UN higher; spin 10 → estimates lower. The anchor doesn't have to be relevant to bias judgment.

**Mobile paywall application:**
- **Strikethrough monthly price** anchors the annual as a deal (Calm's £14.99 → £39.99/yr pattern)
- **Show $200 Pro tier first** anchors $20 Plus as "reasonable" (ChatGPT pattern)
- **"Save $40/year"** needs the $40 reference to work — without anchor, savings don't compute
- **Comparison table** with Free column anchors what user is "missing"
- **First plan card seen** influences the perceived value of all others (default to highest tier visible first when you want premium-anchor)

**Design rule:** Always set an anchor before showing your target price. Apple Rule: the anchor must be a real reference price, not fictional.

---

### 3. System 1 / System 2 (Thinking, Fast and Slow, 2011)

**Citation:** Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus and Giroux. **Best-selling book that synthesizes 40 years of his research.**

**Finding:** Decisions split between two systems:
- **System 1:** fast, intuitive, automatic, emotional. Handles 95%+ of decisions.
- **System 2:** slow, deliberate, effortful, rational. Engaged only when System 1 hits friction.

**Mobile paywall application:**
- **Above-fold = System 1 decision zone.** User decides to subscribe / dismiss in 3 seconds, before System 2 engages.
- **Cognitive load = abandonment.** Anything that forces System 2 (math, fine print, choice paralysis) raises bounce rate.
- **Pre-selected default** routes user to the System 1 path (no choice = no thinking)
- **Visual pricing hierarchy** (one big number, others subordinate) lets System 1 grab the answer

**Design rule:** Design for System 1. If your paywall requires the user to think, you've lost most of them. Our SKILL.md core principle "Clarity beats cleverness" derives directly from this.

---

### 4. Endowment Effect (Kahneman, Knetsch & Thaler 1990)

**Citation:** Kahneman, D., Knetsch, J. L., & Thaler, R. H. (1990). Experimental Tests of the Endowment Effect and the Coase Theorem. *Journal of Political Economy*, 98(6), 1325–1348.

**Finding:** Once people "own" something, they value it ~**2x more** than before they owned it. Coffee mug experiment: students given a $5 mug demanded ~$7 to sell it; students who didn't have one would only pay ~$3. Pure ownership doubled valuation.

**Mobile paywall application:**
- **Reverse trial mechanics scientifically explained.** User "owns" premium for 7 days. Refusing to subscribe = giving it up = endowment loss = 2x more painful than not having had it.
- **Trial Timeline transparency** (Blinkist pattern) deliberately builds endowment: "You ALREADY have access; here's when it ends."
- **Free preview content** creates partial endowment — once user has used the feature, locking it triggers loss aversion
- **"Your personalized plan reserved"** (Noom pattern) — endowment is virtual but feels real

**Design rule:** Whenever possible, give the user partial ownership before asking them to pay. Reverse trial > regular trial > direct paywall on this lever.

---

### 5. Peak-End Rule (Kahneman, Fredrickson, Schreiber, Redelmeier 1993)

**Citation:** Kahneman, D., Fredrickson, B. L., Schreiber, C. A., & Redelmeier, D. A. (1993). When More Pain Is Preferred to Less: Adding a Better End. *Psychological Science*, 4(6), 401–405.

**Finding:** People judge experiences by the **emotional peak** + the **ending**, not by average intensity. Famous colonoscopy study: a longer procedure with mild ending was rated less painful than a shorter procedure with sharp ending.

**Mobile paywall application:**
- **Onboarding peak** = "Your personalized plan is ready" reveal moment (Noom, Flo, Cal AI all engineer this)
- **Onboarding end** = paywall hit. If end is positive (continuity, trust, transparency), the entire onboarding is remembered positively → higher conversion
- **Loading screen bridge** between quiz and paywall converts a transition into a positive peak ("Building YOUR plan…")
- **Mid-trial value summary push** ("You've used X today") creates a positive peak before charge
- **Refund flow ending matters** — graceful refund creates a positive end → user may return later; aggressive refund denial = negative end → bad reviews

**Design rule:** Engineer at least one positive peak in onboarding (the personalized plan reveal works) AND make sure the paywall end is positive (trust, transparency, dignity). See [onboarding-paywall-handoff.md](onboarding-paywall-handoff.md).

---

### 6. Default Effect / Status Quo Bias (Kahneman, Knetsch, Thaler 1991)

**Citation:** Kahneman, D., Knetsch, J. L., & Thaler, R. H. (1991). Anomalies: The Endowment Effect, Loss Aversion, and Status Quo Bias. *Journal of Economic Perspectives*, 5(1), 193–206.

**Finding:** People disproportionately stick with whatever the default is. Organ donation rate by country: ~**86% in opt-out countries** vs. **~4% in opt-in countries** — same population, only the default flipped.

**Mobile paywall application:**
- **Pre-selected annual plan** is the single highest-leverage UX choice on a multi-plan paywall
- **"Most popular" badge** biases toward that tier (default by social signal)
- **Auto-renewal as default** (Apple defaults this) — must be transparent, but the bias works for you
- **Family plan as default** for Family-eligible products
- **Annual auto-renewal** vs monthly auto-renewal — anchor LTV-positive plan as default

**Design rule:** Always have a default selected. The default is what 50%+ of System-1 users will accept without thinking. Choose it deliberately for LTV.

---

### 7. Mental Accounting (Thaler 1980, building on Kahneman)

**Citation:** Thaler, R. H. (1980). Toward a Positive Theory of Consumer Choice. *Journal of Economic Behavior & Organization*, 1(1), 39–60. Then formalized in Thaler (1985, 1999). Built on Kahneman's prospect theory foundation.

**Finding:** People categorize money into mental "accounts" — daily expenses, monthly bills, entertainment, savings, "found money." The **same dollar feels different depending on which account** the brain assigns it to.

**Mobile paywall application:**
- **"$0.16/day"** = daily-expense account → low friction (compares to coffee, snack)
- **"$59/year"** = annual-investment account → high friction (compares to gym membership, insurance)
- Same total cost, different mental account = different decision
- **Per-week framing** ("$1.15/week") for annual sits between — easier than yearly, more committal than daily

**Design rule:** Choose your subordinate framing based on which mental account you want the price to land in. Apple Rule: actual billed amount must dominate visually, but the subordinate per-day or per-week framing is psychologically loaded.

---

### 8. WYSIATI — What You See Is All There Is (Thinking, Fast and Slow, 2011)

**Citation:** Kahneman (2011), *Thinking, Fast and Slow*, Ch. 7.

**Finding:** System 1 makes confident judgments based **only on visible information**. Unseen ≠ uncertain to the brain; unseen = doesn't exist. The brain doesn't compute "what am I missing?" — it acts on what's in front of it.

**Mobile paywall application:**
- **Above-fold rules become scientifically grounded.** Anything below the scroll fold effectively doesn't exist for the conversion decision.
- **Hidden trial terms = surprise charge = refund.** User did not process them, so they "didn't exist" until billing hit.
- **Hidden Restore Purchase = duplicate charges + 1-star reviews.** Same logic.
- **The strongest argument for Apple Rule "billed amount most prominent"** — what's visible IS the entire decision input.

**Design rule:** Treat anything below the fold as nonexistent for the conversion decision. If it must exist, surface it above. If it can't be above, it shouldn't gate the decision.

---

### 9. Substitution Heuristic (Thinking, Fast and Slow, 2011)

**Citation:** Kahneman (2011), *Thinking, Fast and Slow*, Ch. 9.

**Finding:** When asked a hard question, the brain unconsciously **substitutes an easier question** and answers that instead — without noticing the substitution.

**Mobile paywall application:**
- **Hard question:** "Will this app deliver $59/yr of value to me over 12 months?"
- **Brain substitutes:** "Do I trust this app right now?"
- → **Social proof, brand consistency, authority signals matter MORE than feature lists**
- → Explains why Cialdini's Social Proof + Authority test as the most-influential principles in mobile commerce (Springer 2024)
- → Explains why brand-consistent paywalls (Duolingo) outperform off-brand ones

**Design rule:** Don't try to convince the user that your feature list is worth the price (System 2 task they won't do). Instead, build trust signals that answer the substituted question (System 1 task they will do automatically).

---

### 10. Planning Fallacy (Kahneman & Tversky 1979)

**Citation:** Kahneman, D., & Tversky, A. (1979). Intuitive Prediction: Biases and Corrective Procedures. *TIMS Studies in Management Science*, 12, 313–327.

**Finding:** People consistently underestimate how long tasks will take and how hard they'll be. Best-case scenarios feel more likely than they are.

**Mobile paywall application:**
- **"7-day trial" feels like ample time** to evaluate → user signs up confident they'll cancel if not satisfied → many forget
- **"Cancel anytime"** overpromises future self-discipline
- This is WHY trials work even though many users forget to cancel — they sign up underestimating the friction of remembering to cancel
- **Trial Timeline (Blinkist)** addresses planning fallacy honestly: shows the calendar, builds trust, paradoxically increases trial signups (+23%)

**Design rule:** Honest disclosure (Trial Timeline) reduces refunds without reducing signups, because planning fallacy still works in your favor. Don't fight the bias; just be transparent about it.

---

### 11. Hedonic Adaptation (Kahneman, Diener & Schwarz 1999)

**Citation:** Kahneman, D., Diener, E., & Schwarz, N. (Eds.) (1999). *Well-Being: The Foundations of Hedonic Psychology.* Russell Sage Foundation.

**Finding:** People adapt to new conditions (positive or negative) faster than they expect. Lottery winners and accident victims both return toward baseline happiness within months.

**Mobile paywall application:**
- **Reverse trial works because user adapts to premium quickly** — the premium becomes their new baseline → losing it triggers loss aversion (concept #1)
- **Don't promise lasting happiness in copy** — "you'll be transformed" overpromises and triggers refund disappointment
- **Habit-forming features** anchor the new baseline (streak counters, daily reminders) — habit becomes the thing they can't lose

**Design rule:** Build features that become user habits in the first week. The faster the habit forms, the harder the loss aversion hits at trial end.

---

## Summary Table: Kahneman Concept → Paywall Design Choice

| Kahneman concept | Direct paywall lever |
|------------------|---------------------|
| Prospect Theory / Loss Aversion | Loss-frame trial expiry, "don't lose your progress" |
| Anchoring | Strikethrough higher price; show premium tier first |
| System 1 / System 2 | Above-fold simplicity; pre-selected default |
| Endowment Effect | Reverse trial; free preview before paywall |
| Peak-End Rule | Personalized-plan reveal moment; positive paywall ending |
| Default Effect | Pre-select annual plan; "Most popular" badge |
| Mental Accounting | Per-day framing for annuals (low-friction account) |
| WYSIATI | Above-fold rules; trial terms must be visible |
| Substitution Heuristic | Trust signals beat feature lists |
| Planning Fallacy | Trial Timeline (transparency without losing conversion) |
| Hedonic Adaptation | Habit-forming features in week 1 of trial |

---

## Other Academic Foundations

### Tversky & Kahneman (1981) — Framing Effect (Specific Paper)
**Citation:** Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211(4481), 453–458. **17,000+ citations.**
**URL:** https://www.science.org/doi/10.1126/science.7455683

**Finding:** The same factual problem produces different choices when framed as gain vs. loss. (Specific empirical paper that operationalized prospect theory's loss aversion.)

**Mobile paywall application:**
- "Save $40/year by going annual" (gain frame) vs. "Lose $40 if you stay monthly" (loss frame)
- Trial-end framing: "Don't lose your progress" (loss) vs. "Keep your progress" (gain)
- **Caveat:** Direct mobile A/B data on gain vs. loss frames in paywalls is limited. Lab effect doesn't always transfer cleanly to mobile context. Test in your own app.

---

### Anderson & Simester (2003) — $9 Endings
**Citation:** Anderson, E. T., & Simester, D. I. (2003). Effects of $9 price endings on retail sales: Evidence from field experiments. *Quantitative Marketing and Economics*, 1, 93–110.

**Finding:** Catalog field experiment — same shirt at $39 outsold the same shirt at $34. The $9 ending lift exists even when the price is higher. Authors attribute to **left-digit anchoring**.

**Mobile application:** Use $X.99 pricing where store/category convention allows. Caveat: App Store auto-pricing tiers in many regions force $X.99 by default, so the lift may already be baked in.

---

### Thomas & Morwitz (2005) — Left-Digit Effect
**Citation:** Thomas, M., & Morwitz, V. (2005). Penny wise and pound foolish: The left-digit effect in price cognition. *Journal of Consumer Research*, 32(1), 54–64.

**Finding:** Consumers encode prices left-to-right. "$9.99" anchors on "9", not interpolated to "$10". The brain compresses cents into noise.

**Mobile application:** $9.99 reads as "nine-something" not "ten". This is why $9.99 outperforms $10 even though the dollar difference is trivial. Same logic: $39.99 vs $40.

---

### Ariely (2008) — Decoy Effect (Asymmetric Dominance)
**Source:** Predictably Irrational, Ch. 1 — The Economist subscription experiment (n=100 MIT students)

| Option | Without decoy | With decoy |
|--------|---------------|------------|
| Online only ($59) | 68% | 16% |
| Print only ($125) | — | 0% (decoy) |
| Print + Online ($125) | 32% | 84% |

**Finding:** Adding a clearly inferior third option ($125 print only — same price as combo) shifted preference toward the combo by ~52pp. ~30% revenue increase from decoy presence.

**Mobile application:** Tinder's 7-day Passport at the same price as 7-day Plus is a decoy that makes Plus look like the better deal.

**Caveat:** Replication studies with real (non-hypothetical) money show weaker effect. Use as **Operator Insight** — design with the decoy logic in mind, but don't bank on a 30% lift.

---

### Cialdini (1984, 2016) — 7 Principles of Influence

**Source:** Cialdini, R. B. (1984). *Influence: The Psychology of Persuasion.* Plus *Pre-Suasion* (2016) added Unity (7th).

| # | Principle | Mobile paywall expression | Strength (mobile, Springer 2024) |
|---|-----------|---------------------------|----------------------------------|
| 1 | Reciprocity | Free trial, free preview, free core | Significant |
| 2 | Commitment & Consistency | Long onboarding quiz, "your reserved plan" | Significant |
| 3 | Social Proof | User counts, ratings, "Most popular" badges | **Most influential** |
| 4 | Authority | Expert endorsements, doctor recommendations, academic citations | **Most influential** |
| 5 | Liking | Personalized greetings, brand voice, mascot | Significant |
| 6 | Scarcity | Countdown timers, "limited offer" | Least but still significant |
| 7 | Unity | "Built for runners by runners" | Emerging research |

**Source:** Springer 2024 mobile-app persuasion study — https://link.springer.com/chapter/10.1007/978-3-031-59465-6_17

**Mobile takeaway:**
- **Social Proof + Authority** are the strongest persuaders in mobile commerce contexts. Lead with these.
- **Scarcity** still works but must be real (Apple Rule on misleading marketing — fake countdowns get rejected).
- **Commitment** lever is uniquely powerful in long-onboarding apps (Noom, Flo, Cal AI).

---

## Mobile-Specific Pricing Patterns

### Anchor Pricing

**Concept:** A higher reference price makes the target price look like a deal.

**Examples:**
- Calm: monthly £14.99 strikethrough → annual at £39.99 (~£3.33/month) feels cheap
- Strava: monthly $11.99 ($143.88/year math) → annual $79.99 = ~44% "savings"
- ChatGPT: Enterprise $30/seat → Plus $20 looks accessible

**Mobile rule:**
- Show both prices (anchor + target)
- Anchor must be a real product or honest baseline (Apple Rule)
- Don't fabricate "list prices" that never existed

---

### Decoy Pricing

**Concept:** A clearly inferior option steers users toward the target.

**Mobile examples:**
- Tinder: 7-day Passport priced equal to 7-day Plus → Plus is a no-brainer
- 3-tier paywalls where the middle tier is the decoy
- Annual-only-with-trial pattern as intentional decoy ("annual is the only way to get the trial")

**Caution:** A/B data on decoys in mobile paywalls is sparse. Don't bank on 30% lift from Ariely's catalog test transferring to your in-app subscription screen.

---

### Charm Pricing ($X.99)

**Why it works:** Left-digit effect (Thomas & Morwitz 2005) + cognitive heuristic.

**Mobile reality:**
- App Store auto-pricing tiers default to charm prices in most regions ($0.99 / $1.99 / $4.99 etc.)
- Manual pricing within those tiers usually still respects the convention
- Charm pricing lift is **already priced in** for most mobile apps

**When to break the pattern:**
- High-end / luxury positioning ($60 sounds more premium than $59.99)
- B2B / enterprise context
- Bundle / decoy pricing where the round number is the anchor

---

### Per-Day Framing

**Concept:** Annual price ÷ 365 = small daily number that feels low-friction.

**Examples:**
- $59.99/year = "$0.16/day" or "less than your daily coffee"
- $99/year = "$0.27/day"

**Apple Rule (3.1.2(c)):** Per-day framing is allowed but **the actual billed amount must be the most prominent pricing element**. Per-day breakdown must be subordinate visually.

**Tested patterns:**

```
[Large] $59.99/year
[Small] just $0.16/day · billed annually
```

---

### PPP / Geo Pricing

**Concept:** Price differently by purchasing power across markets.

**Adapty 2026 H&F data:**
- 4.4x pricing variance across markets (DE/JP/CH high; TR/IN/ID low)
- EU apps charge 29–39% more than NA on average
- IN/SEA RLTV is ~46% of NA on annual

**Implementation options:**

| Approach | Pros | Cons |
|----------|------|------|
| App Store auto-tier ("Store rules") | Zero maintenance, charm prices automatic | Same price across all of EU = leaving money on the table |
| Manual per-territory pricing | Capture EU surplus, optimize emerging markets | More setup, must update with FX shifts |
| Geo-tier (separate SKU per region) | Like ChatGPT Go @ $8 for India | Engineering complexity, App Store SKU management |

**Recommendation (Operator Insight):** Manual per-territory for top 5 revenue markets; auto-tier for the rest. Re-review annually.

---

### Trial Length Strategy

**RevenueCat 2026 data (large_scale_report):**

| Trial length | Trial-to-paid median |
|-------------|---------------------|
| ≤4 days | 25.5% |
| 5–9 days | 37.4% |
| 10–16 days | (mid-range) |
| 17–32 days | 42.5% |

**Counter-data:** longer trials = more cancellations before reaching paid (more time to forget / cancel). Math is non-linear.

**Cancellation by Day 0:**
- 3-day trial: 55.4% cancel Day 0
- 7-day trial: 39.8% cancel Day 0

**Operator Insight (Adapty 2026):** 7-day trial is the most balanced default. 3-day = aggressive (more conversions but more refunds). 30-day = high LTV per paid user but slow to monetize.

**Category exception:**
- Gaming: 73% use ≤4 day trials (fast value moment)
- H&F: 54% use 5–9 day trials
- Productivity/Lifestyle: trial can hurt LTV (direct buyers more valuable per RC)

---

### Trial-on-Annual-Only

**Concept:** Offer the free trial only on the annual plan; weekly/monthly are direct-to-paid.

**Adapty Operator Insight:** "One of the most consistent patterns" — prevents trial subsidizing the lowest-value (weekly) subscribers.

**Math:** A trial-acquired weekly subscriber retains 5.5% at D380 (Adapty). A trial-acquired annual: 19.9%. So the trial ROI is ~4x better for annual.

**Caveat:** No isolated A/B published. Adopt as default unless your data shows otherwise.

---

### Reverse Trial

**Concept:** Full premium access for N days, then revert to free.

**RevenueCat Operator Insight:** Recommended for low-intent users. Different from a StoreKit free trial — the app manages it.

**Use cases:**
- Users who installed but haven't engaged with premium features
- Apps where value compounds over time (analytics, fitness progress)
- Apps where exposure to premium changes intent (most don't know what they're missing)

**Apple Rule:** This is NOT a free trial in the StoreKit sense. Don't claim "free trial" if you mean reverse trial. Use language like "Premium experience for 7 days, then continue with Free."

---

### The Hollow Middle (2026 Phenomenon)

**Concept:** The $5–$10/month tier is dying. **41% of consumers report subscription fatigue** (Adapty 2026). Users now want either a **clear deal** (cheap or free) OR a **clear premium** (expensive with measurable outcome). Mid-priced apps without strong differentiation are squeezed from both sides.

**Implication for tier design:**
- Don't price your "main" tier in the $5–$10/mo dead zone unless it has a clear job-to-be-done
- The "good / better / best" structure now resembles "free / mid-anchor / premium-power-user" — the mid acts as decoy, not target
- 2026 winners push toward **$30+/mo for measurable outcomes** (Cal AI, ChatGPT Plus, Headspace Plus tier)
- Or push toward **$5/wk + free tier** (gaming, casual utilities, AI companions)
- Tiered pricing increases revenue **25–40%** vs single-tier — but only if tiers are clearly differentiated (Adapty)

**Cross-reference:** Decoy effect (Ariely) explains why a mid-tier still helps even when nobody buys it — frames the premium as obvious value.

**Source:** Adapty 2026 tiered pricing analysis (https://adapty.io/blog/tiered-pricing/)

---

### Apple Small Business Program — Free LTV Boost

**Apple Rule:** If your annual revenue across all your apps is **under $1M**, you qualify for the Small Business Program — **15% commission instead of 30%**.

**Math:** Switching from 30% to 15% = **+17.6% net ARPU** (price stays same, you keep more).

**Applies to:**
- New subscriptions
- Renewals
- All in-app purchases

**Doesn't apply to:**
- Apps already over $1M (you can't downgrade in)
- Year 1 of subscriptions outside SBP territory (year 2+ subs already at 15%)

**Apply at:** https://developer.apple.com/app-store/small-business-program/

**No reason not to enroll if eligible.** This is the highest-leverage zero-effort change available to indie devs.

---

### Discount Strategy

**Adapty 2026:** 90% of subscriptions sell at full price. Discounts work for **recovery, not as default**.

| Use case | Depth | Window | Risk |
|----------|-------|--------|------|
| Onboarding paywall | 0% (full price) | — | Low — preserves anchor |
| Post-close offer | 20–30% | 24h | Low LTV risk |
| Win-back (lapsed) | 30–50% | One-time | Medium — LTV erosion |
| Aggressive win-back | 50%+ | One-time | High — train discount expectation |

**Apple Rule:** Discount must reference a real higher price (no fictional "list price"). "Save 50%" requires both prices to be real and current.

---

## Common Mistakes

| Mistake | Why bad | Fix |
|---------|---------|-----|
| Per-week price larger than billed amount | Apple Rule violation (3.1.2(c)) | Make billed amount most prominent |
| "Save 75%" without anchor | Misleading marketing (Apple Rule) | Show reference price |
| Charm price on luxury positioning | Cheapens brand | $60 reads more premium than $59.99 |
| Auto-pricing in EU + IN with same SKU | Leaving money on the table in EU; pricing IN out of reach | Manual per-territory pricing |
| 30-day trial for impulse-buy app | Long trial = more cancellations | Match trial length to category |
| Trial on weekly + monthly + annual | Weekly trial subscribers don't retain | Trial on annual only |
| Decoy that's actually preferred by some users | Decoy must be clearly inferior | Make decoy obviously worse on price OR features |

---

## Source Pointers

- Tversky & Kahneman 1981 — https://www.science.org/doi/10.1126/science.7455683
- Anderson & Simester 2003 — Quantitative Marketing and Economics
- Thomas & Morwitz 2005 — Journal of Consumer Research
- Ariely Decoy — https://thestrategystory.com/2020/10/02/economist-magazine-a-story-of-clever-decoy-pricing/
- Cialdini Influence — https://www.cognitigence.com/blog/cialdini-7-principles-of-persuasion
- Springer 2024 mobile persuasion study — https://link.springer.com/chapter/10.1007/978-3-031-59465-6_17
- Adapty State 2026 — https://adapty.io/state-of-in-app-subscriptions/
- RevenueCat State 2026 — https://www.revenuecat.com/state-of-subscription-apps/
- Apple Review Guidelines — https://developer.apple.com/app-store/review/guidelines/
