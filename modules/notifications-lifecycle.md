# Notifications & Lifecycle Messaging

Push and email sequences for trial, abandon, renewal-risk, win-back, and billing-issue. Most paywall optimization stops at the screen — half the LTV gains come from these touchpoints **after** the paywall.

For lifecycle stages overview see SKILL.md LIFECYCLE MONETIZATION. For paywall screen patterns see [teardowns.md](teardowns.md).

---

## Why Notifications Matter

Blinkist's Trial Timeline paywall is famous for +23% trial signups, but the **+1,200% notification opt-in lift** (from 6% to 74%) is what compounds. Once users opted in, the Day-5 trial reminder push became their highest-leverage retention lever.

**Source:** Purchasely Blinkist case study + B2B Pricing Insights analysis.

The pattern: paywall transparency earns the opt-in → opt-in enables the reminder → reminder reduces refund + complaint rate.

---

## Notification Permission Strategy

### When to ask for push

| When | Why | Conversion |
|------|-----|-----------|
| ❌ App launch | Cold ask, low intent | 20-30% opt-in |
| ❌ Right after install | Same problem | 25-35% |
| ✅ After first value moment | User just got value, reciprocity activated | 50-65% |
| ✅ During paywall (Blinkist pattern) | Frame as "we'll remind you before charging" | 70-80%+ |
| ✅ After trial start | "Get a reminder before your trial ends" | 75-85% |

### Apple Rule

iOS requires explicit opt-in via `UNUserNotificationCenter.requestAuthorization`. Pre-prompt soft ask ("Allow notifications so we can remind you before billing?") + hard system ask = 2-3x opt-in rate of cold system ask alone.

### Anti-pattern

Don't ask for push permission on the same screen as the paywall purchase. Either request opt-in BEFORE paywall (during onboarding completion) OR AFTER successful purchase (so it doesn't add friction to conversion).

---

## Trial Lifecycle Notifications

### The Blinkist Sequence (proven pattern)

| Day | Channel | Message intent | Effect |
|-----|---------|---------------|--------|
| Day 0 | In-app banner | "Welcome to Premium" + show timeline | Sets expectations |
| Day 1 | Push | "You unlocked X — try Y next" | Drives engagement |
| Day 3 | Push | "You're halfway through your trial" | Mid-trial anchor |
| Day 5 (3 days before charge) | **Push + email** | "Your trial ends in 2 days. Tap to manage." | -55% complaints |
| Day 6 | Push | "1 day left — keep your progress" | Last reminder |
| Day 7 | Push (if cancelled) | "We saved your progress for 7 days" | Win-back hook |

### Copy patterns

**Day 5 reminder (the critical one):**

```
Subject: Your trial ends Friday
Body: You've been using [Feature] for 5 days. Your trial converts to paid on
[date]. Tap to keep going or cancel anytime.

[Manage Subscription]  [Continue Trial]
```

**Tone rules:**
- Transparent about charge date (Apple Rule alignment + builds trust)
- Reminds user of value gained ("You've used [Feature] X times")
- Both options (manage / continue) — never trap

### What NOT to send

- Reminders less than 24h before billing (too late to cancel = anger)
- "Your trial ends soon" without specific date
- Guilt-trip ("Don't lose your gains") — Field Report: high rejection correlation if shown in-app

---

## Transaction Abandon Sequence

User cancelled the payment sheet. Different from "dismissed paywall" — they were committed enough to start checkout.

**Superwall study:** 17% of total revenue comes from abandon paywalls (18 companies, 525K users).

### The Abandon Sequence

| Trigger | Channel | Message |
|---------|---------|---------|
| Immediate | In-app soft prompt | Alternative plan offer (NOT full paywall — Apple Rule risk) |
| +1 hour | Push | "Still interested? Here's a special offer" |
| +24 hours | Email | Detailed offer with 24h expiry |
| +3 days | Push | Last-chance reminder if applicable |

### Copy patterns

**Soft prompt (immediate, in-app):**

```
Headline: "Looking for a different plan?"
Body: "Try our weekly plan instead — same access, less commitment."
[See Weekly Plan]  [No thanks]
```

**Push +1 hour:**

```
"Special offer: 30% off annual plan, today only."
```

### Anti-pattern

**Two full paywalls back-to-back.** Apple has rejected for "aggressive monetization." Use a soft prompt or banner, not a second full screen.

---

## Renewal-Risk Notifications

Triggered by `DID_CHANGE_RENEWAL_STATUS` in App Store Server Notifications V2 (or Play `SUBSCRIPTION_RENEWAL_DISABLED`).

### The Sequence

| Days before renewal | Channel | Message |
|--------------------|---------|---------|
| Renewal turned off → +0 | Push | Acknowledge the choice; don't beg |
| Day -25 | Email | What they'll lose; promotional offer |
| Day -7 | Push | Apple Promotional Offer or Win-Back hook |
| Day -1 | Push | Last reminder |
| Day 0 (expiry) | Push | "Your subscription ended. Here's a one-time offer." |
| Day +14 | Push | Win-Back Offer (iOS 18+) |

