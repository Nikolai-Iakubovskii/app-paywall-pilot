# Subscription Compliance Watchlist (late 2026)

Store and law changes that hit paywalls, trials, renewals and cancellation, plus code scans to run before submission. Load in `compliance` and `audit` modes when the app ships to the EU, UK or US, uses Play Billing, or uses external purchase links.

Evidence class: `apple_docs` / `platform_capability` / regulation, each with its primary link. Dates were cross-checked against the open [mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance) tracker (release 2.4.0, 2026-11-15). That repo is under the OpenRoots Agent License; nothing here is copied from it, only primary sources are cited. Open the primary link before giving a dated verdict: several items below were still provisional on 2026-11-15.

---

## 1. Dated obligations

| Effective | Market | What changes for the paywall / subscription | Primary source |
|---|---|---|---|
| In force since 2026-06-19 | EU | Directive (EU) 2023/2673 adds a mandatory **withdrawal function** for distance contracts made in an online interface, apps included. Label like "withdraw from contract here", prominently displayed and easy to reach for the whole 14-day withdrawal period, then a confirmation step and a durable-medium receipt. Store-billed IAP: the store handles the contract, but web/Stripe subscriptions need it in-app or on the account page. | [EUR-Lex 2023/2673](https://eur-lex.europa.eu/eli/dir/2023/2673/oj) |
| Since 2026-09-16 | Apple, global | **Multiseat purchases are on by default** for auto-renewable subscriptions in App Store Connect. Volume Purchasing via Apple Business / School Manager since 2026-10-22, Group Purchases this winter. For each subscription decide: allow, limit, or disable. A single-user entitlement sold as multiseat breaks entitlement logic and refund rates. | [Apple news likeohx4](https://developer.apple.com/news/?id=likeohx4) |
| New apps/updates since 2026-08-31 (extension ended 2026-11-01) | Google Play | **Play Billing Library 8+** required to publish. All published apps by 2027-08-31, v9 by 2028-08-31. | [Billing deprecation FAQ](https://developer.android.com/google/play/billing/deprecation-faq) |
| Orders after 2026-08-03 | Google Play | Google **no longer absorbs chargebacks**: developer pays price minus fee plus the card-network fee. Handle `PendingRefundReviewNotification` (RTDN) and answer via the Review Refund API within 24 h with usage evidence. | [Play Console 17068375](https://support.google.com/googleplay/android-developer/answer/17068375) |
| 2026-10-01 | Google Play, US | Apps in the US alternative billing / external links program must report transactions and pay the Play service fee. | [Play Console 16497028](https://support.google.com/googleplay/android-developer/answer/16497028) |
| 2026-10-01 | Apple, EU | Core Technology Fee replaced by 5% Core Technology Commission outside the App Store; alternative payments may sit next to IAP. Update unit economics, not paywall layout. | [Apple news gmws0jgp](https://developer.apple.com/news/?id=gmws0jgp) |
| Provisional 2027-01-01 | UK | **DMCCA subscription regime**: pre-contract information, renewal reminders, two cooling-off periods (start and after a free/discounted trial converts), easy cancellation, new refund rules. Exact day not made law on 2026-11-15. Whether store IAP shifts any duty to Apple/Google is not settled; assume the reminder and information duties are yours. | [GOV.UK announcement](https://www.gov.uk/government/news/pm-starts-roll-out-of-everyday-fixes-on-the-cost-of-living-ending-rip-off-discounts-and-subscription-traps) |
| 2027-01-27 | Google Play | Subscriptions with an **ongoing eligibility discount** (student, etc.) must state eligibility criteria, how it is verified, and the price and benefits after eligibility ends — on the paywall. | [Play policy table](https://support.google.com/googleplay/android-developer/table/12921780) |
| Proposed 2026-11-11, applies 12 months after entry into force | EU | **Digital Fairness Act** (COM(2026) 1100). No obligation yet. Design now for: reminder before a free trial converts, express consent to convert, no dark-pattern pricing. Our Day -3 trial reminder already fits. | [Commission proposal](https://commission.europa.eu/document/download/0575d59f-554f-4a9e-b54b-e6b717175809_en?filename=Proposal+for+a+Digital+Fairness+Act.pdf) |

Standing rules that keep getting rejected:

- **US external purchase link carve-out is US storefront only.** The same button is a 3.1.1 rejection in JP, CA, AU, UK and elsewhere. Gate on `Storefront.current?.countryCode`. Since 2026-10-16 the music streaming entitlement folded into the StoreKit External Purchase Link Entitlement in 3.1.1(a). [Apple news 9txfddzf](https://developer.apple.com/news/?id=9txfddzf)
- **Cancellation outside store billing** (web / Stripe) must be self-serve and no harder than sign-up. Federal FTC click-to-cancel was vacated in 2025, but California, New York and Massachusetts laws plus FTC ROSCA still apply. Never "call / email us to cancel".
- **Apple price increases** in Austria, Germany, Poland need customer consent (already in [audit-checklist.md](audit-checklist.md) section 8).

---

## 2. Pre-submission code scans

Run from the app repo root. A hit is a lead to inspect, not a verdict. Each scan pairs a risk signal with the counter-signal that means it is handled.

```bash
# R1. Paid content but no restore path (Apple 3.1.1; required for non-consumables and non-renewing subs)
grep -rlE '\.purchase\(|SKProduct|makePurchase|purchasePackage|Adapty\.makePurchase|buyNonConsumable' --include='*.swift' --include='*.dart' --include='*.kt' --include='*.ts' --include='*.tsx' . \
  && ! grep -rqE 'AppStore\.sync|restoreCompletedTransactions|restorePurchases|restoreTransactions' --include='*.swift' --include='*.dart' --include='*.kt' --include='*.ts' --include='*.tsx' . \
  && echo 'R1: no restore call found'

# R2. External payment SDK for digital goods (Apple 3.1.1 / Play Payments)
grep -rnE 'Stripe|PayPal|braintree|razorpay|paddle' --include='*.swift' --include='*.kt' --include='pubspec.yaml' --include='package.json' --include='*.gradle*' --include='Podfile' .

# R3. External purchase link without storefront gating (US-only carve-out)
grep -rqE 'ExternalPurchaseLink|openExternalPurchaseLink|external-purchase-link' . \
  && ! grep -rqE 'Storefront|storefront|countryCode' --include='*.swift' --include='*.dart' . \
  && echo 'R3: external link not gated by storefront'

# R4. Play Billing Library below 8 (publishing gate)
grep -rnoE 'com\.android\.billingclient:billing(-ktx)?:[0-7]\.' --include='*.gradle' --include='*.kts' --include='*.toml' .

# R5. Play billing with no chargeback dispute handling (revenue exposure, not a rejection)
grep -rqE 'BillingClient|com\.android\.billingclient|purchases\.subscriptionsv2' . \
  && ! grep -rqiE 'pendingRefundReview|reviewRefund' . \
  && echo 'R5: no PendingRefundReviewNotification / Review Refund handling (check backend repo too)'

# R6. Hard-cancel copy for web subscriptions (ROSCA / state law / EU withdrawal)
grep -rniE '(call|email|write|mail).{0,25}to cancel|cancel.{0,20}(by phone|by mail|in person)' --include='*.swift' --include='*.dart' --include='*.kt' --include='*.arb' --include='*.json' --include='*.html' --include='*.strings' .
```

RevenueCat / Adapty: a server-side RTDN integration may handle R5 for you; confirm in the provider dashboard before flagging.

Manual checks that grep cannot do:

- **Billed amount vs per-month figure.** The amount charged per period must be at least as prominent as any "$X/month" equivalent (3.1.2(c)). Measure font size and weight in the screenshot.
- **Eligibility-discount disclosure** (Google, from 2027-01-27): criteria, verification, post-eligibility price on the same screen.
- **Multiseat setting** per subscription in App Store Connect.
- **EU web subscriptions:** withdrawal function visible on the account page during the 14 days.

---

## 3. Routing

| Signal | Do |
|---|---|
| App sells to EU consumers outside store billing | Section 1 EU rows + R6, add withdrawal function to the audit |
| App ships to UK | DMCCA row; plan renewal reminder and post-trial cooling-off copy now |
| Android target | R4 + R5 + eligibility-discount row, then [android-parity.md](../modules/android-parity.md) |
| External link / web checkout | R2 + R3, then [audit-checklist.md](audit-checklist.md) section 8 |
| Rejection already received | [decision-trees.md](../modules/decision-trees.md) Tree 8 first, this file second |
