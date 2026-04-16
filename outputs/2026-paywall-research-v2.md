# 2026 Paywall Research v2 — Additional Behavioral Foundations

**Date:** 2026-04-16
**Purpose:** Layer 2 of academic foundations for app-paywall-pilot, expanding beyond the Kahneman base added in v3.7.0. Each concept verified for primary citation, scrutinized for replication evidence, and mapped to a specific paywall design rule.
**Method:** WebSearch + WebFetch on primary sources (peer-reviewed journals, foundational books). Skeptical handling of contested findings.

---

## Executive Summary

This brief verifies and curates 12 additional behavioral-science concepts for paywall design. **Nine are academic-strong** (peer-reviewed, well-replicated); **one (ego depletion) failed multi-lab replication and is included with explicit caveat**; **two (Hooked Model, Atomic Habits identity) are practitioner frameworks** and labeled as such — not academic foundations.

The standout finding is the **replication failure of ego depletion** (Hagger et al. 2016 multi-lab; Vohs et al. 2016) [9][10]. The simple "willpower depletes like fuel" model is no longer scientifically defensible. The practical paywall rule (keep paywalls cognitively simple) still stands — but the underlying mechanism is **Choice Overload (Iyengar & Lepper 2000)** [3] and **System 1 cognition (Kahneman 2011)** [v3.7.0 module], not ego depletion.

The strongest additions for the skill are: **Choice Overload** (direct evidence for 2-3 plans), **IKEA Effect** (scientific basis for personalization in onboarding), **Goal-Gradient** (progress bars accelerate behavior), **Hyperbolic Discounting** (why weekly impulse > annual commitment in the moment), and **Negativity Bias** (refunds and 1-star reviews weigh disproportionately).

---

## Section 1 — Academic-Strong Foundations

### 1.1 BJ Fogg Behavior Model (B = M·A·T)

**Citation:** Fogg, B. J. (2009). A behavior model for persuasive design. *Proceedings of the 4th International Conference on Persuasive Technology*, Article 40, 1–7. ACM. [1]
**Status:** Conference paper; **1,900+ academic publications reference the Fogg model** [1]. More design framework than experimental finding, but widely operationalized.

**Finding:** For a behavior to occur, three elements must converge **simultaneously**:
- **Motivation** (sensation, anticipation, social cohesion)
- **Ability** (time, money, physical effort, brain cycles, social deviance, non-routine)
- **Trigger** (cue / prompt at the moment of decision)

If any element is at zero, the behavior doesn't happen — and you can compensate for low motivation by reducing ability friction.

**Paywall design rule:**
- **Motivation = your copy + onboarding affect.** Outcome-led headlines, real social proof.
- **Ability = paywall friction.** Pre-selected default, one-tap purchase via Apple Pay / Google Pay, no scroll required for the decision, no math.
- **Trigger = placement.** Post-aha moment, contextual feature-gate, transaction-abandon prompt.

**Implication:** When motivation is borderline (low-intent user), don't try to raise motivation with more copy — **reduce ability friction**. Pre-select annual, 1-tap purchase, no signup required.

### 1.2 Choice Overload — Iyengar & Lepper Jam Study

**Citation:** Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating: Can one desire too much of a good thing? *Journal of Personality and Social Psychology*, 79(6), 995–1006. [2][3]
**Status:** Three experimental studies. Foundational paper. **Effect direction validated; effect size has been challenged in meta-analyses** (Scheibehenne, Greifeneder, Todd 2010). Principle stands; magnitude depends on context.

**Finding (jam study specifically):** Gourmet jam display in a real supermarket:
- **24-jam display:** 60% of passersby stopped, 3% bought
- **6-jam display:** 40% stopped, **30% bought**
- → 6-option display generated **~10x the purchase conversion** of 24-option

**Across all 3 studies:** participants given limited choice reported greater satisfaction with their selections than those given extensive choice [2][3].

