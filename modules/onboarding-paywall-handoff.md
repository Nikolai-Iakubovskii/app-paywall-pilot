# Onboarding → Paywall Handoff

The continuity between onboarding promise and paywall headline is core principle 10 in SKILL.md. Mismatch = trust break = conversion loss. This module covers concrete patterns from top-revenue apps and how to wire them.

For one-off paywall teardowns, see [teardowns.md](teardowns.md). For copy patterns, see [copy-library.md](copy-library.md).

---

## The Continuity Principle

**Whatever you promised in onboarding must reappear in the paywall headline.**

Bad:
- Onboarding asks: "What's your weight loss goal?"
- Paywall headline: "Unlock Premium Features"
- Result: cognitive disconnect → trust break → low conversion

Good:
- Onboarding asks: "What's your weight loss goal?"
- Paywall headline: "Your personalized 12-week plan to lose 8 kg"
- Result: continuity → effort feels rewarded → high conversion

**Source:** Operator pattern across Noom, Flo, Cal AI, BoldVoice, Headspace. Adapty's "personalized headline 15%+ lift" claim is the quantified version of this principle.

---

## Onboarding Length: When Long Wins

### Short onboarding (1-3 screens)
- **Use when:** product value is obvious in one sentence (Calm, Strava trial signup, ChatGPT)
- Trade-off: faster install→trial but no personalization signal at paywall
- CR pattern: high install→trial, average trial→paid

### Medium onboarding (4-15 screens)
- **Use when:** you need 2-3 personalization data points (theme preference, goal, experience level)
- Trade-off: balanced; works for most categories
- Examples: Headspace, Duolingo

### Long onboarding (50-100+ screens)
- **Use when:** value is high-commitment AND personalizable (H&F, behavior change, AI calorie tracking)
- Examples: **Noom (77 screens)**, **Flo (70 screens)**, **Cal AI (deep + animations)**
- Trade-off: install→trial drops, but trial→paid jumps because of commitment + consistency lever (Cialdini)
- **Key:** every long quiz needs a "personalized plan reserved" payoff before paywall

### Decision rule

```
If LTV per converted user > $50 (annual) → long onboarding usually wins
If LTV per converted user < $20 (weekly impulse) → short onboarding wins
If LTV $20-50 → test medium length
```

---

## 7 Onboarding Patterns Linked to Paywall

### 1. Quiz → Personalized Plan → Paywall (Noom pattern)

**Flow:**
1. 50-100 quiz screens collecting goals, behavior, preferences
2. "Building your personalized plan" loader (with progress)
3. "Plan reserved" intermediate screen with summary
4. Paywall with headline matching the quiz outcome

**Paywall headline matches quiz answer:**
- Quiz: "What's your weight loss goal?" → "Lose 5 kg" selected
- Paywall: "Your personalized plan to lose 5 kg in 12 weeks"

**Best for:** H&F, Education, behavior change, AI assistants
**Real example:** Noom $17.42/mo, 77-step onboarding
**Cialdini levers:** commitment & consistency (effort), authority (science framing), unity ("for people like you")

### 2. Demo Video → Onboarding → Paywall (Cal AI pattern)

**Flow:**
1. 5-10 second demo video of app's core action
2. Short onboarding (5-10 screens, mostly visual/animated)
3. Mid-onboarding review prompt
4. "Generating your plan" loader
5. Hard paywall (card required)

**Paywall headline:** outcome-led, references the demo
- Demo showed: "Snap a photo, get calories"
- Paywall: "Track every meal in 1 second"

**Best for:** AI tools, single-action apps
**Real example:** Cal AI ($1.4M/mo profit)
**Cialdini levers:** social proof (review prompt), reciprocity (demo gives value first)

### 3. Day/Night Theme + Segment → Paywall (Headspace pattern)

**Flow:**
1. 3-5 onboarding screens identifying segment (sleep / stress / focus)
2. App selects time-of-day theme (day / night)
3. Free preview of one item per segment
4. Paywall with segment-specific copy + theme

**Paywall headline matches segment:**
- Sleep segment: "Sleep better tonight"
- Stress segment: "Calm your mind in 3 minutes"
- Focus segment: "Find your focus, every day"

**Best for:** Mindfulness, wellness apps with multiple use cases
**Real example:** Headspace $69.99/yr
**Cialdini levers:** liking (theme matches user state), commitment (segment chosen)

### 4. Goal-First Onboarding → Paywall (Duolingo pattern)

**Flow:**
1. Language selection
2. "Why are you learning?" (goal selection)
3. Daily goal commitment (5 / 10 / 15 / 20 min)
4. First lesson (free taste)
5. Paywall after first lesson with personalized headline

**Paywall headline references chosen goal:**
- Travel goal: "Speak [Language] confidently for your trip"
- Career goal: "[Language] for your next opportunity"

**Personalization at paywall:**
- First benefit bullet matches entry placement
- Family vs Individual plan selection
- CTA: "Start my free week" (possessive + outcome)

**Best for:** Education, skill-building, hobbyist apps
**Real example:** Duolingo $25M/mo

