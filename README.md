<p align="center">
  <h1 align="center">App Paywall Pilot</h1>
  <p align="center">
    <strong>Your AI copilot for designing, auditing, and shipping<br>App Store-compliant in-app paywalls.</strong>
  </p>
  <p align="center">
    <a href="#how-to-use">Get Started</a> &bull;
    <a href="#whats-inside">What's Inside</a> &bull;
    <a href="#data-sources">Data Sources</a> &bull;
    <a href="#contributing">Contributing</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Version-3.1.0-brightgreen?style=flat-square" alt="Version">
    <img src="https://img.shields.io/badge/Platform-iOS_%7C_Android-blue?style=flat-square" alt="Platform">
    <img src="https://img.shields.io/badge/Benchmarks-April_2026-green?style=flat-square" alt="Benchmarks">
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
    <img src="https://img.shields.io/github/stars/Nikolai-Iakubovskii/app-paywall-pilot?style=flat-square" alt="Stars">
  </p>
</p>

---

An AI instruction file (`SKILL.md`) that turns any LLM into a mobile subscription paywall expert.

Works with **Claude Code** &bull; **Codex** &bull; **ChatGPT** &bull; **Cursor** &bull; **Windsurf** &bull; **Gemini** -- or any AI tool that supports custom instructions.

---

## The Problem

Most paywall advice is either **generic web CRO** that ignores App Store rules, **hype-driven** single-app case studies with no methodology, or **outdated** tactics that get your app rejected by Apple in 2026.

## The Fix

App Paywall Pilot gives your AI assistant real-world paywall expertise:

| Principle | How |
|-----------|-----|
| **Compliance first** | Every recommendation checked against Apple App Store Review Guidelines |
| **7-level evidence ladder** | Every claim labeled from Apple Rule down to Hypothesis -- no unmarked assertions |
| **Sourced data** | Every benchmark carries its source + date -- no unsourced claims |
| **Full lifecycle** | 10 lifecycle stages from first purchase through win-back |

---

## What's Inside

<details>
<summary><strong>7-Level Evidence Ladder</strong></summary>

Every recommendation carries a confidence label. Higher = more reliable.

| Level | Label | Meaning |
|-------|-------|---------|
| 1 | **Apple Rule** | Published in App Store Review Guidelines |
| 2 | **Apple Guidance** | Apple documentation, WWDC sessions, or HIG recommendations not enforced as rejection criteria |
| 3 | **Platform Capability** | Feature documented in StoreKit, App Store Connect, or Google Play Billing |
| 4 | **Vendor Aggregate Data** | Large-scale report from SDK provider (10K+ apps or $1B+ tracked) |
| 5 | **Vendor Case Study** | Published result from a single app or small group |
| 6 | **Operator Insight** | Practitioner observation without published dataset |
| 7 | **Hypothesis** | Directional signal, must be validated on this app |

</details>

<details>
<summary><strong>4-Axis Taxonomy</strong></summary>

The paywall system has four independent axes. Separate them when analyzing or recommending.

**Axis 1: Access Model** -- What we sell (8 types)

| Model | Evidence |
|-------|----------|
| Hard paywall | Vendor Aggregate Data |
| Freemium / soft paywall | Apple Rule |
| Metered paywall | Apple Rule |
| Reverse trial | Operator Insight |
| Hybrid (subscription + one-time) | Operator Insight |
| Multi-tier | Platform Capability |
| Credits / usage packs | Apple Guidance |
| Family Sharing | Platform Capability |

**Axis 2: Placement** -- When we show it (13 types)

Onboarding, Post-aha, Feature gate, Usage limit, Post-close offer, Transaction abandon, Session-start, Renewal-risk, Billing issue / grace period, Win-back, Push marketing, Plan-upgrade, Value primer / bridge.

**Axis 3: Presentation Pattern** -- How we show it (9 types)

One-screen paywall, Value stack, Social-proof-led, Comparison table, Trial timeline, Video/demo paywall, Long-form landing, Interactive/gamified, Contextual mini-paywall.

**Axis 4: Surface / Rendering Layer** -- Where it renders (6 types)

Native StoreKit sheet, Provider remote paywall (Adapty/RevenueCat), Custom native screen, WebView hybrid, System-provided sheet (grace period, price increase consent), Push / notification deep-link surface.

</details>

<details>
<summary><strong>7-Category Matrix</strong></summary>

