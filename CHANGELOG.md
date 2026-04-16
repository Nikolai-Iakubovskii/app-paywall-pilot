# Changelog

## [3.6.0] -- 2026-04-16

Data refresh + README redesign.

### Changed
- **README header redesigned** with jobs-to-be-done framing. New "Use this when…" table maps 10 concrete user situations to "what to ask your AI" + "which modules activate". New "What you get" table maps 6 outputs to deliverables + powered-by modules. Hero badges upgraded to for-the-badge style. Anchor links + table-of-contents added.
- **ChatGPT teardown trimmed** to remove model-version trivia (GPT-5.x specifics change every quarter and are not paywall-design relevant). Now focuses on the durable lessons: $20/mo consumer baseline, $200/mo premium ceiling (10x Plus), $8/mo geo-tier for emerging markets. Added explicit note: "don't put model version names in your paywall copy unless you commit to updating it every quarter."
- ChatGPT pricing-tier source updated: was "Free/Go/Plus/Business/Enterprise/Edu" (outdated), now "Free/Go/Plus/Pro/Business/Enterprise" (April 2026 verified via OpenAI public pricing page).
- ChatGPT pricing source URL updated to https://chatgpt.com/pricing/

### Note
The skill is for **all subscription apps**, not just AI. ChatGPT is one of 11 teardowns and AI is one of 10 categories. Treat AI examples as comparable references, not as the focus.

## [3.5.0] -- 2026-04-16

Phase 3 of follow-up improvements. Adds polish modules (refund management, cohort analysis), worked-audit examples, audit checklist, migration playbook, and CI validation.

### Added
- **`modules/refund-management.md`** -- 2026 refund baselines per plan/region, prevention sequence (in-app + push timeline), Apple Consumption API for refund decline (with Swift example), Subscription Pause as alternative, channel-level refund diagnostic flowchart.
- **`modules/cohort-analysis.md`** -- three cohort types explained (install / trial / calendar), how to read RC/Adapty/Apphud dashboards correctly, 7 common cohort mistakes, healthy retention curve patterns by plan, pre/post-change comparison setup.
- **`docs/audit-checklist.md`** -- standalone printable 50+ item checklist for manual review before App Store submission. 7 sections (Apple compliance, field reports, copy, pricing, localization, accessibility, implementation) plus quick triage of top 10 items.
- **`docs/migrations/from-toggle-paywall.md`** -- migration playbook for apps caught in Apple's Jan 2026 toggle ban. Apple's exact cited reason. 4 compliant alternatives (separate plan cards, trial-on-annual-only, multi-plan comparison, personalized). Step-by-step migration, expected impact data.
- **`examples/audit-h-and-f-app.md`** -- worked audit for fictional H&F app showing full 12-section DEFAULT OUTPUT FORMAT with calculator-predicted LTV impact.
- **`examples/audit-ai-app.md`** -- worked audit for AI app emphasizing post-aha placement, ChatGPT $20 baseline, geo-tier pricing for emerging markets.
- **`examples/audit-productivity-app.md`** -- worked audit for Productivity app showing the counter-intuitive trial economics (direct buyers > trial buyers per RC 2026), comparison-table presentation pattern, sophisticated audience pricing.
- **`.github/workflows/validate.yml`** -- CI pipeline that runs on push and PR: validates sources.json structure (required fields, allowed evidence classes), checks all internal markdown links resolve, smoke-tests LTV calculator with both direct-CR and trial-funnel inputs, enforces SKILL.md size guard (1500 lines max).
- **`.github/scripts/validate_sources.py`** -- standalone sources.json validator.
- **`.github/scripts/validate_links.py`** -- standalone link validator (caught 3 broken links during initial run).

### Changed
- Module count: 14 -> 16
- Added docs/ tree with audit-checklist + migrations/
- Added examples/ tree with 3 worked audits
- SKILL.md MODULES table updated with all Phase 3 entries

### Fixed
- 3 broken internal links in docs/migrations/from-toggle-paywall.md (off-by-one path depth)

## [3.4.0] -- 2026-04-16

Phase 2 of follow-up improvements. Adds foundational modules that fill gaps identified after Phase 1: continuity onboarding-paywall, lifecycle messaging, canonical metric definitions, executable Python calculator.