**Paywall design rule:**
- **2–3 plans is the sweet spot.** Match RC 2026 vendor data: 41–60% of apps use 2 plans; 27% of Travel apps use 3+. Beyond 3, hide behind "More plans" disclosure.
- This explains why **Calm's single-plan paywall works** (zero choice = zero overload) and why **Tinder's 3-tier ladder works** (choice within a manageable set).
- **Caveat:** the 2010 meta-analysis by Scheibehenne et al. found near-zero average effect across 50+ studies, suggesting choice overload depends heavily on context (product category, decision difficulty, user expertise). Don't expect Iyengar's 10x lift in your A/B test; expect a directional benefit only.

### 1.3 IKEA Effect — Norton, Mochon, Ariely

**Citation:** Norton, M. I., Mochon, D., & Ariely, D. (2012). The IKEA effect: When labor leads to love. *Journal of Consumer Psychology*, 22(3), 453–460. [4]
**Status:** Four studies (IKEA boxes, origami, Lego). **Replicated** (Marsh et al. conceptual replication confirmed effect; psychological ownership identified as mediator). [4]

**Finding:** People value self-made products **as much as expert-made products**, and expect others to share that valuation. Effect dissipates if the labor fails (incomplete tasks) or if the product is destroyed — **completion matters**.

**Paywall design rule:**
- **Long onboarding = labor = ownership = higher willingness to pay.** Explains scientifically why Noom (77 screens), Flo (70 screens), and Cal AI (deep personalization + animations) all out-monetize their categories.
- **The plan must "complete"** for the effect to land — that's what the "Your personalized plan reserved" intermediate screen does. Without that completion moment, the labor was wasted.
- **Don't ship a long onboarding without a labor-payoff moment.** Failure mode: 70-screen quiz → generic paywall → user feels their effort was for nothing → trust break.

### 1.4 Hyperbolic Discounting — Laibson

**Citation:** Laibson, D. (1997). Golden Eggs and Hyperbolic Discounting. *The Quarterly Journal of Economics*, 112(2), 443–478. [5]
**Status:** Foundational behavioral-economics paper. Formalized present bias mathematically. Subsequent decades of replication across savings, addiction, health behavior research.

**Finding:** People apply a **disproportionately steep discount to future rewards**, especially for short delays — "I want it now" beats "I want more later" even when the math favors waiting. Creates **dynamically inconsistent preferences**: today you'd choose to save tomorrow; tomorrow, you spend.

**Paywall design rule:**
- **Weekly plans win on present bias.** "$5/week today" feels less than "$59/year now" even when the annual is mathematically better. Adapty 2026: weekly = 55.5% of all subscription revenue — present bias in action.
- **Trial conversions exploit present bias.** "Free now, charged in 7 days" — the future cost is hyperbolically discounted at signup.
- **Annual default + savings callout** must work HARDER than the weekly equivalent — because you're fighting the bias.
- **Per-day framing exploits present bias positively.** "$0.16/day" lands in the immediate-cost mental account → lower hyperbolic discount factor.

### 1.5 Goal-Gradient Effect — Kivetz, Urminsky, Zheng

**Citation:** Kivetz, R., Urminsky, O., & Zheng, Y. (2006). The goal-gradient hypothesis resurrected: Purchase acceleration, illusionary goal progress, and customer retention. *Journal of Marketing Research*, 43(1), 39–58. [6]
**Status:** Field experiments at a real café + online music-rating studies. Multi-method, multi-context. Robust.

**Finding:** Effort and engagement **accelerate as users approach a reward**. Specific results:
- Café customers buy coffee **more frequently** as they near the free-coffee threshold on a punch card [6]
- Internet users **rate more songs per visit** as they approach reward goals [6]
- **Illusion of progress works:** customers given a 12-stamp card with 2 free "bonus" stamps complete the 10 required purchases **faster** than customers given a regular 10-stamp card [6]

