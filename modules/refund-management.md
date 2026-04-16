# Refund Management

Refunds are a controllable variable, not a fixed cost. This module covers refund baselines, prevention patterns, App Store / Play tooling, and what to do when refund rate spikes.

For lifecycle messaging that prevents refunds, see [notifications-lifecycle.md](notifications-lifecycle.md). For pricing patterns that affect refund rates, see [pricing-psychology.md](pricing-psychology.md).

---

## 2026 Refund Baselines

Source: Adapty 2026 + RevenueCat 2026. Cross-referenced.

| Plan / segment | Refund rate | Notes |
|----------------|-------------|-------|
| Weekly (no trial) | ~2.6% | Lowest |
| Monthly | ~3.2% | |
| Annual | ~4.2% | Highest baseline |
| Photo & Video APAC | up to 14.1% | Korea consumer-friendly refund policies |
| Trial-to-paid converts | varies; +trial often = +refund | Trial subsidizes "I forgot to cancel" |

Anything above category baseline = warning sign.

### Involuntary Billing Failures (different from refunds)

| Platform | Failure rate of cancellations |
|----------|-------------------------------|
| Google Play | ~31% |
| App Store | 14% |

These are payment failures (card expired, insufficient funds), not user-initiated refunds. Reduce via grace period UX, not refund prevention.

---

## What Causes High Refunds

### 1. Trial → paid surprise
User forgot trial converts. They wake up to a charge. → refund request.

**Fix:** Day -3 / Day -1 reminder push (Blinkist Day-5 pattern: -55% complaints). See [notifications-lifecycle.md](notifications-lifecycle.md).

### 2. Overpromise on paywall
User bought based on a promise the app didn't deliver in the first session.

**Fix:** Audit headline + benefits. Reduce to what the trial actually delivers. Trial Timeline visual signals transparency.

### 3. Value not hit before refund window
Apple gives 14 days to refund (varies by region). If user doesn't experience value in first 14 days, refund is rational.

**Fix:** Onboarding to aha moment <3 minutes. Engagement push days 1-3. Pre-trial-end value summary.

### 4. Wrong audience (UA channel mismatch)
Paid traffic from misaligned creative attracts users who don't match the product.

**Fix:** Audit channel-level refund rate (need MMP — see [cac-acquisition.md](cac-acquisition.md)). Pause channels with >2x baseline refund.

### 5. Bot / fraud installs
SDK fraud or click farms generate fake purchases that get charged back.

**Fix:** AppsFlyer Protect360 / Adjust Fraud Prevention Suite. Stricter anti-fraud SDK settings.

### 6. Family Sharing confusion
User accidentally subscribed via Family member's account; cancellation feels like refund.

**Fix:** Clear Family Sharing copy on paywall. Apple Guidance: highlight Family Sharing as a feature.

---

## Refund Prevention Sequence

### In-app touchpoints (post-purchase)

| Day | Action |
|-----|--------|
| 0 | Welcome to Premium screen with "what to do first" |
| 1 | Engagement push: "You unlocked X — try Y next" |
| 3 | Value summary: "You've used X today" |
| 7 (annual) | Mid-month value report |
| Pre-renewal -7 | "Heads up: renews in 7 days" |
| Pre-trial-end -3 | "Trial ends in 3 days. Manage anytime." |

**Apple Rule:** Trial-end reminders are not just best practice — Apple recommends transparent renewal communication in the App Store Review Guidelines (3.1.2(c) spirit).

### Web touchpoints

- Email receipt with explicit next billing date
- Account/subscription management URL in email
- Customer support contact in trial confirmation

---

## When the User Asks for a Refund

### App Store

Apple owns the refund flow — you can't issue it directly. User goes to:
- reportaproblem.apple.com (web)
- Settings → Apple ID → Subscriptions (in-app)

You CAN:
- **Decline the refund** via App Store Connect (within 60 days of original transaction)
- **Provide consumption data** — Apple's Consumption API tells Apple how much the user actually used the subscription, which influences refund decisions
- **Reach out via your support channel** if user contacted you first

### Consumption API

```swift
// Implement to influence Apple's refund decisions
import StoreKit

func declineRefund(transaction: Transaction) async {
    let consumptionRequest = ConsumptionRequest(
        customerConsented: true,
        consumptionStatus: .substantiallyUsed,
        platform: .apple,
        sampleContentProvided: true,
        deliveryStatus: .deliveredOK,
        appAccountToken: transaction.appAccountToken,
        accountTenure: .moreThan300Days,
        playTime: .moreThan60Hours,
        lifetimeDollarsRefunded: .small,
        lifetimeDollarsPurchased: .small,
        userStatus: .active,
        refundPreference: .preferDecline
    )
    try await Transaction.beginRefundRequest(...)
}
```

