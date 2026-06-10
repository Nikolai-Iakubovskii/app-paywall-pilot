# Copy Library

Concrete copy patterns for paywall headlines, benefits, CTAs, and trust elements. Use as starting variants for testing — never ship unchanged. Every recommendation labeled by Evidence Class from SKILL.md.

---

## The Copy Ladder

Three rungs. Always climb the ladder before writing copy.

| Rung | Type | Example | When to use |
|------|------|---------|-------------|
| 1 (top) | **Outcome** | "Sleep better in 7 nights" | First-time users, broad audience, low product literacy |
| 2 | **Benefit** | "Personalized sleep stories from experts" | Mid-funnel, users who understand the problem |
| 3 (bottom) | **Feature** | "100+ sleep tracks with offline mode" | Power users, settings/upgrade screens, technical audiences |

**Rule (Operator Insight):** Adapty/RevenueCat repeatedly observe that outcome-led headlines beat feature-led for first-purchase paywalls. Switch to feature copy only when audience is sophisticated.

**Source for outcome priority:** RevenueCat "How top apps approach paywalls" + Adapty 2026 paywall guide (vendor_blog).

## Copy Compression Defaults

Most AI-generated paywall copy is too long. Start short, then add detail only when the placement needs it.

| Element | Default | Expand only when |
|---------|---------|------------------|
| Headline | 3-7 words | Category is abstract or risk-sensitive |
| Subheadline | 0-1 line | The headline cannot carry product value alone |
| Bullets | 3 bullets | Settings/upgrade screen where user asked for details |
| Bullet length | 4-8 words | Legal/trust wording requires more |
| CTA | 2-5 words | Locale or trial terms need explicit duration |
| Trust line | One compact line | Price/trial/renewal terms need separation for readability |

When auditing, do not lengthen copy that is already clear. Prefer deleting, tightening, or moving detail below the fold.

---

## Copywriting Strategy: Load, Trust, Outcome

Paywall copy is not a feature brochure. Its job is to make a subscription decision feel obvious, safe, and low-effort.

### Priority order

| Priority | What copy must do | Good signal | Bad signal |
|----------|-------------------|-------------|------------|
| 1 | Reduce cognitive load | One selected plan, one clear next action | User must compare 5 claims or calculate value |
| 2 | Build trust | Real rating, clear billing, neutral exit | Fake proof, vague "best value", hidden terms |
| 3 | State outcome | "Walk without limits" | "Premium features" |
| 4 | Prove with features | 3 supporting bullets | Long feature dump above CTA |

### Four questions the screen must answer

1. What changes for me if I continue?
2. Can I trust this app right now?
3. What will I pay, when, and how do I cancel?
4. What is the single next action?

If copy does not answer one of these, delete it or move it below the fold.

### Feature Copy Rule

Features are proof, not the pitch. Use them only when they make the outcome believable.

| Weak feature dump | Better decision copy |
|-------------------|----------------------|
| "12 characters, quests, streak shields, story chapters" | "Walk without limits" + 3 proof bullets |
| "Advanced AI tools and exports" | "Turn every meeting into searchable notes" |
| "Premium workouts and analytics" | "Train smarter every week" |

### Trust beats persuasion

When the user sees a paywall, the hard question is "Will this be worth the price?" Most users answer the easier question: "Do I trust this right now?" So prioritize:

- clear full renewal price
- real rating/review count or real authority
- visible restore, terms, privacy
- plain trial/renewal/cancel wording
- neutral close/dismiss copy

Do not replace trust with more adjectives.

---

## Headline Formulas

### 12 reusable patterns