**Paywall design rule:**
- **Show progress in onboarding.** "Step 5 of 10" beats no indicator. The user accelerates toward completion.
- **"Bonus" head-start works.** "We've already done X for you — finish in just N steps" outperforms equivalent N-step quiz with no bonus framing.
- **Trial Timeline (Blinkist pattern) is a goal-gradient device.** Visualizes the path from now to billing → reduces anxiety, increases completion.
- **Loyalty/streak mechanics** (Duolingo) tap goal-gradient for retention. Day 6 of a 7-day streak triggers more app-opens than Day 2.

### 1.6 Negativity Bias — Baumeister et al. "Bad is Stronger than Good"

**Citation:** Baumeister, R. F., Bratslavsky, E., Finkenauer, C., & Vohs, K. D. (2001). Bad is stronger than good. *Review of General Psychology*, 5(4), 323–370. [7]
**Status:** Comprehensive review. **10,000+ citations** [7]. Domain-spanning consensus: bad weighs more than good in everyday events, major life events, relationships, social networks, learning, feedback.

**Finding:** When equal measures of good and bad are present, **the psychological impact of the bad outweighs the good**. Bad emotions, bad parents, bad feedback all have more impact than equivalent good. **The self is more motivated to avoid bad self-definitions than to pursue good ones.**

**Paywall design rule:**
- **A 1-star review weighs ~5x a 5-star review** in a prospective user's decision (rule of thumb derived from negativity bias literature). Reply to bad reviews; refund cleanly to prevent them.
- **Refund rate matters more than conversion rate.** A 7% refund rate damages brand and ASO more than a 30% conversion uplift compensates for.
- **Aggressive monetization = aggressive backlash.** Strava's 2025 Year-in-Sport paywalling caused brand damage disproportionate to the revenue it captured (see [teardowns.md](../modules/teardowns.md)).
- **The end of the trial / refund / cancellation experience matters disproportionately.** Smooth exits = neutral memory; aggressive exit = lasting bad memory + bad reviews.
- **Always under-promise on paywall, over-deliver in product.** Reverse triggers negativity bias instantly.

### 1.7 Costly Signaling — Spence Job Market Signaling

**Citation:** Spence, M. (1973). Job Market Signaling. *The Quarterly Journal of Economics*, 87(3), 355–374. [8]
**Status:** Nobel Memorial Prize in Economics (2001) shared by Spence for this signaling work. **14,759 citations** per Semantic Scholar [8]. Foundational microeconomics.

**Finding:** When the buyer can't directly verify quality, they use **costly signals** — observable attributes that cost the seller something to provide and which would not be worth providing if quality were low. Education in the original paper; pricing, brand investment, certifications in derivative literature.

**Paywall design rule:**
- **Premium pricing IS a quality signal.** Adapty 2026: high-priced apps earn **3x the LTV** of low-priced apps. Some of that effect is selection (premium-aware users), but signaling theory says some of it is genuine quality inference: "if it costs more, it must be better."
- **Don't undercharge in your category.** A meditation app at $1.99/mo signals low quality vs Calm's $69.99/yr — even if features are identical.
- **Brand investment signals durability.** Polished design, real testimonials, professional copy → user infers "this company can afford to invest, so they'll be around next year."
- **The Hollow Middle problem (v3.7.0)** is partly a signaling failure: $5–10/mo apps signal neither "value deal" nor "premium quality" — they're stuck between two costly-signal positions.

### 1.8 Reactance Theory — Brehm

**Citation:** Brehm, J. W. (1966). *A Theory of Psychological Reactance.* Academic Press. [11]
**Status:** Foundational. **50+ years of replication** across health, marketing, politics, education domains [11]. Reviewed in Steindl et al. (2015) Springer Nature.

**Finding:** When people perceive their **freedom to choose** is being threatened or removed, they become motivated to **restore that freedom** — often by doing the opposite of what's being pushed. "You can't have this!" → "Watch me have this."