Apple's algorithm weighs consumption signals heavily. Apps that report substantial usage have meaningfully lower refund grant rates.

### Play Store

Play's refund flow is more developer-controlled:
- Standard refund policy: 48 hours auto-refund window
- Beyond 48 hours: developer decides via Play Console
- For subscription cancellation refunds: prorated by default

---

## Refund Decline Strategy

### When to decline

- User clearly used the service substantially (consumption data supports it)
- User requested refund after charge for an annual that's been active >30 days
- User has refund history (chronic refunder)

### When NOT to decline

- User contacted you in good faith with a specific complaint
- Bug or service outage on your side
- User refunded within 48h of trial conversion (they probably forgot)
- High-LTV potential customer (one refund decline = lost lifetime relationship)

**Operator wisdom:** Decline refunds for the bottom 10% of refund requesters; approve the rest. Don't fight the marginal $30 — fight the chronic bots.

---

## Channel-Level Refund Analysis

You need an MMP (AppsFlyer / Adjust / Singular) to see refund rate by acquisition channel.

| Channel signal | Action |
|---------------|--------|
| Refund rate <1.5x baseline | Healthy |
| Refund rate 1.5-2x baseline | Audit creative — overpromise? |
| Refund rate >2x baseline | Pause channel; investigate fraud or audience mismatch |
| Specific creative >3x baseline | Pause that creative; keep others |

---

## Region-Specific Refund Patterns

### APAC (especially Korea)
Consumer protection laws make refunds easier. Adapty 2026: Photo & Video category in APAC = 14.1% refund rate. Plan accordingly:
- Don't push aggressive trials in Korea
- Show clearer trial terms
- Lower CPI ceilings (refund eats into LTV)

### EU (post-DMA)
Digital Markets Act introduced alternative billing on Android. Refund flows now vary by billing system used. Track refund rate per billing surface.

### IN/SEA
Lower refund rates baseline (~1.5-2%) but high involuntary failures. Different problem to solve. Focus on payment retry UX.

---

## Diagnostic Flowchart

```
Refund rate above baseline?
├── Annual >5%? → Likely value-not-delivered
│   └── Audit: aha moment time, week 2-4 engagement
│
├── Monthly >5%? → Likely surprise charge
│   └── Audit: trial reminder cadence, billing transparency
│
├── Specific channel >2x? → UA mismatch or fraud
│   └── Pause channel; investigate creative
│
├── Specific region >2x? → Refund-friendly market
│   └── Adjust pricing/trial structure for region
│
└── Recent spike across all → Production bug or service issue
    └── Investigate: app crashes, payment flow, entitlement bugs
```

---

## Refund vs Subscription Pause

Apple offers Subscription Pause (introduced iOS 14.5+) — better than refund for retention. User keeps their subscription record, just pauses billing for 1-3 months.

**When to suggest pause vs refund:**
- User says "too expensive right now" → suggest pause
- User says "doesn't work for me" → process refund (don't fight)
- User says "I'm traveling" → suggest pause

Pause is a Platform Capability — surface it in your support flow.

---

## Common Mistakes

| Mistake | Why bad |
|---------|---------|
| No consumption data implemented | Refunds approved automatically; you lose money |
| Auto-decline all refund requests | Triggers user retaliation (1-star reviews, chargebacks) |
| Same refund policy for all channels | Hides which channel is broken |
| Treating chargebacks like refunds | Different process, higher fees, must dispute via processor |
| Ignoring grace period for failed payments | Users churn silently when card expires |
| Aggressive paywall that maximizes immediate conversion | Trades short-term CR for long-term refund spike |

---

## Refund as Signal

A refund is feedback. Track refund REASONS in your support system. Patterns reveal product gaps:

| Reason cited | Likely fix |
|-------------|-----------|
| "Forgot to cancel" | Trial reminder cadence |
| "Doesn't have feature X" | Paywall overpromise OR add feature |
| "Charged twice" | Restore Purchase flow + entitlement bug |
| "Doesn't work" | Bug — investigate logs |
| "Too expensive" | Pricing tier mismatch — offer downgrade path |
| "Not what I expected" | Onboarding-paywall handoff mismatch |

---

## Source Pointers

- Apple App Store refund flow: https://developer.apple.com/documentation/appstoreserverapi/lookup_orderid
- Apple Consumption API: https://developer.apple.com/documentation/storekitexternalpurchase
- Apple Subscription Pause: https://developer.apple.com/documentation/storekit/working_with_pause_periods_for_subscriptions
- Play Refund flow: https://support.google.com/googleplay/android-developer/answer/2741495
- Adapty 2026 refund data: https://adapty.io/state-of-in-app-subscriptions/
- AppsFlyer Protect360: https://www.appsflyer.com/protect360/
