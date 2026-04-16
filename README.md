<p align="center">
  <h1 align="center">App Paywall Pilot</h1>
  <p align="center">
    <strong>Your AI copilot for designing, auditing, and shipping<br>App Store-compliant in-app paywalls.</strong>
  </p>
  <p align="center">
    <a href="#how-to-use">Get Started</a> &bull;
    <a href="#modules">Modules</a> &bull;
    <a href="#whats-inside">What's Inside</a> &bull;
    <a href="#data-sources">Data Sources</a> &bull;
    <a href="#contributing">Contributing</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Version-3.5.0-brightgreen?style=flat-square" alt="Version">
    <img src="https://img.shields.io/badge/Platform-iOS_%7C_Android-blue?style=flat-square" alt="Platform">
    <img src="https://img.shields.io/badge/Benchmarks-April_2026-green?style=flat-square" alt="Benchmarks">
    <img src="https://img.shields.io/badge/Modules-16-purple?style=flat-square" alt="Modules">
    <img src="https://img.shields.io/badge/Sources-58%2B-orange?style=flat-square" alt="Sources">
    <img src="https://github.com/Nikolai-Iakubovskii/app-paywall-pilot/actions/workflows/validate.yml/badge.svg" alt="Validate">
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
    <img src="https://img.shields.io/github/stars/Nikolai-Iakubovskii/app-paywall-pilot?style=flat-square" alt="Stars">
  </p>
</p>

---

An AI instruction file (`SKILL.md`) plus 8 deep-dive modules that turn any LLM into a mobile subscription paywall expert.

Works with **Claude Code** &bull; **Codex** &bull; **ChatGPT** &bull; **Cursor** &bull; **Windsurf** &bull; **Gemini** -- or any AI tool that supports custom instructions.

---

## The Problem

Most paywall advice falls into one of three traps:

- **Generic web CRO** that ignores App Store rules and gets your app rejected
- **Hype-driven case studies** with no methodology and no sample size
- **Outdated tactics** -- toggle paywalls were the gold standard in 2024 and are mass-rejected by Apple in 2026

And most AI assistants compound the problem: they recommend whatever pattern they saw most often in 2023 training data, with no source, no compliance check, and no acknowledgement of category economics.

## The Fix

App Paywall Pilot grounds every recommendation in published evidence and labels its confidence level explicitly:

| Principle | How |
|-----------|-----|
| **Compliance first** | Every recommendation checked against Apple App Store Review Guidelines |
| **7-level evidence ladder** | Every claim labeled from Apple Rule down to Hypothesis -- no unmarked assertions |
| **Sourced data** | Every benchmark carries source + date + sample size -- no unsourced claims |
| **Big-app teardowns** | Annotated paywall analyses for Calm, Duolingo, Noom, Cal AI, Tinder, Strava, Headspace, Blinkist, Flo, ChatGPT, AI companions |
| **Academic foundations** | Pricing psychology grounded in Tversky-Kahneman 1981 (Science), Anderson-Simester 2003, Thomas-Morwitz 2005, Ariely 2008, Cialdini -- not just blog posts |
| **Full lifecycle** | 10 stages from first purchase through win-back |
| **Modular** | Core SKILL.md plus 8 deep-dive modules loaded on demand |
| **Common-sense overrides** | Explicit "WHEN TO IGNORE BENCHMARKS" guidance for small N, niche category, recent launch |

---

## Modules

The skill is split into a core [SKILL.md](SKILL.md) plus 16 deep-dive modules under [`modules/`](modules/), an executable Python calculator, worked examples, and migration playbooks. Load on demand based on the task.

