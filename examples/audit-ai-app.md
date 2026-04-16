# Example Audit: AI App

Worked example for an AI category app. AI has unique economics — high price tolerance, fast churn, ChatGPT $20/mo benchmark.

For comparison, see [audit-h-and-f-app.md](audit-h-and-f-app.md) and [audit-productivity-app.md](audit-productivity-app.md).

---

## Input

**Hypothetical app:** "ScribeAI" — AI-powered note-taking and meeting transcription. iOS + Android, US + EU + APAC.

**Current state:**
- Onboarding: 8 screens (use case, source picker, sample import)
- Paywall: post-onboarding, 3 plans (monthly $14.99, annual $99.99, lifetime $199), 7-day trial on all
- Free tier: 5 transcriptions / month
- Markets: US 60%, EU 25%, APAC 15%
- Metrics: install→trial 14%, trial→paid 22%, monthly churn 8%, refund rate 7.4%

---

## Audit Output

### 1. Current state

AI category, freemium-with-meter (5/month) → post-aha hard paywall with 3 plans. Trial on all plans. Pricing slightly **above ChatGPT baseline** ($14.99 vs $20 Plus) — competitively positioned.

Trial→paid 22% is **below 27.8% global benchmark** but reasonable for AI (RC 2026 notes AI churns 30% faster than category avg). Refund rate 7.4% is **elevated** vs ~4-5% expected.

### 2. Main problem or opportunity

**Trial-on-all-plans is the issue.** Adapty Operator Insight: trial-on-annual-only is one of the most consistent winning patterns. Math: weekly/monthly trial subscribers retain 5.5-17% D380 vs annual 19.9%. Trial on monthly subsidizes lower-LTV cohort.

Secondary: refund rate 7.4% suggests overpromise on paywall OR users not hitting AI value in first 7 days. AI users expect immediate magic; if first transcription has issues, they refund fast.

### 3. Recommended access model

Keep **freemium with metered free tier** (5 transcriptions/month). AI is the canonical metered category — Apple Guidance documents it as valid acquisition model. Layer a **hard paywall after first transcription completes** (post-aha placement).

### 4. Recommended placements

- **Post-aha paywall (primary):** after first successful transcription. The user has felt the magic; show paywall with personalized "Your first transcription was X words" framing.
- **Usage limit (secondary):** when user hits 5/month free limit, show upgrade prompt.
- **Onboarding paywall (light test):** for high-intent users (e.g., signed in with corporate email), test direct hard paywall.
- **Renewal-risk:** AI users are price-sensitive; promotional offer at -25 days.
- **Win-back:** Apple Win-Back Offer (iOS 18+) — AI churns fast; win-back is critical for LTV.

### 5. Recommended presentation

**Demo + post-aha paywall.** AI apps need to show the value, not describe it.

```
┌────────────────────────────────────┐
│ [X close]                          │
│                                    │
│ Your transcript is ready.          │ ← personalized, post-aha
│ Get unlimited transcriptions.      │
│                                    │
│ ★★★★★ 4.7 — Used by 50K+ teams  │
│                                    │
│ Annual                Monthly       │ ← 2 plans (drop lifetime)
│ ✓ $99.99/yr           $14.99/mo    │
│   $1.92/wk            (no trial)   │
│   7-day free trial                  │
│                                    │
│ [Start free trial]  [Buy monthly]  │
│                                    │
│ Maybe later                        │
│                                    │
│ Restore · Terms · Privacy          │
└────────────────────────────────────┘
```

### 6. Screen content

**Headline (Outcome-led, post-aha personalization):**
- "Your transcript is ready."
- Sub: "Get unlimited transcriptions for [meetings / lectures / interviews]."

**Benefit bullets (5 max, AI-specific):**
- Unlimited transcriptions per month
- Multi-speaker detection with names
- Search across all your transcripts
- Export to Notion / Obsidian / Markdown
- 90-day retention with full edit history

**Pricing block:**
- Annual selected by default ($99.99/yr, ~$1.92/wk)
- Monthly secondary ($14.99/mo, no trial)
- Lifetime removed — was cannibalizing annual LTV