Different categories have different economics. Do not apply one playbook to all apps.

| Category | Dominant Plan | Trial Impact |
|----------|--------------|-------------|
| Health & Fitness | 68% annual | Trial helps (35-40% trial-to-paid) |
| Gaming | 82% weekly | Short trial works |
| Productivity | 77% monthly | Trial can hurt LTV |
| Lifestyle | Mixed | Direct buyers also more valuable at 12mo |
| Utilities / Education | Trial-friendly | Trial users generate 50.4% more 12-mo LTV |
| AI Apps | 59.8% monthly | Higher pricing tolerated, churn 30% faster |
| Photo & Video | Mixed | Higher refund rates in APAC |

</details>

### 6-Phase Process

```
Discovery & Audit --> Paywall Strategy --> Screen Design
        |                                        |
        v                                        v
iOS Compliance  <-- Implementation  <-- Testing Plan
```

1. **Discovery & Audit** -- understand the app, audit existing paywall, Apple Analytics benchmarks
2. **Paywall Strategy** -- access model, trigger points, plan architecture
3. **Screen Design** -- value block, pricing, CTA, trust/legal
4. **Testing Plan** -- what to test first (structure > polish)
5. **Implementation** -- Adapty, RevenueCat, StoreKit 2, Google Billing
6. **iOS Compliance** -- pre-ship checklist with Apple Rule vs Apple Guidance distinction

### 10-Stage Lifecycle Monetization

| Stage | Action |
|-------|--------|
| First purchase | Main paywall |
| Post-close recovery | Discounted offer (banner) |
| Transaction abandon | Soft prompt with alternative |
| Trial-to-paid | Reminder / value reinforcement |
| Renewal risk | Promotional offer to retain |
| Billing issue | Grace period UX + retry |
| Price increase | Consent flow |
| Win-back | Win-back offer (iOS 18+) |
| Plan upgrade | Upsell to higher tier |
| Refund / support | Support surface, consumption data |

### 6 Screen Templates + 5 New Paywall Types

| Template | When to use |
|----------|-------------|
| **Post-Onboarding** | Hard paywall after onboarding quiz |
| **Feature Gate** | User taps a locked premium feature |
| **Usage Limit** | Free tier cap reached |
| **Transaction Abandon** | User cancelled payment sheet |
| **Post-Close Offer** | Dismissed main paywall -- show banner |
| **Win-Back** | Lapsed subscriber returns |

Plus: Metered Paywall, Reverse Trial, One-Time Unlock, Renewal-Risk / Churn-Save, Intent-Tiered Paywall.

### Benchmark Tables (April 2026)

<details>
<summary><strong>Conversion Rates</strong> -- Adapty/RevenueCat, Mar 2026</summary>

| Metric | Value | Source |
|--------|-------|--------|
| Install to Trial (global) | 10.9-11.2% | Adapty |
| Trial to Paid (global) | 25.6-27.8% | Adapty/RC |
| Trial to Paid (Health & Fitness) | 35.0-39.9% | Adapty/RC |
| Hard paywall D35 conversion | 10.7% | RevenueCat |
| Freemium D35 conversion | 2.1% | RevenueCat |
| Hard paywall vs freemium | ~5x | Both |

</details>

<details>
<summary><strong>A/B Test Win Rates</strong> -- Adapty, Mar 2026</summary>

| Experiment Type | LTV Win Rate |
|----------------|-------------|
| Localization | 62.3% |
| Trial structure | 59.6% |
| Plan duration | 58.7% |
| Number of plans | 57.1% |
| Price changes | 45.5% |
| Visual/copy | 34.6% |

**Key insight:** Structure tests beat copy tests. Don't start with polish.

</details>

<details>
<summary><strong>Pricing Medians</strong> -- Global, Mar 2026</summary>

| Period | Median | Range |
|--------|--------|-------|
| Weekly | $5.99-$7.48 | $4.99-$6.99 |
| Monthly | $10.00-$12.99 | $7.99-$9.99 |
| Annual | $34.80-$38.42 | $29.99-$39.99 |

</details>

<details>
<summary><strong>+ More tables inside SKILL.md</strong></summary>

Trial length impact, Revenue per install, Plan architecture by category, Revenue share by plan type, 12-month retention, LTV data, Superwall aggregate data (32M views), Apple Analytics benchmarks, Regional conversion data.

</details>

### Design Patterns with Evidence