| Module | What's inside |
|--------|---------------|
| [copy-library.md](modules/copy-library.md) | The Copy Ladder (Outcome > Benefit > Feature), 12 headline formulas, benefit-bullet patterns, CTA templates with action+benefit pattern, banned words list, length expansion factors and formality cheatsheet for 12+ locales, loading-screen copy, pricing-block templates |
| [teardowns.md](modules/teardowns.md) | Annotated paywall breakdowns for **Calm, Duolingo, Noom, Cal AI, Tinder, Strava, Headspace, Blinkist, Flo, ChatGPT, AI companions** -- structure, copy, pricing, takeaway, source for each |
| [pricing-psychology.md](modules/pricing-psychology.md) | Tversky & Kahneman 1981 (framing, *Science*), Anderson & Simester 2003 ($9 endings, field experiment), Thomas & Morwitz 2005 (left-digit), Ariely 2008 (decoy with replication caveats), Cialdini 7 principles + 2024 Springer mobile-app strength data, anchor / decoy / charm / per-day / PPP frameworks, **Hollow Middle** 2026 trend, **Apple SBP** explainer |
| [decision-trees.md](modules/decision-trees.md) | 10 diagnostic flowcharts: access model choice, low-conversion triage, plan architecture, surface choice, when-to-test priority, compliance triage, refund diagnosis, vendor-data conflict resolution |
| [category-deep-dives.md](modules/category-deep-dives.md) | Per-category economics for Health & Fitness, Gaming, Productivity, Lifestyle, Education, AI, Photo & Video, Travel, Shopping, B2B; geography cuts NA / Western Europe / IN-SEA |
| [screen-anatomy.md](modules/screen-anatomy.md) | Visual hierarchy, F-pattern layout, thumb zone, spacing rhythm, pricing block anatomy, accessibility (WCAG AA, Dynamic Type, VoiceOver), dark mode, safe areas, loading and error states |
| [localization.md](modules/localization.md) | Adapty 2026 4.4x pricing variance data, App Store auto-tier vs manual per-territory vs geo-tier strategy with cost/benefit, copy length expansion factors, formality, RTL, number formatting, cultural trust signals |
| [android-parity.md](modules/android-parity.md) | Play Billing Library v6+ concepts (Base Plan + Offers), EU DMA alternative billing, Android refund reality (RC: 31% involuntary failures vs iOS 14%), AppsFlyer 2026 Android growth (4x faster than iOS) |
| [unit-economics-calculator.md](modules/unit-economics-calculator.md) | Conversational LTV / ARPU / ROAS / breakeven calculator with default retention multipliers, performance grading thresholds, expert advice engine with 11 conditional recommendations, scenario modeling, full worked example |
| [indie-dev-faq.md](modules/indie-dev-faq.md) | 35+ direct-answer Q&A: "Should I add weekly?", "Are my numbers good?", "Why is trial-to-paid low?", "What's a healthy LTV:CAC?" -- threshold + verdict + one action with cited source |
| [cac-acquisition.md](modules/cac-acquisition.md) | CAC formula and variants, 2026 mobile CAC benchmarks (iOS / Android, premium and emerging markets), channel CPI table (ASA / Meta / TikTok / Google / Snap / Reddit), LTV:CAC thresholds, channel mix strategy by stage, MMP comparison (AppsFlyer / Adjust / Singular / RevenueCat), Apple Search Ads tactics, Web2App economics, common CAC mistakes |
| [onboarding-paywall-handoff.md](modules/onboarding-paywall-handoff.md) | Continuity principle made concrete. 7 onboarding patterns linked to paywall (Noom quiz, Cal AI demo, Headspace segmented, Duolingo goal-first, Strava aha, Flo empathy, reverse trial). Loading-screen bridge templates. Decision rule for onboarding length by LTV. |
| [notifications-lifecycle.md](modules/notifications-lifecycle.md) | Push + email sequences for trial (Blinkist Day-5 +1,200% opt-in), abandon recovery (Superwall 17% revenue), renewal-risk, billing-issue, win-back. Permission strategy, copy templates, tooling choice. |
| [glossary.md](modules/glossary.md) | Canonical definitions: ARPU vs ARPPU, gross vs RLTV, CR variants, MRR/ARR, CAC variants (CPI/CPR/CAC/eCAC), ROAS, retention vs renewal vs churn. Plus 24-acronym quick reference. |
| [refund-management.md](modules/refund-management.md) | Refund baselines per plan + region, prevention sequence (in-app + push), Apple Consumption API for refund decline (Swift example), Subscription Pause alternative, channel-level diagnostic flowchart. |
| [cohort-analysis.md](modules/cohort-analysis.md) | Three cohort types (install / trial / calendar), how to read RC/Adapty/Apphud dashboards, 7 common cohort mistakes, healthy retention curve patterns, pre/post-change comparison setup. |

