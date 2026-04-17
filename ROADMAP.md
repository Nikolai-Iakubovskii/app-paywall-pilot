# Roadmap

**Version:** 4.0.0 (framework)
**Last updated:** 2026-04-17

Paywall Pilot started as a single Claude Code skill for in-app paywalls (v1.0–v3.8). In v4.0 it becomes a **framework** — positioned to expand into adjacent subscription-app domains while keeping paywalls as the flagship domain.

---

## Current state (v4.0.0)

### Domain: Paywall (flagship, production-ready)
- 16 modules under `modules/`
- Python calculator in `tools/`
- Audit checklist + migration playbooks in `docs/`
- 3 worked examples in `examples/`
- 79 sourced benchmarks + 20-concept academic foundation

### Shared (cross-domain)
- `modules/pricing-psychology.md` — 20 academic concepts. **Applies to any subscription-app domain**, not just paywalls.
- `modules/glossary.md` — subscription metrics glossary.
- `sources.json` — evidence manifest.

---

## Planned expansion (by priority)

### Priority 1 — Onboarding (v5.0)

The most natural expansion. We already have `onboarding-paywall-handoff.md` (paywall-facing subset).

**Planned modules:**
- `modules/onboarding/patterns.md` — quiz vs tutorial vs demo vs hybrid; 15+ patterns from Noom / Flo / Cal AI / Duolingo / Headspace / Strava / ChatGPT full-flow analysis
- `modules/onboarding/copy-library.md` — onboarding-specific headline formulas, progress copy, loading-screen copy, segmentation questions
- `modules/onboarding/teardowns.md` — full-flow analyses (not just paywall-facing) of top apps
- `modules/onboarding/compliance.md` — ATT timing, push permission timing, GDPR/COPPA for quiz data collection, privacy-prompt patterns
- `modules/onboarding/metrics.md` — completion rate, step-by-step drop-off, aha-moment measurement, cohort analysis for onboarding variants
- `modules/onboarding/decision-trees.md` — length decision, personalization decision, gating decision
- `examples/audit-onboarding-*.md` — worked examples per category

**Expected release:** v5.0.0

### Priority 2 — Retention & Lifecycle (v6.0)

Goes beyond paywall-lifecycle (we already cover notifications, refunds, cohorts). Full retention domain:

- `modules/retention/habit-loops.md` — trigger + action + reward + investment, behavioral basis (Fogg, Eyal), measurement
- `modules/retention/streaks.md` — streak design (Duolingo, Strava), psychological basis (goal-gradient, sunk cost)
- `modules/retention/churn-prevention.md` — leading indicators, intervention timing
- `modules/retention/win-back.md` — beyond paywall: email + push + App Store win-back surfaces
- `modules/retention/grace-period-ux.md` — billing failure recovery
- `modules/retention/dunning.md` — payment retry orchestration

**Expected release:** v6.0.0

### Priority 3 — Growth & Acquisition (v7.0)

We have `cac-acquisition.md` as paywall-context CAC. Full growth domain:

- `modules/growth/aso.md` — App Store Optimization (keyword research, metadata, visuals)
- `modules/growth/asa.md` — Apple Search Ads tactics (we briefly cover)
- `modules/growth/paid-ua.md` — Meta / TikTok / Google playbook with creative testing
- `modules/growth/web2app.md` — web acquisition → app activation
- `modules/growth/attribution.md` — MMP setup, SKAN, conversion value configuration
- `modules/growth/virality.md` — K-factor, referral mechanics, sharing loops

**Expected release:** v7.0.0

### Priority 4 — Pricing Strategy (standalone domain, not just paywall tactics) (v8.0)

Currently pricing-psychology lives inside paywall context. Separate domain:

- `modules/pricing/tier-design.md` — 2 vs 3 vs 4 tier decisions with cross-category data
- `modules/pricing/geo-pricing.md` — beyond `localization.md`; PPP, currency risk, regional elasticity
- `modules/pricing/dynamic-pricing.md` — segment-based pricing, intent-tiered
- `modules/pricing/price-testing.md` — how to test prices without breaking App Store Connect
- `modules/pricing/hybrid-monetization.md` — subs + IAP + one-time unlocks