| # | Formula | Example | Best for |
|---|---------|---------|----------|
| 1 | **Outcome + Timeframe** | "Run your first 5K in 8 weeks" | H&F, Education |
| 2 | **Identity + Outcome** | "Become the runner you want to be" | H&F, Lifestyle |
| 3 | **Problem → Relief** | "Stop counting calories. Start eating right." | H&F, Productivity |
| 4 | **Question hook** | "Tired of fad diets that don't last?" | H&F, Lifestyle |
| 5 | **Number + Promise** | "Join 12M+ on their fitness journey" | Apps with real scale |
| 6 | **Personalized "Your"** | "Your personalized 12-week plan is ready" | Post-onboarding paywalls |
| 7 | **Loss-frame** | "Don't lose your progress — keep Premium" | Renewal-risk, win-back |
| 8 | **Before/After** | "From restless to rested" | Sleep, mood, mental health |
| 9 | **Authority** | "Built with sleep doctors at Stanford" | YMYL apps |
| 10 | **Outcome + Proof** | "75% of users hit their goal in 90 days" (with source) | Established apps with real data |
| 11 | **Time-to-value** | "First insight in 60 seconds" | AI tools, productivity |
| 12 | **Reverse trial sealed** | "Keep your premium experience" | Reverse trial expiry |

**Behavioral lens:**
- #5, #9, #10 = Authority / Social Proof (Cialdini; most-influential principle in mobile per Springer 2024)
- #6 = Commitment & Consistency (Cialdini); also Endowment Effect (Kahneman, Knetsch & Thaler 1990) when paired with onboarding-built ownership
- **#7 = Loss Aversion (Kahneman & Tversky 1979 *Prospect Theory*, Econometrica, 65K+ citations)** — losses felt ~2x more than equivalent gains. Strongest pattern for renewal-risk, win-back, trial-end. **Recommended default for trial expiry copy.** See [pricing-psychology.md](pricing-psychology.md) Kahneman concept #1.
- #11 = Reciprocity (Cialdini); also Mental Accounting (Thaler) — "60 seconds" lands in the daily-time mental account, not the project-time account
- **All headlines must work for System 1** (Kahneman 2011, *Thinking, Fast and Slow*) — fast, intuitive read in under 3 seconds. If reading the headline requires conscious parsing, you've failed the System-1 test.

---

## Benefit Bullet Patterns

### Verb-led, outcome-first

| Pattern | Bad (feature) | Good (outcome) |
|---------|--------------|----------------|
| Verb + Result | "100+ workouts" | "Train smarter with adaptive plans" |
| Verb + Time | "Daily reminders" | "Build the habit in 21 days" |
| Verb + Place | "Offline mode" | "Stay on track without WiFi" |
| Verb + Audience | "Family Sharing" | "Share Premium with up to 6 family members" |

### Bullet length rule

- 3–5 bullets max (Adapty observed 5+ hurts conversion — vendor_blog)
- Each bullet ≤8 words for thumb-zone scanning
- Lead with verb when possible
- One concrete number per paywall maximum (more = noise)

### Banned bullet patterns

| Pattern | Why bad |
|---------|---------|
| "Premium [Feature]" | Generic; does not communicate outcome |
| "Get access to X" | Passive; usually weaker than an active outcome |
| "And much more!" | Vague; reduces trust |
| "Unlimited everything" | Apple may flag as misleading if not literally true |

---

## CTA Patterns

### Action + Benefit > Generic

| ❌ Generic | ✅ Action+Benefit |
|------------|------------------|
| Subscribe | Start my free week |
| Continue | Begin my journey |
| Buy Now | Unlock my plan |
| Get Premium | Try free for 7 days |
| Upgrade | Keep going Premium |

**Source:** Duolingo "Start my free week" pattern (operator) — works because it's possessive ("my") + action verb + benefit.

Do not force this pattern when it makes the button too long. On small screens, "Continue" can be acceptable if the selected plan and trust line directly above/below it make the purchase terms unmistakable.

### CTA length rule

- ≤5 words English
- ≤6 words German/French (longer translations)
- ≤4 words Russian/Polish (typical translation expansion)
- Sentence case > ALL CAPS (Apple HIG preference)

### Secondary CTA (decline)

| ❌ Manipulative | ✅ Neutral |
|----------------|-----------|
| No, I want to fail | Maybe later |
| Continue with limits | Not now |
| I'll stay basic | Skip |

**Field Report / Best Practice:** Guilt-trip decline copy correlates with rejections in practitioner reports and reduces trust. Always offer dignified opt-out.

---

## Social Proof Templates

(Cialdini: most-influential principle in 2024 mobile-app studies — Springer 2024)