Plus standalone documentation, executable tools, worked examples, and research:

- **[docs/audit-checklist.md](docs/audit-checklist.md)** -- printable 50+ item checklist for manual review before App Store submission
- **[docs/migrations/from-toggle-paywall.md](docs/migrations/from-toggle-paywall.md)** -- migration playbook for apps caught in Apple's Jan 2026 toggle ban, with 4 compliant alternatives
- **[examples/](examples/)** -- worked audit examples: [H&F app](examples/audit-h-and-f-app.md), [AI app](examples/audit-ai-app.md), [Productivity app](examples/audit-productivity-app.md). Each shows full 12-section DEFAULT OUTPUT FORMAT.
- **[tools/ltv-calculator.py](tools/ltv-calculator.py)** -- Python implementation of the unit-economics calculator. CLI + JSON I/O. Verified output matches worked example.
- **[.github/workflows/validate.yml](.github/workflows/validate.yml)** -- CI: validates sources.json structure, all internal links resolve, calculator smoke tests, SKILL.md size guard
- [outputs/2026-paywall-research.md](outputs/2026-paywall-research.md) -- full source manifest with methodology, sample sizes, evidence class for every benchmark used
- [outputs/2026-paywall-research.provenance.md](outputs/2026-paywall-research.provenance.md) -- sources consulted vs accepted vs rejected, cross-references, weak-signal flags

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

Plus two academic-foundation classes used in pricing-psychology.md: **academic** (peer-reviewed papers) and **platform_capability** (documented features).

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
<summary><strong>10-Category Matrix</strong></summary>

Different categories have different economics. Do not apply one playbook to all apps. Full per-category deep-dives in [modules/category-deep-dives.md](modules/category-deep-dives.md).

| Category | Dominant Plan | Trial Impact | Notable 2026 stat |
|----------|--------------|-------------|-------------------|
| Health & Fitness | 60.6% annual | Trial helps (35-42% trial-to-paid) | Install LTV $1.21 (highest of any category) |
| Gaming | 82% weekly | Short trial works | 73% use ≤4-day trials |
| Productivity | 77% monthly | Trial **hurts** LTV ($56.95 direct vs $49.13 trial) | Direct buyers preferred |
| Lifestyle | Mixed | Direct buyers ~21% more valuable at 12mo | Similar to Productivity |
| Education | Annual / mixed | Trial users +50.4% 12-mo LTV | Highest discount usage (14.3%) |
| AI Apps | 59.8% monthly | Higher pricing tolerated, churn 30% faster | $20/mo (ChatGPT) is the baseline |
| Photo & Video | Mixed | Trial-to-paid 22.2% (lowest) | APAC refund rate 14.1% |
| Travel | 3+ plans | Trial-to-paid 43.5% (highest) | Annual median $20 (lowest) |
| Shopping | 1-plan dominant | Mixed monetization | 40% use single-plan paywalls |
| Business / B2B | Annual | Trial filters intent | $35.48 12-mo RLTV per payer |

</details>

<details>
<summary><strong>Geography Cuts</strong> -- where to focus in 2026</summary>

Per AppsFlyer 2026 (1.7B installs, 2,900 apps): subscription UA spend grew 24% YoY but the growth is **not where you might think**.

| Region | D30 Trial | D35 Paid | D14 RPI | 12-mo RLTV per payer |
|--------|-----------|----------|---------|----------------------|
| North America | 7.1% | 2.8% | $0.38 | $32 |
| Western Europe | mid | mid | mid | $25 |
| IN/SEA | 3.0-3.7% | 0.7% | $0.08 | $14 |

