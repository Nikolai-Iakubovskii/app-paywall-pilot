# Pre-Ship Audit Checklist

Printable / standalone checklist version of the SKILL.md audit. Use when you don't have AI access or want a manual review pass before submitting an App Store update.

50+ items grouped into 7 sections. Each item references the SKILL.md / module section that explains why.

---

## 1. Apple Compliance (rejection-blockers)

These are Apple Rules. Failing any = likely rejection.

- [ ] Clear description of what user gets (Guideline 3.1.2(c))
- [ ] Subscription name and duration visible (3.1.2(c))
- [ ] **Full renewal price is the most prominent pricing element** (3.1.2(c))
- [ ] Trial duration AND post-trial price shown if trial offered (3.1.2(a))
- [ ] Restore Purchases accessible (in-app, not buried)
- [ ] Terms of Use link in-app (clickable, not just text)
- [ ] Privacy Policy link in-app (clickable, not just text)
- [ ] No misleading savings math (every "save X%" verifiable against real reference price)
- [ ] No fake urgency / countdown not tied to real expiry
- [ ] No fake reviews / ratings / user counts
- [ ] Existing paid users keep previously purchased access (no entitlement breakage)
- [ ] **No toggle paywall** (Apple Guideline 3.1.2 mass rejections since Jan 2026)
- [ ] No deceptive plan pre-selection
- [ ] Auto-renewal terms disclosed clearly

References: SKILL.md iOS COMPLIANCE CHECKLIST + [decision-trees.md](../modules/decision-trees.md) Tree 8.

---

## 2. Field Reports (high rejection-correlation, not Apple-published)

Not formal rules, but observed rejection patterns.

- [ ] Pricing font ≥16pt (RevenueFlo field threshold)
- [ ] Close button visible immediately (NOT delayed >5s)
- [ ] No two full paywalls back-to-back (use soft prompt instead — Superwall pattern)
- [ ] Decline copy is neutral ("Maybe later" / "Not now"), not guilt-trip
- [ ] No hidden close button

References: [decision-trees.md](../modules/decision-trees.md) Tree 8.

---

## 3. Copy Quality

- [ ] Headline is outcome-led, not feature-led ("Sleep better in 7 nights" not "Premium Features")
- [ ] CTA uses action+benefit pattern ("Start my free week", not "Subscribe")
- [ ] 3-5 benefit bullets max
- [ ] Each bullet ≤8 words
- [ ] No banned words: "Premium" alone, "Subscribe" generic, "Unlock", "Pay"
- [ ] Real social proof above the fold (rating + count, real testimonial, or authority)
- [ ] Trust line includes trial terms + billed amount + restore + terms + privacy
- [ ] Onboarding promise referenced in paywall headline (continuity check)

References: [copy-library.md](../modules/copy-library.md) + [onboarding-paywall-handoff.md](../modules/onboarding-paywall-handoff.md).

---

## 4. Pricing & Plan Architecture

- [ ] 1-3 plans visible (Adapty 2026: 2-plan paywalls 41-60% of apps; 3-plan via Superwall +44%)
- [ ] Selected plan is visually clear (border + badge + background)
- [ ] Annual default if annual LTV > 2x monthly
- [ ] Per-day / per-week breakdown is subordinate to billed amount
- [ ] Trial on annual only (or all plans, with clear reason)
- [ ] Savings math verifiable against reference price
- [ ] Pricing tier appropriate for category (compare to [category-deep-dives.md](../modules/category-deep-dives.md))
- [ ] Apple Small Business Program enrolled if eligible (<$1M annual revenue → +17.6% net ARPU)

References: [pricing-psychology.md](../modules/pricing-psychology.md) + [category-deep-dives.md](../modules/category-deep-dives.md).

---

## 5. Localization

- [ ] Localized for top 5 revenue markets minimum
- [ ] Manual per-territory pricing for top markets (not just auto-tier)
- [ ] EU pricing 20-30% above NA (capture surplus)
- [ ] Geo-tier consideration for emerging markets >5% of installs (e.g., India, Indonesia)
- [ ] Number formatting localized (€/¥/$/₽ in correct positions)
- [ ] CTA text fits in button at longest locale (DE +30-40% vs EN)
- [ ] Tone matches market expectation (Sie/du in German, vous in French, formality in Japanese)
- [ ] RTL flip tested for Arabic/Hebrew if shipping in MENA

References: [localization.md](../modules/localization.md). Adapty 2026: localization = 62.3% LTV win rate (highest).

---

## 6. Accessibility & Layout

- [ ] Above-fold contains: close X, headline, plan card, CTA
- [ ] Primary CTA in thumb zone (bottom third)
- [ ] WCAG AA contrast on CTA (4.5:1 minimum)
- [ ] Tap targets ≥44pt (Apple HIG)
- [ ] Dynamic Type tested up to AX5
- [ ] VoiceOver labels on all interactive elements
- [ ] Reduce Motion respected
- [ ] Dark mode tested
- [ ] Safe areas respected (status bar, dynamic island, home indicator)
- [ ] No information conveyed by color alone (colorblind users)

References: [screen-anatomy.md](../modules/screen-anatomy.md).

---

## 7. Implementation & Lifecycle

- [ ] Restore Purchase implemented and tested
- [ ] Already-entitled user handled (don't show paywall to active subscriber)
- [ ] Network failure UX (specific copy: "Couldn't connect. Try again.")
- [ ] Purchase cancellation UX (silent return, no friction)
- [ ] Analytics events fired: paywall_impression, dismissed, plan_selected, purchase_started/completed/failed
- [ ] Server Notifications V2 wired (App Store) / RTDN (Play)
- [ ] Trial reminder push at Day -3 / Day -1 (Blinkist pattern)
- [ ] Renewal-risk push at Day -25 if auto-renew turned off
- [ ] Win-back offer configured (Apple Win-Back iOS 18+)
- [ ] Refund consumption API implemented for refund decline
- [ ] MMP integrated (AppsFlyer / Adjust / Singular) for channel-level CAC
- [ ] Cohort dashboards set up (RC / Adapty / Apphud)

References: [notifications-lifecycle.md](../modules/notifications-lifecycle.md), [refund-management.md](../modules/refund-management.md), [cohort-analysis.md](../modules/cohort-analysis.md), [cac-acquisition.md](../modules/cac-acquisition.md), [android-parity.md](../modules/android-parity.md).

---

## Quick Triage

If you can only check 10 items, check these:

1. ✅ Toggle paywall removed (post Jan 2026 ban)
2. ✅ Billed amount most prominent
3. ✅ Trial terms + post-trial price visible
4. ✅ Restore Purchase / Terms / Privacy links
5. ✅ Headline outcome-led
6. ✅ Trial reminder Day -3 push wired
7. ✅ Localized for top 5 markets
8. ✅ Apple SBP enrolled if eligible
9. ✅ Onboarding promise matches paywall headline
10. ✅ MMP integrated

---

## Use This Checklist

- **Before App Store submission** — full pass
- **After ANY paywall change** — Section 1, 2, 3 minimum
- **Quarterly** — re-check Section 5 (localization), Section 7 (lifecycle), Section 4 (pricing tier vs category)
- **After rejection** — focus on Sections 1 + 2 with [decision-trees.md](../modules/decision-trees.md) Tree 8

---

## Source

Full reasoning behind each item: SKILL.md + the module references inline. This checklist is a fast pass; the modules are the depth.