**Why this works (Kahneman lens):** When the user sees your paywall, the hard question is "Will this app deliver $X of value to me over 12 months?" — a System-2 question they won't actually do. By the **Substitution Heuristic** (Kahneman 2011, *Thinking Fast and Slow* Ch. 9), the brain unconsciously swaps in an easier question: **"Do I trust this app right now?"** Social proof + authority answer that easier question instantly. This is why feature lists underperform trust signals on conversion. See [pricing-psychology.md](pricing-psychology.md) Kahneman concept #9.

### By format

| Format | Template | When |
|--------|----------|------|
| User count | "Join 12M+ runners worldwide" | When >100K users; never inflate |
| Star rating | "★★★★★ 4.8 — 200K App Store reviews" | When >4.5 and >1K reviews |
| Specific outcome | "75% of users hit their goal in 90 days*" | When you have the data; *footnote source |
| Authority | "Built with [Stanford / NHS / Mayo Clinic]" | Real partnership only |
| Press | "Featured in [TechCrunch / NYT]" | Major publication only |
| Testimonial | "—Sarah, lost 12kg in 6 months" | Real user, with consent |
| Family | "Share with up to 6 family members" | Apple Family Sharing enabled |

### Banned social proof patterns (Apple Rule risk)

- Fake user counts ("Join 1B happy users" if not true)
- Fake testimonials (made-up names + photos)
- Fake star ratings on the paywall (must be real App Store rating)
- Cherry-picked stats without footnote source

---

## Trust Block Templates

Below CTA. Always present.

### Universal trust block

```
[7-day free trial, then $59.99/year. Cancel anytime.]

Restore Purchase · Terms · Privacy
```

### With Family Sharing

```
[7-day free trial, then $59.99/year. Cancel anytime.]
[Family Sharing supported — share with up to 6 family members.]

Restore Purchase · Terms · Privacy
```

### Reverse trial / soft paywall

```
[Keep using free anytime. Premium adds [outcome].]

Restore Purchase · Terms · Privacy
```

**Apple Rule (3.1.2(c)):** Subscription duration, full renewal price, and trial terms must be clearly visible. The billed amount must be the most prominent pricing element.

---

## Weak Words And Risky Defaults

These are not literal App Store banned words. Treat them as weak defaults unless the surrounding copy makes the value and subscription terms clear.

| Word | Why | Use instead |
|------|-----|-------------|
| Premium | Generic; doesn't communicate value | Specific outcome or benefit |
| Subscribe | Transactional; activates loss-frame | "Start my [trial/plan/journey]" |
| Lock / Unlock | Implies content withholding | "Get full access to..." |
| Pay | Transactional anxiety trigger | "Continue with Premium" |
| Discount | Without anchor = noise | Specific savings vs reference |
| Free | When not actually free | "Try at no cost for 7 days" |
| Ultimate / Best | Marketing fluff | Specific outcome |
| Award-winning | Unless real award named | Cite the award name |

---

## Locale-Specific Notes

### Length expansion factors (vs English)

| Locale | Expansion | Implication |
|--------|-----------|-------------|
| German | +30–40% | Headlines need shorter source |
| French | +20–30% | CTA buttons may wrap |
| Spanish | +15–25% | Manageable |
| Russian | +10–20% expansion in chars, but Cyrillic visually denser | Test on real device |
| Japanese | -20–30% | Often shorter |
| Arabic | +5–15%, RTL flip required | Mirror entire layout |
| Chinese (Simplified) | -30–50% | Plenty of room |

### Tone & formality

| Locale | Formality default | Notes |
|--------|------------------|-------|
| EN-US | Casual ("you") | "Start your journey" |
| EN-UK | Slightly more formal | Less "amazing", more "discover" |
| DE | Formal "Sie" by default; informal "du" for younger audiences (Duolingo, Headspace use du) | Test both |
| FR | Formal "vous" almost always | "tu" risks alienating |
| ES (Spain) | "tú" for consumer apps | "usted" is rare |
| ES (LatAm) | "tú" except Argentina ("vos") | Mexico/Colombia use "tú" |
| JA | Polite form (です/ます) baseline | Casual is rare in commercial copy |
| RU | "ты" for consumer apps; "вы" for B2B/finance | Match the brand |