- **Android growing 4x faster than iOS** in subscription UA
- **Indian Subcontinent: 49% of net Android paid install growth**; LATAM: 18%
- **North America: essentially flat**
- **Top 5 apps per category control >90% of UA spend** (high concentration risk)
- **Western Europe charges 29-39% more than North America** -- huge under-priced opportunity

Strategic implication: NA-only apps face flat user pool; emerging markets are where Android growth happens. Geo-tier pricing (ChatGPT Go @ $8 for India) is increasingly important.

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

### Big-App Teardowns

Annotated breakdowns of 11 high-revenue subscription apps in [modules/teardowns.md](modules/teardowns.md). One-line summary:

| App | Single biggest pattern |
|-----|------------------------|
| **Calm** | Single plan (no tier choice) -- universal value = no choice paralysis |
| **Duolingo** | Brand-consistent paywall + "Start my free week" CTA pattern |
| **Noom** | 77-step onboarding -> "your reserved plan" -> paywall |
| **Cal AI** | Hard paywall + obsessive personalization + single core action ($1.4M/mo profit) |
| **Tinder** | Blur-to-reveal Zeigarnik tension + ML-driven dynamic paywall |
| **Strava** | 30-day trial without credit card (ultimate trust signal) |
| **Headspace** | Equal-prominence monthly + annual (NOT annual-default) + day/night theming |
| **Blinkist** | Trial Timeline visual: +23% trial signups, -55% complaints, +1,200% notif opt-in |
| **Flo** | 70-screen onboarding + free core / premium upsell ($6M/mo revenue) |
| **ChatGPT** | $20/mo became AI baseline; geo-tier (Go @ $8) for emerging markets |
| **AI companions** | High price tolerance + high churn -- optimize first-month conversion |

### Benchmark Tables (April 2026)

<details>
<summary><strong>Conversion Rates</strong> -- Adapty 16K apps + RevenueCat 115K apps + AppsFlyer 1.7B installs, Mar 2026</summary>

| Metric | Value | Source |
|--------|-------|--------|
| Install to Trial (global) | 10.9% | Adapty |
| Install to Trial (North America) | 14.5% | Adapty |
| Trial to Paid (global) | 25.6% | Adapty |
| Trial to Paid (Health & Fitness) | 35.0-42.2% | Adapty/RC |
| Trial to Paid (Travel) | 43.5% (highest) | RC |
| Trial to Paid (Photo & Video) | 22.2% (lowest) | RC |
| Hard paywall D35 conversion | 10.7% | RevenueCat |
| Freemium D35 conversion | 2.1% | RevenueCat |
| Hard paywall vs freemium | ~5x | Both |
| Day 0 share of trial starts | ~80-90% | Both |
| Hard paywall LTV uplift vs soft | +21% per subscriber | Adapty |

</details>

<details>
<summary><strong>A/B Test Win Rates</strong> -- Adapty platform, Mar 2026 (vendor_blog)</summary>

| Experiment Type | LTV Win Rate |
|----------------|-------------|
| Localization | 62.3% |
| Trial structure | 59.6% |
| Plan duration | 58.7% |
| Number of plans | 57.1% |
| Price changes | 45.5% |
| Visual/copy | 34.6% |

**Key insight:** Structure tests beat copy tests by ~2x. Don't start with polish. **Localize first** -- highest win rate of any test category.

</details>

<details>
<summary><strong>Pricing Medians</strong> -- Global, Mar 2026</summary>

| Period | Median | Range |
|--------|--------|-------|
| Weekly | $5.99-$7.48 | $4.99-$6.99 |
| Monthly | $10.00-$12.99 | $7.99-$9.99 |
| Annual | $34.80-$38.42 | $29.99-$39.99 |

**EU charges 29-39% more than NA. IN/SEA RLTV is ~46% of NA on annual.**