**Expected release:** v8.0.0

### Priority 5 — Review & Reputation Management (v9.0)

- `modules/reviews/prompt-timing.md` — when to ask for rating (Apple's SKStoreReviewController)
- `modules/reviews/response-playbook.md` — replying to bad reviews; scripts per category
- `modules/reviews/recovery-flow.md` — turning 1-star into 5-star via in-app support
- Link to **Negativity Bias** (already covered in Layer 2 foundations)

**Expected release:** v9.0.0

---

## Architecture evolution

### Current (v4.0) — flat with domain prefixes in filenames where needed

```
modules/
  paywall-*.md          ← paywall-specific (most files)
  pricing-psychology.md ← shared foundations
  glossary.md           ← shared
tools/
  ltv-calculator.py
docs/
  audit-checklist.md    ← paywall-specific
  migrations/           ← paywall-specific
examples/
  audit-*-app.md        ← paywall-specific
outputs/                ← research briefs
```

### Future (v5.0+) — domain folders

```
domains/
  paywall/
    modules/
    docs/
    examples/
    tools/
  onboarding/
    modules/
    docs/
    examples/
    tools/
  retention/ ...
  growth/ ...
shared/
  foundations/          ← pricing-psychology.md + glossary.md + sources.json
  decision-trees/       ← cross-domain how-to-navigate
  evidence-ladder.md    ← canonical reference for all domains
outputs/                ← cross-domain research briefs
```

### Migration strategy
- **v4.0 keeps current flat structure** — no breakage
- **v5.0 introduces `domains/` folder** alongside existing files; symlinks or re-export for backward compat
- **v6.0** completes migration; old paths deprecated with redirect notes
- **v7.0** removes deprecation notices; fully migrated structure

Claude Code / ChatGPT / Cursor installations continue to work throughout — the core `SKILL.md` entry point stays stable at repo root.

---

## Non-goals (intentionally NOT on roadmap)

- **Generic web CRO.** This framework is mobile-subscription-first. Web landing pages have different compliance (no Apple), different testing (no statistical-sig constraints at mobile scale), different buyer psychology. Out of scope.
- **Enterprise B2B sales processes.** B2B subscription has different sales cycles, procurement layers, legal negotiation. Some principles transfer; the framework won't specialize for it.
- **AI-app feature design.** We discuss AI category paywall economics. We don't advise what AI features to build.
- **Original academic research.** We curate and apply existing peer-reviewed research. We don't publish novel studies.
- **Competing vendor SDK.** We stay framework-agnostic. Works with Adapty / RevenueCat / Superwall / Apphud — doesn't replace any.

---

## Contribution targets by domain

When community PRs open up, these are the highest-value contributions per planned domain:

| Domain | Most-wanted contribution |
|--------|------------------------|
| Paywall (v4) | Additional big-app teardowns (with screenshots + sources) |
| Onboarding (v5) | Cohort data from real app before-after quiz redesigns |
| Retention (v6) | Habit-loop case studies with cohort math |
| Growth (v7) | Channel-level LTV:CAC data by geo |
| Pricing (v8) | A/B results from price tests (with sample size) |
| Reviews (v9) | Per-category response scripts that actually recovered ratings |

---

## Versioning policy

- **Major (X.0.0):** new domain added OR breaking structural change (file moves requiring users to re-clone)
- **Minor (x.Y.0):** new modules within existing domains, new tools, significant data refresh
- **Patch (x.x.Z):** corrections, small additions, documentation polish

All releases tagged on GitHub with notes. Installation paths remain stable across minor/patch; major releases document migration steps.

---

## Where we won't sprint ahead

- **Onboarding v5 won't ship until paywall v4 is fully validated in the wild.** Real user feedback on whether the modular structure works first.
- **Retention v6 waits on at least 2-3 major onboarding pattern releases** so we don't introduce domain without shipping previous one cleanly.
- **Growth v7 requires MMP data partnerships** to ship with real benchmarks, not just principle-level guidance.

Shipping the framework well in one domain > shipping three domains shallow.
