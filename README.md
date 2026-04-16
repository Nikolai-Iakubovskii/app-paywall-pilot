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
    <img src="https://img.shields.io/badge/Platform-iOS_%7C_Android-blue?style=flat-square" alt="Platform">
    <img src="https://img.shields.io/badge/Benchmarks-April_2026-green?style=flat-square" alt="Benchmarks">
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
    <img src="https://img.shields.io/github/stars/Nikolai-Iakubovskii/app-paywall-pilot?style=flat-square" alt="Stars">
  </p>
</p>

---

An AI instruction file (`SKILL.md`) that turns any LLM into a mobile subscription paywall expert.

Works with **Claude Code** &bull; **Codex** &bull; **ChatGPT** &bull; **Cursor** &bull; **Windsurf** &bull; **Gemini** — or any AI tool that supports custom instructions.

---

## The Problem

Most paywall advice is either **generic web CRO** that ignores App Store rules, **hype-driven** single-app case studies with no methodology, or **outdated** tactics that get your app rejected by Apple in 2026.

## The Fix

App Paywall Pilot gives your AI assistant real-world paywall expertise:

| Principle | How |
|-----------|-----|
| **Compliance first** | Every recommendation checked against Apple App Store Review Guidelines |
| **Labeled confidence** | Each finding marked as **Rule**, **Pattern**, or **Hypothesis** |
| **Sourced data** | Every benchmark carries its source + date — no unsourced claims |
| **Full lifecycle** | Placement, pricing, trials, personalization, analytics, implementation |

---

## What's Inside

### 6-Phase Process

```
Discovery & Audit ──> Paywall Strategy ──> Screen Design
        │                                        │
        v                                        v
iOS Compliance  <── Implementation  <── Testing Plan
```

1. **Discovery & Audit** — understand the app, audit existing paywall
2. **Paywall Strategy** — access model, trigger points, plan architecture
3. **Screen Design** — value block, pricing, CTA, trust/legal
4. **Testing Plan** — what to test first (structure > polish)
5. **Implementation** — Adapty, RevenueCat, StoreKit 2, Google Billing
6. **iOS Compliance** — pre-ship checklist

### 6 Screen Templates

| Template | When to use |
|----------|-------------|
| **Post-Onboarding** | Hard paywall after onboarding quiz |
| **Feature Gate** | User taps a locked premium feature |
| **Usage Limit** | Free tier cap reached |
| **Transaction Abandon** | User cancelled payment sheet |
| **Post-Close Offer** | Dismissed main paywall — show banner |
| **Win-Back** | Lapsed subscriber returns |

### Benchmark Tables (April 2026)

<details>
<summary><strong>Conversion Rates</strong> — Adapty/RevenueCat, Mar 2026</summary>

| Metric | Value | Source |
|--------|-------|--------|
| Install → Trial (global) | 10.9–11.2% | Adapty |
| Trial → Paid (global) | 25.6–27.8% | Adapty/RC |
| Trial → Paid (Health & Fitness) | 35.0–39.9% | Adapty/RC |
| Hard paywall D35 conversion | 10.7% | RevenueCat |
| Freemium D35 conversion | 2.1% | RevenueCat |
| Hard paywall vs freemium | ~5x | Both |

</details>

<details>
<summary><strong>A/B Test Win Rates</strong> — Adapty, Mar 2026</summary>

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
<summary><strong>Pricing Medians</strong> — Global, 2025 data</summary>

| Period | Median | Range |
|--------|--------|-------|
| Weekly | $5.99–$7.48 | $4.99–$6.99 |
| Monthly | $10.00–$12.99 | $7.99–$9.99 |
| Annual | $34.80–$38.42 | $29.99–$39.99 |

</details>

<details>
<summary><strong>+ More tables inside SKILL.md</strong></summary>

Trial length impact, Revenue per install, Plan architecture by category, Revenue share by plan type, 12-month retention, LTV data, Superwall aggregate data (32M views), Regional conversion data.

</details>

### Design Patterns with Evidence

| Pattern | Evidence | Source |
|---------|----------|--------|
| Trial Timeline ("Honest Paywall") | **Pattern** — single company case study (+23%) | Blinkist via Purchasely |
| Personalized Headline from Quiz | **Pattern** — vendor data (15%+ lift) | Adapty 2026 report |
| Animated Paywall | **Pattern** — vendor data (2.9x vs static) | Adapty 2026 report |
| 3 Products vs 1 | **Pattern** — large-scale vendor data (+105%, 32M views) | Superwall |
| Multi-Page Paywall | **Hypothesis** — conflicting results | Superwall |
| "Design Your Trial" | **Hypothesis** — methodology unpublished | Superwall |

### Apple Compliance (2026)

- Toggle paywall ban (killed Jan 2026, Guideline 3.1.2)
- Billed amount must be most prominent pricing element
- Trial duration + post-trial price required if trial offered
- Restore Purchases, Terms, Privacy links required
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
Read `SKILL.md` directly — it's a structured knowledge base that works without any AI tool.

---

## Example

Ask your AI: *"Audit my paywall"* with a screenshot. You get:

```
1. Current state      — app context, placement, plan config
2. Compliance audit   — rules checked, flags raised (Rule/Pattern/Hypothesis)
3. Value communication — copy quality, personalization gaps
4. Strategy           — plan architecture, trigger timing
5. Tests to run       — prioritized by expected impact
6. Actions            — fix now vs next sprint
```

---

## Data Sources

| Source | Dataset | Date |
|--------|---------|------|
| [Adapty](https://adapty.io/state-of-in-app-subscriptions/) | 16,000+ apps, $3B revenue | Mar 2026 |
| [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps/) | 115,000+ apps, $16B revenue | Mar 2026 |
| [Superwall](https://superwall.com/) | 100M+ monthly paywall views | 2024–2026 |
| [Apphud](https://apphud.com/) | Subscription analytics | 2025–2026 |
| [Apple](https://developer.apple.com/app-store/review/guidelines/) | App Store Review Guidelines | Current |
| [Sensor Tower](https://sensortower.com/) | State of Mobile reports | 2025–2026 |

---

## What This Is NOT

- **Not a web pricing page optimizer** — in-app subscription flows only
- **Not a guarantee** — benchmarks are directional, test with your own data
- **Not a dark patterns toolkit** — flags anti-patterns, prioritizes user trust
- **Not affiliated** with Adapty, RevenueCat, Superwall, Apphud, or Apple

---

## Contributing

PRs welcome. Ground rules:

1. **Every benchmark needs a source and date.** No unsourced numbers.
2. **Label every recommendation** — Rule, Pattern, or Hypothesis.
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