</details>

<details>
<summary><strong>Trial Cancellation Timing</strong> -- RevenueCat 115K apps, Mar 2026</summary>

| Trial length | Cancel Day 0 |
|--------------|--------------|
| 3 days | 55.4% |
| 7 days | 39.8% |

**Short trials = aggressive (more conversions, more refunds). 7-day is the balanced default.**

</details>

<details>
<summary><strong>Refund / Billing Failure</strong> -- RevenueCat 115K apps + Adapty 2026</summary>

| Metric | Value |
|--------|-------|
| Google Play involuntary billing failures | ~31% of cancellations |
| App Store involuntary billing failures | 14% of cancellations |
| Photo & Video APAC refund rate | 14.1% (highest regional) |

</details>

<details>
<summary><strong>+ More tables inside SKILL.md</strong></summary>

Trial length impact, Revenue per install (D14 + D60), Plan architecture by category, Revenue share by plan type, 12-month retention by plan, RLTV per payer by category / region / price tier, Superwall aggregate data (32M views, 18-company abandon study), AppsFlyer 2026 (1.7B installs, Android 4x growth), Apple Analytics benchmarks.

</details>

### Design Patterns with Evidence

| Pattern | Evidence Level | Source |
|---------|---------------|--------|
| Trial Timeline ("Honest Paywall") | **Vendor Case Study** -- single company (+23% signups, -55% complaints, +1,200% notif opt-in) | Blinkist via Purchasely |
| Personalized Headline from Quiz | **Vendor Aggregate Data** -- 15%+ lift, methodology not open | Adapty 2026 report |
| Animated Paywall | **Vendor Aggregate Data** -- 2.9x vs static, methodology not open | Adapty 2026 report |
| 3 Products vs 1 | **Aggregate Study** -- +61% (1->2) and +44% (2->3), 32M views, 15 apps | Superwall |
| Transaction Abandon Recovery | **Aggregate Study** -- 17% of total revenue, 18 companies | Superwall |
| "Building Your Plan" loader | **Operator Insight** -- no published data, widely adopted | Industry observation |
| Long Onboarding Quiz | **Operator Insight** -- consistent in highest-revenue H&F apps | Noom, Flo, Cal AI |
| Multi-Page Paywall | **Hypothesis** -- conflicting results (Speak4Me +27% vs Stompers single-page win) | Superwall |
| "Design Your Trial" | **Hypothesis** -- methodology unpublished | Superwall |

### Apple Compliance (2026)

- **Toggle paywall ban** (killed Jan 2026, Guideline 3.1.2): Apple-cited reason: *"This design is confusing and may prevent users from understanding that they are committing to an auto-renewing subscription."*
- Billed amount must be most prominent pricing element
- Trial duration + post-trial price required if trial offered
- Restore Purchases, Terms, Privacy links required
- Apple Rule vs Apple Guidance distinction for subscription groups, freemium, metered models
- Family Sharing as trust lever
- Field reports (RevenueFlo): pricing fonts <16pt, delayed close >5s, two paywalls back-to-back, guilt decline copy = high rejection risk
- Full "Must Have" + "Must NOT Have" checklists inside

### Pricing Psychology -- Academic Foundations

Mobile paywall pricing isn't invented in vendor blogs. The foundational research:

- **Tversky & Kahneman 1981** -- Framing effects (gain vs loss). *Science*, 17,000+ citations.
- **Anderson & Simester 2003** -- $9 endings outsell $4 endings in field experiments. *Quantitative Marketing and Economics*.
- **Thomas & Morwitz 2005** -- Left-digit effect: $9.99 anchors on "9". *Journal of Consumer Research*.
- **Ariely 2008** -- Decoy effect (Economist subscription experiment). *Predictably Irrational*.
- **Cialdini 1984 + Pre-Suasion 2016** -- 7 principles of influence. Springer 2024 mobile-app study: Social Proof + Authority test as most influential.

Full mobile-application mapping in [modules/pricing-psychology.md](modules/pricing-psychology.md).

