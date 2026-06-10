# Android / Play Billing Parity

SKILL.md is iOS-first by default. This module covers Play-specific differences.

Per AppsFlyer 2026: **Android subscription UA spend grew 4x faster than iOS YoY**, with Indian Subcontinent driving 49% of net Android paid install growth. Android is no longer the afterthought.

---

## Play Billing Library Concepts

Use Play Billing Library 9.0.0+ for new Android implementation work when possible. PBL 9 was released May 19, 2026, adds richer error context through sub-response codes, and removes previously deprecated APIs. If an app is on PBL 7/8, check the PBL 9 migration guide before touching billing code.

| iOS | Android (Play Billing v9) |
|-----|---------------------------|
| Subscription Group | Base Plan + Offers |
| Introductory Offer | Offer eligibility (NEW_SUBSCRIBER, etc.) |
| Promotional Offer | Promotion code or developer-determined offer |
| Offer Codes | Promo codes |
| Win-Back Offers | Re-entry offer (separate setup) |
| StoreKit 2 transactions | Play Billing PurchaseResponse |
| App Store Server Notifications V2 | Play Developer Notifications (RTDN) |

### Base Plan vs Offer

Play's mental model is:
- **Base Plan:** the recurring product (annual, monthly)
- **Offers:** modifications layered on (free trial, intro discount)

You can have **multiple offers per base plan**, eligible for different audiences (new subscriber, existing, etc.).

### Subscription configuration

```
Subscription
├── Base Plan: monthly_premium ($9.99/month)
│   ├── Offer: 7-day free trial (NEW_SUBSCRIBER)
│   └── Offer: 50% off month 1 (EXISTING_NON_SUBSCRIBER)
└── Base Plan: annual_premium ($59.99/year)
    └── Offer: 14-day free trial (NEW_SUBSCRIBER)
```

---

## Play-Specific Compliance

### Play policy parallels to App Store

- Clear pricing and renewal terms (similar to Apple Rule 3.1.2)
- Restore purchases supported
- Cancellation easily accessible
- No dark patterns / forced subscription

### Play unique requirements

- **EU Digital Markets Act (DMA):** Android in EU must allow alternative billing systems for in-app purchases. Different from US/global.
- **Play Console "Subscription Center":** users can manage subs from Play Store, not just in-app.
- **Grace Period + Account Hold:** Play has 30-day grace period for failed payments by default. Implement notifications for both.
- **Age Signals / in-app product age ratings:** Google Play is adding support for applicable US state app-store bills. If the app targets minors or sells age-sensitive IAP/subscriptions, check Play Age Signals API and in-app product age rating requirements.

### Toggle paywall (Play stance)

**Apple banned free-trial toggle paywalls on iOS in Jan 2026 through Guideline 3.1.2 enforcement. Play has not issued an equivalent rejection wave.** Toggle paywalls remain technically allowed on Android, but for cross-platform clarity and lower support risk, replacing them everywhere is recommended.

---

## Android Refund Reality

**RevenueCat 2026:**
- Google Play involuntary billing failures: ~31% of cancellations
- App Store: 14%

Android has higher payment failure rate due to:
- Carrier billing in emerging markets
- Wider variety of payment methods (UPI, Boleto, etc.)
- Less uniform card requirements

**Implication:** Implement payment retry UX. Show grace period clearly. Don't lose subscribers to silent payment failures.

---

## Trial Mechanics

### Free trial via Play Billing

```kotlin
// Pseudo-config
ProductDetails subscription = ...
SubscriptionOfferDetails offer = subscription.subscriptionOfferDetails
   .firstOrNull { it.basePlanId == "annual_premium" && it.offerId == "free_trial_14d" }
```

### Trial eligibility

Play tracks eligibility per offer. A user who has used a "NEW_SUBSCRIBER" offer cannot get it again. Different from App Store, which uses one-trial-per-subscription-group.

---

## Win-Back / Re-entry

Apple has native Win-Back Offers (iOS 18+) shown on the App Store product page.

**Play equivalent:**
- No native off-app surface
- Must implement in-app via re-entry detection (user opens app, was previously subscribed but lapsed)
- Use a Promotional offer with EXISTING_NON_SUBSCRIBER eligibility

---

## Web Checkout (Cross-Platform)

Apple allows external purchase flows in more region-specific ways than it did before: US changes followed the Epic v. Apple court decision, EU changes follow DMA terms, and Japan adds alternative payments/distribution options under MSCA beginning with iOS 26.2. Treat this as a regional compliance surface, not a global paywall default.
Play allows external web checkout globally (post Google v. Epic settlement) with restrictions.

**Best practice:**
- Show web option only in storefronts where the current Apple/Google terms allow it
- Apple Pay / Google Pay buttons prominent
- Disclose: "External purchase — handled by [your company], not Apple/Google."

---

## Tooling

| Tool | iOS | Android |
|------|-----|---------|
| RevenueCat | ✅ | ✅ |
| Adapty | ✅ | ✅ |
| Superwall | ✅ | ✅ (newer) |
| Apphud | ✅ | ✅ |
| Native (StoreKit 2) | ✅ | — |
| Native (Play Billing) | — | ✅ |

All major SDKs unify the API. Use one — don't write Play Billing or StoreKit by hand unless you have a specific reason.

---

## Android-Specific Patterns That Don't Translate to iOS

- **Pre-paid plans** (Play has explicit support; iOS doesn't)
- **Custom SKU offers** with non-Apple-allowed structures
- **Carrier billing flows** (visible in Play Console; not on Apple)

---

## Source Pointers

- Play Billing Library: https://developer.android.com/google/play/billing
- Play Billing Library 9 release notes: https://developer.android.com/google/play/billing/release-notes
- PBL 9 migration guide: https://developer.android.com/google/play/billing/migrate-gpblv9
- Google Play age signals / in-app product age ratings: https://support.google.com/googleplay/android-developer/answer/16569691
- Play subscription policies: https://support.google.com/googleplay/android-developer/answer/12089935
- AppsFlyer 2026 (Android growth): https://www.appsflyer.com/resources/reports/subscription-marketing/
- RevenueCat Play vs Apple cancellation rates: https://www.revenuecat.com/state-of-subscription-apps/
- EU DMA on alternative billing: https://digital-markets-act.ec.europa.eu/
- Apple Japan iOS changes: https://developer.apple.com/news/