### Number formatting

| Locale | Format |
|--------|--------|
| EN-US | $9.99 |
| EN-UK | £9.99 |
| EU (DE/FR/ES) | 9,99 € (note comma decimal, space, suffix) |
| RU | 9,99 ₽ |
| JA | ¥1,000 (no decimals usually) |

### App Store auto-PPP vs manual

**Platform Capability:** App Store Connect can auto-localize prices to "store rules" (rounded charm prices per region) OR you can manually set per-territory prices. Manual is more control but more maintenance.

**Adapty 2026 finding:** EU apps charge 29–39% more than NA. Don't blindly auto-convert NA prices to EU — manual lift captures that surplus.

---

## Loading Screen Copy (between onboarding and paywall)

**Pattern:** "Building Your Plan" loader. Used by Noom, Flo, BoldVoice, Cal AI.

### Templates

```
Analyzing your preferences…
Building your personalized plan…
Almost ready…
```

```
Step 1: Profile created ✓
Step 2: Goals analyzed ✓
Step 3: Plan generated ⏳
```

```
Sarah, your 12-week plan is being prepared.
Based on your goals, we've matched you with the [Premium] track.
```

**Operator Insight:** No isolated A/B data published, but adopted by every major H&F app at this point. Cialdini: commitment + consistency lever — by the time the user sees the paywall, they've invested in a "their" plan.

**Anti-pattern:** Loading time longer than 3s = friction. Use animation but keep total wait under 3s.

---

## Pricing Block Copy

### Plan card patterns

```
[Most Popular]                    or   [Save 60%]
Annual                                  Annual
$59.99/year                             $59.99/year
$1.15/week                              ~$5/month
[7-day free trial]                      [vs $9.99 monthly]
```

### Savings math rules (Apple Rule)

- Show both reference and discounted price ("$9.99 → $4.99")
- Reference must be a real product or honest baseline (not fictional "list price")
- "Save X%" must equal the actual math
- "Per week" / "per day" framing is allowed but the **actual billed amount must be more prominent** (Apple Rule, 3.1.2(c))

### Per-day framing examples

```
Annual: $59.99/year — that's $0.16/day
Monthly: $9.99/month — that's $0.33/day
```

Per-day framing is psychologically powerful (small numbers reduce friction) but Apple requires the actual billed amount to dominate visually.

---

## When Copy Loses to Structure

Adapty's A/B win-rate data (vendor_blog):

| Test type | Win rate |
|-----------|---------|
| Localization | 62.3% |
| Trial structure | 59.6% |
| Plan duration | 58.7% |
| Number of plans | 57.1% |
| **Visual / copy only** | **34.6%** |

**Implication:** copy A/B is the lowest-yield test category. Localize and restructure first, polish copy last.

---

## Checklist: Before Shipping Copy

- [ ] Above-fold copy answers: what changes, why trust, what price/when, what action
- [ ] Headline is on the right rung of the Copy Ladder for this audience
- [ ] CTA is action+benefit, not generic
- [ ] 3–5 benefits max, ≤8 words each
- [ ] No weak standalone words ("Premium" alone, "Unlock", "Subscribe")
- [ ] Features prove the outcome instead of becoming the pitch
- [ ] Trust block: trial terms + billed amount + restore + terms + privacy
- [ ] Locale-specific length verified on real device
- [ ] Decline CTA is neutral, not guilt-tripping
- [ ] Social proof is real and sourced
- [ ] Savings math is verifiable
- [ ] Per-day framing (if used) is subordinate to billed amount

---

## Source pointers

- Adapty 2026 reports: https://adapty.io/state-of-in-app-subscriptions/
- RevenueCat State 2026: https://www.revenuecat.com/state-of-subscription-apps/
- Duolingo CTA pattern: https://adapty.io/paywall-library/duolingo/
- Tversky & Kahneman 1981 (loss frame): https://www.science.org/doi/10.1126/science.7455683
- Cialdini 7 principles: https://www.cognitigence.com/blog/cialdini-7-principles-of-persuasion
- Apple Review Guidelines 3.1.2: https://developer.apple.com/app-store/review/guidelines/