| Pattern | Evidence Level | Source |
|---------|---------------|--------|
| Trial Timeline ("Honest Paywall") | **Vendor Case Study** -- single company (+23%) | Blinkist via Purchasely |
| Personalized Headline from Quiz | **Vendor Aggregate Data** -- 15%+ lift | Adapty 2026 report |
| Animated Paywall | **Vendor Aggregate Data** -- 2.9x vs static | Adapty 2026 report |
| 3 Products vs 1 | **Vendor Aggregate Data** -- +105%, 32M views | Superwall |
| "Building Your Plan" loader | **Operator Insight** -- no published data, widely adopted | Industry observation |
| Multi-Page Paywall | **Hypothesis** -- conflicting results | Superwall |
| "Design Your Trial" | **Hypothesis** -- methodology unpublished | Superwall |

### Apple Compliance (2026)

- Toggle paywall ban (killed Jan 2026, Guideline 3.1.2)
- Billed amount must be most prominent pricing element
- Trial duration + post-trial price required if trial offered
- Restore Purchases, Terms, Privacy links required
- Apple Rule vs Apple Guidance distinction for subscription groups, freemium, metered models
- Family Sharing as trust lever
- Full "Must Have" + "Must NOT Have" checklists inside

---

## How to Use

### Claude Code
```bash
mkdir -p ~/.claude/skills/app-paywall-pilot
curl -o ~/.claude/skills/app-paywall-pilot/SKILL.md \
  https://raw.githubusercontent.com/Nikolai-Iakubovskii/app-paywall-pilot/main/SKILL.md
```
Then run `/app-paywall-pilot` in your project.

### Codex CLI
Add `SKILL.md` content to your project's `AGENTS.md` or custom instructions.

### ChatGPT / GPT-4 / GPT-5
Paste `SKILL.md` as a system prompt, then ask: *"Audit my paywall"* with a screenshot.

### Cursor / Windsurf / AI IDEs
Add `SKILL.md` to your project root or AI rules config.

### Standalone
Read `SKILL.md` directly -- it's a structured knowledge base that works without any AI tool.

---

## Example

Ask your AI: *"Audit my paywall"* with a screenshot. You get:

```
1. Current state      -- app context, placement, plan config
2. Compliance audit   -- rules checked, flags raised (with evidence levels)
3. Value communication -- copy quality, personalization gaps
4. Strategy           -- plan architecture, trigger timing
5. Tests to run       -- prioritized by expected impact
6. Actions            -- fix now vs next sprint
```

---

## Data Sources

| Source | Dataset | Date |
|--------|---------|------|
| [Adapty](https://adapty.io/state-of-in-app-subscriptions/) | 16,000+ apps, $3B revenue | Mar 2026 |
| [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps/) | 115,000+ apps, $16B revenue | Mar 2026 |
| [Superwall](https://superwall.com/) | 100M+ monthly paywall views | 2024-2026 |
| [Apple](https://developer.apple.com/app-store/review/guidelines/) | App Store Review Guidelines | Current |
| [Apple Analytics](https://developer.apple.com/app-store-connect/analytics/) | App Store Connect benchmarks | Current |

Full source manifest with every numeric claim: `sources.json`

---

## What This Is NOT

- **Not a web pricing page optimizer** -- in-app subscription flows only
- **Not a guarantee** -- benchmarks are directional, test with your own data
- **Not a dark patterns toolkit** -- flags anti-patterns, prioritizes user trust
- **Not affiliated** with Adapty, RevenueCat, Superwall, or Apple

---

## Contributing

PRs welcome. Ground rules:

1. **Every benchmark needs a source and date.** No unsourced numbers.
2. **Label every recommendation** with its evidence level (Apple Rule through Hypothesis).
3. **Check against App Store guidelines** before adding UI patterns.
4. **Keep SKILL.md lean.** Every line costs tokens.
5. **Open an issue first** for structural changes.

---

## License

[MIT](LICENSE)

---

<p align="center">
  Built by <a href="https://github.com/Nikolai-Iakubovskii">Nikolai Iakubovskii</a><br>
  Indie developer shipping
  <a href="https://apps.apple.com/us/app/mistyway-walking-quest-game/id6730126556">MistyWay</a> &bull;
  <a href="https://apps.apple.com/us/app/aurora-forecast-map-aurorame/id6749782053">AuroraMe</a>
</p>