### Copy patterns

**Push at -25 days:**

```
"Heads up: your subscription ends [date]. Keep your plan with this offer."
[Get 30% off]
```

**Day 0 expiry:**

```
"Your subscription ended. Welcome back anytime — here's 50% off your first month."
```

### Use Apple's surfaces when possible

Apple's native Win-Back Offers (iOS 18+) appear on the App Store product page automatically. You don't need to push for win-back if the user opens App Store — Apple does the work. Push is for users who don't return organically.

---

## Billing-Issue Notifications

Triggered by `BILLING_RETRY` (App Store) or grace period (Play Billing).

### The Sequence

| Trigger | Channel | Message |
|---------|---------|---------|
| Payment failed → +0 | In-app banner + system sheet | "Update payment to keep access" |
| +24h | Push | Reminder; deeplink to system sheet |
| +3 days (grace ending) | Push | Last reminder before access ends |
| Access ended | Push | "Update payment to restore" |

### Use Apple's system sheet

Apple provides a billing problem sheet — users update payment without leaving your app. Don't reinvent it.

```swift
// SwiftUI
@Environment(\.requestReview) var requestReview
// Use the system billing sheet for retry
```

**Apple Rule:** Don't withhold purchased content during grace period (you've been paid). Only restrict after grace fully expires.

---

## Win-Back Sequence (Lapsed Subscribers)

User's subscription expired and they're not using the app.

### The Sequence

| Trigger | Channel | Message |
|---------|---------|---------|
| Day 7 lapsed | Email | "We miss you" + what's new since they left |
| Day 14 lapsed | Push | Apple Win-Back Offer (iOS 18+) |
| Day 30 lapsed | Email | New features since they left + bigger discount |
| Day 60 | Email (final) | Last attempt; clean list after this |

### Copy patterns

**Day 14 push:**

```
"[Name], we have a special offer for you. 50% off to come back."
```

### Don't over-message

3-4 win-back attempts max. Beyond that, you're spamming and brand will suffer. Clean inactive lists at 90 days.

---

## Engagement Notifications (Pre-Purchase)

For freemium users, push that drives them toward the aha moment.

### What works

- **Streak reminders** ("Don't break your 7-day streak")
- **Personalized insights** ("Your [Insight] just updated")
- **Social proof** ("12 friends have new activity")
- **Time-of-day relevance** ("Time for your evening meditation")

### What hurts

- Generic "Open the app!"
- Pure marketing pushes ("Premium has 50 features")
- More than 1 push per day for non-engaged users

---

## Email vs Push: When to Use Which

| Scenario | Push | Email |
|----------|------|-------|
| Time-sensitive trial reminder | ✅ Primary | ✅ Backup |
| Detailed offer copy | ❌ Too short | ✅ Primary |
| User opted out of push | — | ✅ Primary |
| Win-back after long lapse | ❌ Likely uninstalled | ✅ Primary |
| Engagement nudge | ✅ Primary | — |
| Compliance / legal | ❌ Not appropriate | ✅ Required for some |

---

## Tooling

| Tool | Best for | Note |
|------|---------|------|
| OneSignal | Cross-platform push | Free tier good for indie |
| Firebase Cloud Messaging | Cross-platform push | Most flexible if you have Firebase |
| Customer.io | Email + push lifecycle | Best automation |
| Iterable | Enterprise lifecycle | Overkill for indie |
| Klaviyo | Email-heavy lifecycles | E-commerce roots |
| RevenueCat / Adapty webhooks | Subscription state events | Wire to your messaging tool |

---

## Compliance Notes

- **Push frequency:** Apple may reject apps for excessive push (>5/day, marketing-only push without value)
- **Email opt-out:** GDPR + CAN-SPAM require unsubscribe link
- **Right to be forgotten:** GDPR — delete user data on request, including notification history
- **Push targeting children:** Stricter rules (COPPA / Apple's Kids Category)

---

## Source Pointers

- Blinkist case study (Purchasely): https://www.purchasely.com/blog/blinkist-paywall-transformation-revolutionizes-app-user-engagement
- Blinkist 1,200% opt-in lift: https://b2bpricinginsights.substack.com/p/4-min-read-how-blinkists-new-paywall
- Superwall transaction abandon: https://superwall.com/blog/17-revenue-boost-with-transaction-abandon-paywalls-a-case-study/
- Apple Server Notifications V2: https://developer.apple.com/documentation/appstoreservernotifications
- Play Real-Time Developer Notifications: https://developer.android.com/google/play/billing/rtdn-reference
- Apple Win-Back Offers: https://developer.apple.com/documentation/storekit/promotional_offers