### Added
- **`modules/onboarding-paywall-handoff.md`** -- continuity principle (core principle 10) made concrete. 7 onboarding patterns linked to paywall: Noom quiz (77 screens), Cal AI demo-first, Headspace segmented + day/night, Duolingo goal-first, Strava aha-moment, Flo empathy, reverse trial. Loading-screen bridge templates with timing rules. Decision rule for short vs medium vs long onboarding by LTV.
- **`modules/notifications-lifecycle.md`** -- previously missing area. Push + email sequences for trial (Blinkist Day-5 +1,200% opt-in), transaction abandon (Superwall 17% revenue), renewal-risk (Server Notifications V2), billing-issue (system sheet), win-back (iOS 18+ Apple Win-Back). Permission strategy with timing benchmarks. Copy templates per scenario. Tooling comparison (OneSignal / FCM / Customer.io / Iterable / Klaviyo).
- **`modules/glossary.md`** -- canonical definitions for ARPU vs ARPPU, gross LTV vs RLTV, CR variants (effective CR breakdown), MRR/ARR, CAC variants (CPI/CPR/CAC/eCAC), ROAS, retention vs renewal vs churn, plan architecture terms (Subscription Group vs Base Plan + Offer), data-source class definitions. Plus 24-acronym quick reference.
- **`tools/ltv-calculator.py`** -- executable Python implementation of unit-economics-calculator.md. CLI + JSON I/O modes. Implements all default retention multipliers, performance grading, expert advice engine. Verified output matches the worked example in the module ($48.44 ARPPU 7d, 1.26:1 LTV:CAC at 4yr). Runs in any environment with Python 3.

### Changed
- Module count: 11 -> 14
- SKILL.md MODULES table updated with all Phase 2 entries

## [3.3.0] -- 2026-04-16

Phase 1 of follow-up improvements after analyzing adaptyteam/growth-expert-skill. Closes the operational/numerical gap (we were strong on strategy, weak on calculator-style guidance and CAC).

### Added
- **`modules/unit-economics-calculator.md`** -- conversational LTV / ARPU / ROAS / breakeven calculator. Step-by-step input collection, default retention multipliers per plan type, performance grading thresholds (Excellent / Good / Average / Below / Critical), expert advice engine with 11 conditional recommendations, scenario modeling, full worked example. Inspired by adaptyteam/growth-expert-skill calculator pattern, extended with cross-vendor (RC + Superwall + AppsFlyer) thresholds.
- **`modules/indie-dev-faq.md`** -- 35+ direct-answer Q&A grouped into Pricing & Plans, Trials, Conversion & Funnel, Retention & Churn, Markets & Geography, Acquisition & UA, Compliance & Apple, Strategy & Growth. Each answer = threshold + verdict + one action with cited source.
- **`modules/cac-acquisition.md`** -- previously missing area. CAC formula + variants (CPI / CPR / CAC / eCAC), 2026 mobile CAC benchmarks for iOS / Android premium and emerging markets, channel CPI table (ASA / Meta / TikTok / Google / Snap / Reddit / Twitter / Influencer), LTV:CAC thresholds with verdicts, channel mix strategy by stage, MMP comparison (AppsFlyer / Adjust / Singular / RevenueCat), ASA campaign-type breakdown, Web2App economics, common CAC mistakes, when CAC doesn't apply.
- **RESPONSE MODE: PICK ONE** section in SKILL.md -- explicit guidance to match response depth to question. Quick mode (single tactical Q) vs Calculator mode vs Pattern mode vs Full audit vs Compliance triage. Stops the skill from running 12-section audit when user asked one question.
- **QUICK MODE FORMAT** in SKILL.md -- Verdict / Reason / Action template for single-question responses.
- **The Hollow Middle** subsection in pricing-psychology.md -- 41% subscription fatigue, $5-10/mo dead zone, 2026 trend toward either $30+/mo measurable outcomes OR $5/wk + free tier.
- **Apple Small Business Program** subsection in pricing-psychology.md -- 15% vs 30% commission at <$1M revenue, +17.6% net ARPU instantly. Highest-leverage zero-effort change for indie devs.

### Changed
- ANTI-PATTERNS expanded from 17 to 20 (added: Hollow middle pricing, Paying 30% when SBP-eligible, Optimizing without an MMP)

## [3.2.0] -- 2026-04-16