**Paywall design rule:**
- **Fake urgency backfires.** Countdown timers that aren't real, "limited time" that isn't, "last chance" repeated weekly — all trigger reactance. User dismisses the paywall AND doesn't return.
- **"You must subscribe to continue" hard paywalls trigger reactance** in users who haven't experienced enough value yet. Hard paywall works WHEN value is established (post-aha placement); fails when applied too early.
- **Always offer a dignified way out.** "Maybe later" decline button > "Continue with limits" guilt-trip. Users who feel they have a choice are more likely to say yes; users who feel cornered fight back.
- **Don't show the same paywall 3 times in a session.** Aggressive re-prompting triggers reactance + Apple compliance flag for "aggressive monetization."
- **Apple's toggle paywall ban (Jan 2026)** can be partly explained as Apple protecting users from reactance: the toggle felt like a forced default, triggering long-term resentment toward the App Store ecosystem.

### 1.9 Sunk Cost Fallacy in Onboarding (Concept-level academic, app-specific operator)

**Concept citation:** Arkes, H. R., & Blumer, C. (1985). The psychology of sunk cost. *Organizational Behavior and Human Decision Processes*, 35(1), 124–140. [12]
**Status:** Foundational paper on sunk cost. Concept widely accepted in academic literature; specific application to mobile onboarding is operator/UX-level.

**Finding (academic):** People irrationally continue commitments based on past investment ("I've already paid for the ticket, so I have to use it") even when continuing is no longer rational. Strongest when the investment is recent and visible.

**Paywall design rule:**
- **Long onboarding creates sunk-cost commitment** that flows into paywall conversion. After 7 minutes of quiz, abandoning at the paywall feels like wasting that time.
- **This compounds with IKEA Effect** — labor + ownership + sunk cost stack to maximize willingness to pay at the paywall moment.
- **Visible progress bar amplifies sunk cost** — user sees how much they've already invested.
- **But: Goal-Gradient Effect (1.5) suggests they accelerate toward completion when near the end.** So sunk cost is not "burden the user with effort"; it's "make completion feel close while the investment piles up."

---

## Section 2 — Contested Evidence (Use With Caveats)

### 2.1 Ego Depletion / Decision Fatigue — Baumeister

**Original citation:** Baumeister, R. F., Bratslavsky, E., Muraven, M., & Tice, D. M. (1998). Ego Depletion: Is the Active Self a Limited Resource? *Journal of Personality and Social Psychology*, 74(5), 1252–1265. [9]
**Replication failures:**
- Hagger et al. (2016) multi-lab replication: **2,141 participants, 24 labs worldwide. No evidence for ego depletion found.** [10]
- Vohs et al. (2016) pre-registered multi-lab replication: **3,531 participants, 36 labs. No effect found.** [10]

**Status:** **The simple "willpower depletes like fuel" model is no longer tenable.** Ego depletion was a central case in psychology's replication crisis [9][10].

**What still stands:**
- Choice Overload (1.2) explains why fewer plans convert better — without invoking depleted willpower
- System 1 / System 2 (Kahneman 2011) explains cognitive economics — backed by 40 years of evidence
- The practical UX rule "keep paywalls simple" is correct; the mechanism is **Choice Overload + WYSIATI + System 1**, not ego depletion

**Paywall design rule (corrected):**
- ✅ Keep paywalls cognitively simple (1–3 plans, pre-selected default, no math required) — backed by Choice Overload + System 1
- ❌ Don't use "decision fatigue" as a mechanism explanation in v3.x+ skill content. Use Choice Overload (Iyengar & Lepper 2000) instead.
- ❌ Don't justify discounts as "the user is too tired to evaluate price" — no evidence base.

---

## Section 3 — Practitioner Frameworks (Not Academic Foundations)

These are useful operational frameworks but lack peer-reviewed empirical foundations comparable to Sections 1 and 2.1. Label as **Operator Insight**, not academic.

### 3.1 Hooked Model — Nir Eyal

**Source:** Eyal, N. (2014). *Hooked: How to Build Habit-Forming Products.* Portfolio. [13]
**Status:** **Practitioner book, not peer-reviewed research.** Wall Street Journal best seller. Synthesizes existing academic findings (variable rewards from Skinner, sunk cost, etc.) into a 4-step product framework.

