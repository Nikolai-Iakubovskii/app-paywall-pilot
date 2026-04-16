# Android / Play Billing Parity

SKILL.md is iOS-first by default. This module covers Play-specific differences.

Per AppsFlyer 2026: **Android subscription UA spend grew 4x faster than iOS YoY**, with Indian Subcontinent driving 49% of net Android paid install growth. Android is no longer the afterthought.

---

## Play Billing Library Concepts

| iOS | Android (Play Billing v6+) |
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

### Toggle paywall (Play stance)

**Apple banned toggle paywalls in Jan 2026 (Guideline 3.1.2). Play has not issued an equivalent rejection wave.** Toggle paywalls remain technically allowed on Android — but for cross-platform consistency, removing them everywhere is recommended.

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

Apple allows external web checkout in US (post Epic v. Apple, May 2025).
Play allows external web checkout globally (post Google v. Epic settlement) with restrictions.

**Best practice:**
- Show web option only on Android in EU/US where law allows
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
- Play subscription policies: https://support.google.com/googleplay/android-developer/answer/12089935
- AppsFlyer 2026 (Android growth): https://www.appsflyer.com/resources/reports/subscription-marketing/
- RevenueCat Play vs Apple cancellation rates: https://www.revenuecat.com/state-of-subscription-apps/
- EU DMA on alternative billing: https://digital-markets-act.ec.europa.eu/