### Added
- **8 deep-dive modules** under `modules/`:
  - `copy-library.md` -- 12 headline formulas, benefit patterns, CTA templates, banned words, locale-specific length expansion factors and tone formality cheatsheet for 12+ locales
  - `teardowns.md` -- annotated paywall analyses for Calm, Duolingo, Noom, Cal AI, Tinder, Strava, Headspace, Blinkist, Flo, ChatGPT, AI companion apps; sourced from Sub Club Podcast, Adapty Library, Growth.Design, Purchasely, ScreensDesign, Kristen Berman, CNBC
  - `pricing-psychology.md` -- Tversky-Kahneman 1981 framing (Science, 17K+ citations), Anderson-Simester 2003 ($9 endings field experiment), Thomas-Morwitz 2005 (left-digit cognition), Ariely Decoy Effect with replication caveats, Cialdini 7 principles mapped to mobile paywall context with 2024 Springer research on which principles are most influential
  - `decision-trees.md` -- 10 diagnostic flowcharts for access model choice, low conversion triage, plan architecture, surface choice, when-to-test ranking, compliance triage, refund diagnosis, vendor-data conflict resolution
  - `category-deep-dives.md` -- per-category economics for H&F, Gaming, Productivity, Lifestyle, Education, AI, Photo & Video, Travel, Shopping, B2B; geography cuts NA/WE/IN-SEA
  - `screen-anatomy.md` -- visual hierarchy, F-pattern layout, thumb zone, spacing rhythm, pricing block anatomy, accessibility (WCAG AA, Dynamic Type, VoiceOver), dark mode, safe areas
  - `localization.md` -- App Store auto-tier vs manual per-territory vs geo-tier strategy, copy length expansion factors, RTL handling, formality cheatsheet for 12+ locales
  - `android-parity.md` -- Play Billing concepts vs StoreKit, EU DMA implications, Android refund reality (31% involuntary failures vs iOS 14%), AppsFlyer 2026 Android growth data
- **Research brief** at `outputs/2026-paywall-research.md` with full source manifest, methodology cross-references, and provenance sidecar
- **3 new core principles** (10, 11, 12): Continuity from onboarding to paywall; Climb the copy ladder (Outcome > Benefit > Feature); First principles beat benchmarks below 1,000 subs/variant
- **WHEN TO IGNORE BENCHMARKS** section with 8 explicit conditions where vendor data should not drive decisions
- **BIG-APP TEARDOWNS** quick-reference table in SKILL.md (full breakdowns in module)
- **Copy patterns quick reference** in SKILL.md (top 5 headline formulas, CTA pattern, banned words, decline pattern)
- **AppsFlyer State of Subscriptions 2026** as a new data source (1.7B installs, 2,900 apps, $2.1B UA spend) -- adds Android growth and emerging-markets perspective missing from Adapty/RevenueCat
- **Refund / billing failure** subsection in Benchmarks (Google Play 31% vs App Store 14% involuntary failures)
- **Trial cancellation timing** subsection (3-day: 55.4% Day 0; 7-day: 39.8% Day 0)
- **RLTV per payer** subsection by category, region, and price tier
- **Academic** and **Platform Capability** evidence classes added to sources.json `_meta`
- **20+ new sources.json entries** including academic foundations (Tversky-Kahneman 1981, Anderson-Simester 2003, Thomas-Morwitz 2005, Ariely 2008, Cialdini 1984, Springer 2024) and big-app teardown sources

### Changed
- **DEFAULT OUTPUT FORMAT** expanded from 8 sections to 12: added Copy variants (2-3), Layout sketch, Localization notes, Android delta
- **CORE PRINCIPLES** expanded from 9 to 12
- **ANTI-PATTERNS** expanded from 13 to 17 (added: testing copy before localizing, same SKU across all of EU, optimizing AI app retention, trial on weekly plans)
- **DATA SOURCES** table expanded from 4 rows to 16, with full evidence-class column
- Apple toggle paywall section updated with exact Apple-cited quote: "This design is confusing and may prevent users from understanding that they are committing to an auto-renewing subscription."

## [3.1.0] -- 2026-04-16

### Added
- **Apple Guidance** evidence level (Level 2) -- sits between Apple Rule and Platform Capability for Apple documentation, WWDC sessions, and HIG recommendations not enforced as rejection criteria
- **4th taxonomy axis: Surface / Rendering Layer** -- 6 surface types: Native StoreKit sheet, Provider remote paywall, Custom native screen, WebView hybrid, System-provided sheet, Push / notification deep-link surface
- **New placements:** plan-upgrade (upsell to higher tier), value primer / bridge (pre-paywall framing)
- **New access model:** credits / usage packs (Apple Guidance)
- **Apple Analytics benchmarks** added to Discovery phase -- App Store Connect data as a first-party source
- **Family Sharing** as trust lever and access model variant (Platform Capability)
- **Plan upgrade** and **refund / support** stages in Lifecycle Monetization (now 10 stages)