**Framework:** Trigger → Action → Variable Reward → Investment, in a recurring loop [13].

**Paywall application:**
- **Trigger** (external: push, email; internal: emotion / habit) — placement of paywall in user's existing trigger pattern
- **Action** (low friction) — Fogg's Ability lever + Apple Pay / Google Pay
- **Variable Reward** — Skinner-derived; explains why streak counters and gamified achievements aid retention beyond the paywall
- **Investment** — the user's data, customizations, history that increase switching cost; this is also IKEA Effect (1.3) + Sunk Cost (1.9)

**Caveat:** The Hooked framework is operational synthesis, not validated theory. Cite the underlying academic foundations (variable reward = Skinner; investment = IKEA / sunk cost) when you want academic grounding.

### 3.2 Atomic Habits — James Clear

**Source:** Clear, J. (2018). *Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones.* Avery. [14]
**Status:** **Bestseller, not peer-reviewed research.** Synthesizes Fogg's Behavior Model, habit-loop research, and identity psychology into a popular framework.

**Identity-based behavior change concept:** Lasting change depends on who you believe yourself to be, not what you want to achieve. "I am a runner" beats "I want to run a marathon" [14].

**Paywall application:**
- **Identity-led headlines:** "Become the runner you want to be" (#2 in copy-library headline formulas) is identity-led — links the subscription to who the user wants to be, not what they want to do
- **Onboarding identity choice:** "Are you training for: Speed / Distance / Recovery?" defines an identity the user is now committed to (Cialdini commitment + identity)
- **Lifetime "X-er" framing in retention:** "You've been a Runner with us for 12 months" reinforces identity → reduces churn

**Caveat:** Identity-based framing has academic backing through Bem's self-perception theory (Bem 1972) and Cialdini's commitment & consistency. Cite those for academic grounding; cite Clear/Atomic Habits as the popular operationalization.

---

## Section 4 — Open Questions / Unresolved

1. **Choice Overload meta-analysis controversy.** Scheibehenne, Greifeneder, & Todd (2010, *Journal of Consumer Research*) meta-analyzed 50+ studies and found **near-zero average effect size**. Subsequent studies show effect depends heavily on context (product category, expertise, decision difficulty). Don't expect Iyengar's 10x lift in your A/B; expect a directional benefit at most.

2. **Is the Fogg Behavior Model falsifiable?** B = M·A·T is a framework that explains everything post-hoc. No prediction would falsify it. Useful for design thinking; weak as a scientific claim.

3. **Identity-based habits empirical support.** Clear's framework is intuitive and partially backed by Bem and Cialdini, but no rigorous A/B exists comparing identity-led vs goal-led copy in mobile paywalls. Treat as Hypothesis, not Vendor Aggregate Data.

4. **Hooked Model retention claim.** Eyal claims habit-forming products dominate; the underlying evidence is observational (top-grossing apps DO have these patterns) but causal direction is unclear (do hooks make apps successful, or do successful apps adopt hooks?).

5. **Negativity bias magnitude in mobile reviews specifically.** "1-star weighs 5x 5-star" is a rule-of-thumb derived from general literature, not a measured mobile-app-specific finding. Likely directionally correct; magnitude uncertain.

6. **Goal-Gradient bonus stamps in subscription onboarding.** Kivetz et al. proved the effect for purchase acceleration; whether the same effect transfers to onboarding-quiz completion is plausible but unmeasured.

---

## Section 5 — Updated Evidence Hierarchy

For inclusion in skill modules:

| Concept | Evidence class | Paywall relevance |
|---------|---------------|-------------------|
| Fogg B=MAT | academic (1,900+ pubs ref) | High — direct paywall mapping |
| Choice Overload (Iyengar 2000) | academic, with caveat | High — direct plan-count rule |
| IKEA Effect (Norton 2012) | academic, replicated | High — onboarding personalization |
| Hyperbolic Discounting (Laibson 1997) | academic, foundational | High — weekly vs annual psychology |
| Goal-Gradient (Kivetz 2006) | academic, field-validated | High — progress bars + bonus stamps |
| Negativity Bias (Baumeister 2001) | academic, 10K+ citations | High — refund rate strategy |
| Costly Signaling (Spence 1973) | academic, Nobel | High — premium pricing as quality signal |
| Reactance Theory (Brehm 1966) | academic, 50+ yrs replication | High — anti-pattern justification |
| Sunk Cost (Arkes & Blumer 1985) | academic foundational + operator app | Medium — onboarding effort dynamics |
| **Ego Depletion (Baumeister 1998)** | **REPLICATION FAILED — exclude as mechanism** | Use Choice Overload instead |
| Hooked Model (Eyal 2014) | practitioner framework | Medium — operator framework, cite underlying acads |
| Atomic Habits identity (Clear 2018) | practitioner framework | Medium — operator framework, cite Bem/Cialdini |

---

## Sources

[1] Fogg, B. J. (2009). A behavior model for persuasive design. *Proceedings of the 4th International Conference on Persuasive Technology*. ACM. — https://behaviordesign.stanford.edu/resources/fogg-behavior-model
[2] Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating: Can one desire too much of a good thing? *Journal of Personality and Social Psychology*, 79(6), 995–1006. — https://faculty.washington.edu/jdb/345/345%20Articles/Iyengar%20&%20Lepper%20(2000).pdf
[3] PubMed entry — https://pubmed.ncbi.nlm.nih.gov/11138768/
[4] Norton, M. I., Mochon, D., & Ariely, D. (2012). The IKEA effect: When labor leads to love. *Journal of Consumer Psychology*, 22(3), 453–460. — https://myscp.onlinelibrary.wiley.com/doi/abs/10.1016/j.jcps.2011.08.002
[5] Laibson, D. (1997). Golden Eggs and Hyperbolic Discounting. *The Quarterly Journal of Economics*, 112(2), 443–478. — https://academic.oup.com/qje/article-abstract/112/2/443/1870925
[6] Kivetz, R., Urminsky, O., & Zheng, Y. (2006). The goal-gradient hypothesis resurrected. *Journal of Marketing Research*, 43(1), 39–58. — https://journals.sagepub.com/doi/abs/10.1509/jmkr.43.1.39
[7] Baumeister, R. F., Bratslavsky, E., Finkenauer, C., & Vohs, K. D. (2001). Bad is stronger than good. *Review of General Psychology*, 5(4), 323–370. — https://journals.sagepub.com/doi/abs/10.1037/1089-2680.5.4.323
[8] Spence, M. (1973). Job Market Signaling. *The Quarterly Journal of Economics*, 87(3), 355–374. — https://academic.oup.com/qje/article-abstract/87/3/355/1909092
[9] Baumeister, R. F., Bratslavsky, E., Muraven, M., & Tice, D. M. (1998). Ego Depletion: Is the Active Self a Limited Resource? *Journal of Personality and Social Psychology*, 74(5), 1252–1265. — https://faculty.washington.edu/jdb/345/345%20Articles/Baumeister%20et%20al.%20(1998).pdf
[10] Hagger, M. S. et al. (2016). Multi-lab pre-registered replication of ego depletion. — https://en.wikipedia.org/wiki/Ego_depletion (summary; primary refs in Wikipedia article)
[11] Brehm, J. W. (1966). *A Theory of Psychological Reactance.* Academic Press. — https://psycnet.apa.org/record/1967-08061-000
[12] Arkes, H. R., & Blumer, C. (1985). The psychology of sunk cost. *Organizational Behavior and Human Decision Processes*, 35(1), 124–140. (Foundational paper; not directly fetched in this research pass — included from established literature.)
[13] Eyal, N. (2014). *Hooked: How to Build Habit-Forming Products.* Portfolio. — https://www.nirandfar.com/how-to-manufacture-desire/
[14] Clear, J. (2018). *Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones.* Avery. — https://jamesclear.com/wp-content/uploads/2016/05/CU-Identity-Based-Habits.pdf