### 5. Free Tier + Aha → Soft Paywall (Strava pattern)

**Flow:**
1. Single signup screen
2. Connect Garmin / Apple Watch / phone GPS
3. First activity recorded (the aha)
4. Inline subscription CTA in main UI (NOT modal interruption)
5. 30-day free trial without credit card available

**Paywall headline:** identity-led
- "Train smarter with Strava Premium"
- Bullets: route planning, segment analysis, training plan

**Best for:** Tools where value compounds with use (fitness, productivity, photo)
**Real example:** Strava $79.99/yr

### 6. Empathy Quiz → Personalization → Soft-Sell Paywall (Flo pattern)

**Flow:**
1. 70-screen onboarding with empathetic framing
2. Personalization via name + cycle data
3. "You're not alone" empathy statements throughout
4. Free core (cycle tracking) preserved
5. Premium upsell: AI assistant, predictions, ad-free

**Paywall framing:** keeping core free signals trust → premium feels like a value-add not a wall
**Real example:** Flo $49.99/yr, $6M/mo revenue

### 7. Reverse Trial Onboarding (low-intent pattern)

**Flow:**
1. Short or no onboarding
2. Full premium activated automatically for N days
3. In-app reminders show what user is using ("You used Premium feature X today")
4. Day N-2: notification "Your Premium ends in 2 days. Keep it?"
5. Paywall with framing: "Keep your premium experience"

**Best for:** Photo, Lifestyle, Productivity (where direct buyers > trial)
**Apple Rule:** This is NOT a StoreKit free trial. Use language like "Premium experience for 7 days" not "free trial".

---

## The Loading Screen Bridge

Between onboarding completion and paywall, **always insert a loading screen**.

### Why
1. **Cialdini commitment lever** — by the time the user sees the paywall, they've waited for "their" plan to be built
2. **Anticipation builds value perception** — Noom's "Reserving your plan" feels meaningful even if it's instant
3. **Smooth transition** — avoids jarring jump from quiz → paywall

### Templates

**Variant A: Linear progress**
```
Analyzing your preferences…  ⠋
Building your personalized plan…  ⠙
Almost ready…  ✓
```

**Variant B: Step list**
```
Step 1: Profile created ✓
Step 2: Goals analyzed ✓
Step 3: Plan generated ⏳
```

**Variant C: Personalized**
```
[Name], your 12-week plan is being prepared.
Based on your goals, we've matched you with the [Premium] track.
```

### Timing rule

- **Total wait ≤3 seconds.** Longer = friction.
- **Never lie.** If your plan generation takes 0ms, the loading screen is psychological — keep it under 2s.
- **Don't fake progress for >5s.** That crosses into deception (Apple Rule risk for misleading UX).

---

## Common Handoff Mistakes

| Mistake | Fix |
|---------|-----|
| Quiz answers not referenced on paywall | Echo specific quiz answer in headline |
| Paywall says "Premium" instead of outcome | Use Outcome-led headline from [copy-library.md](copy-library.md) |
| Long onboarding then generic paywall | Personalize first benefit bullet at minimum |
| Loading screen without a payoff | Always end with "Plan ready" or similar — earn the wait |
| "Reserved plan" timer that resets every visit | Apple Rule violation (fake urgency) — make timer real or remove |
| Onboarding promise the app can't deliver | Trust break → high refund rate → bad reviews |
| Skipping personalization for non-H&F categories | Even AI tools (Cal AI, ChatGPT custom GPTs) benefit from light personalization |

---

## When NOT to Personalize

- **You don't have the data** — fake personalization is worse than none
- **Audience values speed over personalization** — gaming, news apps
- **Single-use-case product** — one feature, one user type (Tinder doesn't need quiz; the value is obvious)
- **Privacy-sensitive markets** — GDPR-anxious users may bounce on long quizzes (DE, FR specifically)

---

## Measurement: What to Track

Pre/post handoff funnel:
1. Onboarding screen completion rate per step (find drop-offs)
2. Onboarding total completion rate (% reach paywall)
3. Paywall impression → trial start rate
4. Paywall headline A/B (quiz-personalized vs generic)
5. Trial → paid conversion (does long onboarding deliver promised LTV?)

If long onboarding tanks completion >40%, shorten. If shortening tanks trial→paid more than completion gain, lengthen back.

---

## Source Pointers

- [teardowns.md](teardowns.md) — full app-by-app breakdowns (Noom, Flo, Cal AI, etc.)
- Noom long onboarding analysis: https://www.retention.blog/p/the-longest-onboarding-ever
- Cal AI onboarding deep-dive: https://adapty.io/blog/paywall-newsletter-22/
- Headspace segmentation strategy: https://subclub.com/episode/how-headspace-optimized-revenue-by-gating-content-shreya-oswal-and-keya-patel-headspace
- Adapty 2026 personalization claim (15% lift): https://adapty.io/blog/high-performing-paywall-2026/
- Cialdini 7 principles: see [pricing-psychology.md](pricing-psychology.md)