**CTA:**
- Primary: "Start free trial" (annual selected → trial applies)
- Secondary: "Buy monthly"
- Decline: "Maybe later"

### 7. Copy variants (2-3)

**Variant A (post-aha, personalized):**
- Headline: "Your transcript is ready."
- Sub: "Get unlimited transcriptions."

**Variant B (use-case-led):**
- Headline: "Never forget what was said."
- Sub: "AI transcription for every meeting."

**Variant C (outcome-led, time-to-value):**
- Headline: "Type 0 words. Capture every meeting."
- Sub: "AI does the work."

### 8. Layout sketch

Above-fold: close X, post-aha headline, social proof, 2 plan cards (annual default), CTA. Scroll: full benefit list, comparison Free vs Pro, integrations logos (Notion, Obsidian, Slack), FAQ, Restore Purchase / Terms / Privacy.

### 9. Localization notes

- **Localize for top 5 AI markets:** US, UK, DE, JP, AU.
- **Pricing tier (manual per-territory):**
  - US: $99.99/yr (current)
  - UK: £79.99/yr
  - DE/FR: €89.99/yr (1.2x EU lift)
  - JP: ¥12,800/yr (~$87)
  - AU: A$129/yr
- **APAC consideration:** ChatGPT Go @ $8/mo launched in India shows emerging-market geo-tier is the play. If APAC >15% of installs, consider a $29/yr APAC tier or weekly $1.99 entry product.
- **CTA length:** "Start free trial" (16 char) fits all locales.

### 10. Tests to run

| # | Hypothesis | Primary metric | Guardrail |
|---|-----------|---------------|-----------|
| 1 | Trial-on-annual-only vs trial-on-all-plans lifts LTV per cohort | 12-mo cohort LTV | Trial start rate |
| 2 | Drop lifetime plan (was cannibalizing annual). Test removing | Total LTV | Conversion |
| 3 | Post-aha placement vs onboarding placement | LTV per install | Install→trial |
| 4 | Personalized headline (transcript word count) vs generic | Trial start rate | Trial→paid |
| 5 | APAC geo-tier ($29/yr) test in IN/SEA | Revenue per APAC install | Refund rate |

### 11. iOS review risks

**Compliant ✓:**
- 2-plan layout (no toggle) ✓
- Billed amount most prominent ✓
- Trial terms next to plan ✓
- Restore + Terms + Privacy ✓

**Watch:**
- ⚠️ AI apps face emerging Apple scrutiny for accuracy claims. Don't claim "100% accurate" — Apple may flag misleading
- ⚠️ Privacy policy must address whether transcripts are used for AI training (GDPR + Apple Privacy)
- ⚠️ When dropping lifetime, existing lifetime users retain access (Apple Rule on previously-purchased)

### 12. Android delta

- **Apphud / Adapty / RC** all support cross-platform; entitlements should sync via your subscription SDK
- **Web2App opportunity:** AI apps have strong content/SEO play (blog posts on use cases). Add web checkout for US (post-Epic ruling) — some AI apps report 65-120% revenue lift bypassing 30% cut
- **Play Billing:** Trial as Offer attached to annual Base Plan (not on monthly Base Plan)

---

## Calculator Output

### Current state (3 plans, trial on all)
- CR: 14% × 22% = 3.08%
- CPI: $3 (assumed)
- 12-mo ARPU: ~$48 (with monthly + lifetime mix)
- LTV:CAC: ~1.6:1

### Recommended state (2 plans, trial-on-annual-only, drop lifetime)
- Trial start: 12% (slight drop without monthly-trial), Trial-to-paid: 32% (lift from focused trial)
- Effective CR: 3.84%
- 12-mo ARPU: ~$58 (annual-heavy mix)
- LTV:CAC: ~2.5:1

### Top 3 actions
1. Move trial to annual-only; remove from monthly. Drop lifetime entirely.
2. Reposition paywall to post-aha (after first transcription completes).
3. Localize prices for EU + JP + AU (15-20% blended ARPU lift).