---

## How to Use

### Claude Code

Quickest start (clone the whole skill including modules):

```bash
git clone https://github.com/Nikolai-Iakubovskii/app-paywall-pilot \
  ~/.claude/skills/app-paywall-pilot
```

Then run `/app-paywall-pilot` in your project. The core SKILL.md loads first; modules load on demand when relevant.

Single-file install (core only):

```bash
mkdir -p ~/.claude/skills/app-paywall-pilot
curl -o ~/.claude/skills/app-paywall-pilot/SKILL.md \
  https://raw.githubusercontent.com/Nikolai-Iakubovskii/app-paywall-pilot/main/SKILL.md
```

### Codex CLI
Add `SKILL.md` content to your project's `AGENTS.md` or custom instructions. Reference modules via raw GitHub URLs.

### ChatGPT / GPT-5 / GPT-5.3
Paste `SKILL.md` as a system prompt, then ask: *"Audit my paywall"* with a screenshot. For deeper analysis, also paste the relevant module (e.g. `teardowns.md` when comparing to Calm).

### Cursor / Windsurf / AI IDEs
Add `SKILL.md` to your project root or AI rules config. Modules in `modules/` will be findable in workspace.

### Standalone (no AI tool)
Read `SKILL.md` and the modules directly -- they're a structured knowledge base that works without any AI tool. Designed to be human-readable.

---

## Example Output

Ask your AI: *"Audit my paywall"* with a screenshot. With v3.2.0, the default output is **12 sections**:

```
1. Current state           -- app context, placement, plan config
2. Main problem            -- plain language
3. Recommended access model -- from taxonomy
4. Recommended placements   -- from taxonomy
5. Recommended presentation -- from taxonomy
6. Screen content           -- headline, benefits, pricing, CTA, trust
7. Copy variants            -- 2-3 short and long versions, Copy Ladder rung
8. Layout sketch            -- ASCII or block diagram, thumb-zone confirmed
9. Localization notes       -- pricing per market, CTA length budget per locale
10. Tests to run            -- ranked by Adapty 2026 win rate (localization first)
11. iOS review risks        -- Apple Rules + Field Reports
12. Android delta           -- Play Billing differences if cross-platform
```

Each finding labeled with its evidence level.

---

## Data Sources