### Changed
- Evidence ladder expanded from 6 to 7 levels (Apple Guidance inserted at Level 2, all subsequent levels renumbered)
- A/B win rates downgraded from Vendor Aggregate Data to **Operator Insight** -- methodology not open, cannot verify independently
- "Apps with 50+ experiments earn 18.7x more revenue" claim downgraded to **Operator Insight** -- correlation not causation, methodology unpublished
- Apple Guidance vs Apple Rule distinction applied to subscription groups, freemium model, and metered model documentation
- Design Patterns table uses evidence levels (Vendor Case Study, Vendor Aggregate Data, Operator Insight, Hypothesis) instead of "Proven"
- Data Sources updated: removed Apphud and Sensor Tower (not directly cited in v3.1.0), added Apple Analytics
- Contributing guidelines updated: "Label every recommendation" now references evidence levels instead of Rule/Pattern/Hypothesis

### Removed
- "Proven" label from Design Patterns Reference -- replaced by proper evidence level labels

## [3.0.0] -- 2026-04-16

### Added
- 7-level Evidence Ladder replacing Rule / Pattern / Hypothesis system
- 3-axis Taxonomy: Access Model (6 types), Placement (11 types), Presentation Pattern (9 types)
- Category Matrix with 7 app categories and category-specific economics
- Lifecycle Monetization covering 9 subscription stages
- 5 new paywall types: Metered, Reverse Trial, One-Time Unlock, Renewal-Risk, Intent-Tiered
- Discount & Promotional Offers section with depth guidance and compliance rules
- Apple Offer Types reference (Introductory, Promotional, Offer Codes, Win-Back)
- Field Reports section separating observed rejection patterns from official Apple Rules
- sources.json manifest for every numeric claim

### Changed
- Deep restructure of entire SKILL.md -- taxonomy-first architecture
- Evidence labeling moved from inline markers to formal Evidence Ladder with 6 levels
- iOS Compliance Checklist split into Apple Rules (published) and Field Reports (observed)
- All benchmarks carry explicit evidence level, source, and date
- Source of Truth hierarchy simplified to 4 tiers

### Removed
- Redundant benchmark tables consolidated
- Generic advice replaced by taxonomy-driven recommendations

## [2.0.0] -- 2026-04-15

### Added
- Benchmark tables with source + date columns (Adapty, RevenueCat, Superwall, Apphud, Nami ML, Sensor Tower data)
- 6 screen templates: Post-Onboarding, Feature Gate, Usage Limit, Transaction Abandon, Post-Close Welcome, Win-Back
- Design Patterns Reference section with evidence labels (Proven / Pattern / Hypothesis)
- Apple Offer Types Reference table (Introductory, Promotional, Offer Codes, Win-Back)
- WWDC 2025 StoreKit 2 updates
- Regional pricing and conversion data
- Category-specific plan architecture data
- Trial length impact analysis with nuanced interpretation
- Market reality benchmarks (concentration, experimentation impact)
- Open-source README and CHANGELOG

### Changed
- Rebuilt from revised v1.1.0 foundation -- kept Source of Truth hierarchy, Rule/Pattern/Hypothesis labeling, Core Principles, Anti-patterns
- Enhanced iOS Compliance Checklist -- split into "Must have" and "Must NOT have" sections
- Expanded A/B Test Win Rates table with 6 experiment types
- DATA SOURCES section now lists all providers with dataset sizes

### Removed
- Commitment ritual / finger-hold pattern (moved to Anti-patterns)
- Unsourced benchmark claims
- Generic "Questions to Ask" section (replaced by targeted Phase 1 questions)

## [1.1.0] -- 2026-04-15

### Changed
- Source of Truth hierarchy: Apple docs > StoreKit > provider docs > provider blogs
- Added "How to Label Advice" -- Rule / Pattern / Hypothesis classification
- Removed commitment rituals as default recommendation
- Added Anti-pattern #15: emotional rituals without evidence
- Made benchmark notes explicitly directional with verification requirement
- Simplified Core Principles section

## [1.0.0] -- 2025-12-01

### Added
- Initial skill with 5 phases: Discovery, Strategy, Screen Content, A/B Test Plan, Implementation
- Benchmark tables from Adapty/RevenueCat 2025-2026 reports
- Screen templates for 5 paywall types
- iOS compliance checklist
- Personalization patterns with quiz-based examples
- Related skills cross-references