| Source | Dataset | Date | Class |
|--------|---------|------|-------|
| [Adapty State of In-App Subscriptions 2026](https://adapty.io/state-of-in-app-subscriptions/) | 16,000 apps, $3B revenue, 500M txns, 105K paywalls, 50+ countries | 2026-03-14 | large_scale_report |
| [Adapty Health & Fitness Benchmarks 2026](https://adapty.io/blog/health-fitness-app-subscription-benchmarks/) | Category cut from $3B dataset | 2026 | large_scale_report |
| [Adapty Paywall Experiments Playbook](https://adapty.io/blog/paywall-experiments-playbook/) | Adapty platform A/B tests | 2026 | vendor_blog |
| [RevenueCat State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps/) | 115,000+ apps, $16B+ revenue, 1B+ txns | 2026-03 | large_scale_report |
| [Superwall Product Count Study](https://superwall.com/blog/how-many-products-should-you-offer-on-your-paywall) | 32.3M paywall opens, 15 apps, 383K conversions | 2025 | aggregate_study |
| [Superwall Transaction Abandon Study](https://superwall.com/blog/17-revenue-boost-with-transaction-abandon-paywalls-a-case-study/) | 18 companies, 525K users | 2024-08 | aggregate_study |
| [AppsFlyer State of Subscriptions 2026](https://www.appsflyer.com/resources/reports/subscription-marketing/) | 1.7B paid installs, 2,900 apps, $2.1B UA spend | 2026 | large_scale_report |
| [Apphud Subscription Guide](https://apphud.com/blog/scale-app-revenue-with-apphud) | Apphud platform (no public sample size) | 2025 | vendor_blog |
| [RevenueFlo iOS Rejections](https://revenueflo.com/blog/common-ios-paywall-rejections-and-the-fixes-that-work) | Developer rejection reports | 2026 | field_observation |
| [Apple App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Official | Current | apple_docs |
| [Apple Analytics](https://developer.apple.com/app-store-connect/analytics/) | App Store Connect benchmarks | Current | apple_docs |
| [Tversky & Kahneman 1981](https://www.science.org/doi/10.1126/science.7455683) | Science, 17K+ citations | 1981 | academic |
| [Anderson & Simester 2003](https://link.springer.com/article/10.1023/A:1023581927405) | Quantitative Marketing and Economics field experiment | 2003 | academic |
| [Thomas & Morwitz 2005](https://academic.oup.com/jcr/article/32/1/54/1791749) | Journal of Consumer Research | 2005 | academic |
| [Ariely Decoy Effect](https://thestrategystory.com/2020/10/02/economist-magazine-a-story-of-clever-decoy-pricing/) | Predictably Irrational, Ch. 1 | 2008 | academic |
| [Springer 2024 Mobile Persuasion](https://link.springer.com/chapter/10.1007/978-3-031-59465-6_17) | Cialdini principles in mobile contexts | 2024 | academic |

Full source manifest with every numeric claim: [`sources.json`](sources.json) (50+ entries with URL, date, scope, evidence class).

Independent paywall screenshot libraries used for teardowns:
[Adapty Paywall Library](https://adapty.io/paywall-library/) &bull;
[Mobbin](https://mobbin.com) &bull;
[ScreensDesign](https://screensdesign.com) &bull;
[Paywallscreens.com](https://www.paywallscreens.com) &bull;
[NamiML](https://www.namiml.com/paywalls/) &bull;
[Growth.Design](https://growth.design/case-studies/) &bull;
[Funnel Teardowns](https://www.funnelteardowns.net)

---

## What This Is NOT

- **Not a web pricing page optimizer** -- in-app subscription flows only
- **Not a guarantee** -- benchmarks are directional; SKILL.md has an explicit "WHEN TO IGNORE BENCHMARKS" section for when not to trust them
- **Not a dark patterns toolkit** -- flags anti-patterns, prioritizes user trust
- **Not affiliated** with Adapty, RevenueCat, Superwall, AppsFlyer, Apphud, or Apple

---

## What's New in v3.2.0

- **8 deep-dive modules** under `modules/` (copy library, teardowns, pricing psychology, decision trees, category deep-dives, screen anatomy, localization, Android parity)
- **Research brief** at `outputs/2026-paywall-research.md` with full methodology + provenance sidecar
- **3 new core principles**: onboarding-paywall continuity, copy ladder, first principles below 1,000 subs/variant
- **WHEN TO IGNORE BENCHMARKS** section with 8 explicit conditions
- **AppsFlyer 2026** added as new data source (1.7B installs) -- closes the Android growth and emerging-markets gap
- **Big-app teardowns** for 11 apps (Calm, Duolingo, Noom, Cal AI, Tinder, Strava, Headspace, Blinkist, Flo, ChatGPT, AI companions)
- **Academic foundations** (Tversky-Kahneman, Anderson-Simester, Thomas-Morwitz, Ariely, Cialdini, Springer 2024)
- **Default output expanded** from 8 to 12 sections (added Copy variants, Layout sketch, Localization notes, Android delta)
- **20+ new sources.json entries** with two new evidence classes (`academic`, `platform_capability`)

See [CHANGELOG.md](CHANGELOG.md) for full release notes.

---

## Contributing

PRs welcome. Ground rules:

1. **Every benchmark needs a source and date.** No unsourced numbers.
2. **Label every recommendation** with its evidence level (Apple Rule through Hypothesis).
3. **Check against App Store guidelines** before adding UI patterns.
4. **Keep SKILL.md lean** -- put deep content in a module under `modules/` and reference from SKILL.md. Every line in the core costs tokens for every user.
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
