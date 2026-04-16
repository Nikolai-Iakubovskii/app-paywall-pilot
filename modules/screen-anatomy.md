# Screen Anatomy

Visual hierarchy, layout, accessibility for mobile paywalls. SKILL.md covers what blocks to include; this covers how to lay them out.

---

## Visual Hierarchy Principles

### F-pattern vs Z-pattern

Mobile paywalls should follow a **vertical F-pattern**:
1. Eye lands top-left or center-top (hero / headline)
2. Sweeps down to benefits (left-aligned)
3. Lands on plan card / pricing
4. Lands on CTA
5. Falls to trust block

Don't use Z-pattern (designed for landscape web, doesn't apply on portrait mobile).

### The 3-second rule

**Why 3 seconds:** This is the System-1 decision window (Kahneman 2011, *Thinking, Fast and Slow*). System 1 — fast, intuitive, automatic — makes the dismiss/engage call in this window before System 2 (slow, deliberate) engages. If your paywall requires System-2 thinking (math, fine print, choice paralysis) in those 3 seconds, you've already lost most users. See [pricing-psychology.md](pricing-psychology.md) Kahneman concept #3.

User must understand in 3 seconds:
- What you offer (headline)
- That a free trial exists (if applicable)
- That they can dismiss (close X visible)

If any of these takes longer than 3 seconds, the paywall fails before it starts.

---

## Layout: Above vs Below the Fold

### Above the fold (visible without scroll)

**Why above-fold matters scientifically:** Kahneman's **WYSIATI principle** (*Thinking, Fast and Slow* Ch. 7) — System 1 makes confident judgments based **only on visible information**. Unseen ≠ uncertain to the brain; unseen = doesn't exist. The brain doesn't compute "what am I missing?" — it acts on what's in front of it. This is the strongest scientific argument for Apple Rule "billed amount must be most prominent" — what's visible IS the entire decision input. See [pricing-psychology.md](pricing-psychology.md) Kahneman concept #8.

Must include:
1. Close X (top-left or top-right)
2. Hero / headline
3. Plan card with selected default
4. Primary CTA
5. Trust line (trial terms + price)

### Below the fold (requires scroll)

By WYSIATI: anything below the scroll is functionally invisible for the conversion decision. Treat below-fold as "acceptable for users who actively engage" but never as required for the System-1 decision.

Acceptable below-fold:
- Extended benefit list (>5 items)
- Comparison table (Free vs Pro)
- FAQ
- Testimonials
- Long-form social proof
- Restore Purchase / Terms / Privacy

**Apple Rule:** Restore Purchase, Terms, and Privacy must be **accessible**, not necessarily above fold. Below-fold is OK if reachable by scroll.

---

## Spacing Rules

### Vertical rhythm

| Element | Margin from prev |
|---------|------------------|
| Headline | 16pt from top |
| Subheadline | 8pt from headline |
| Benefits block | 24pt from subheadline |
| Each benefit bullet | 12pt apart |
| Plan card | 32pt from benefits |
| CTA | 16pt from plan card |
| Trust line | 12pt from CTA |
| Legal links | 16pt from trust line |

### Whitespace ratio

- Hero / headline area: 30% of viewport height
- Benefits: 25%
- Plan + CTA: 35%
- Trust + legal: 10%

---

## Thumb Zone (Mobile-Specific)

Bottom third of the screen is the **thumb zone** — easiest to tap one-handed.

| Zone | Element |
|------|---------|
| Top (one-handed strain) | Close X, hero image |
| Middle (visible, harder to tap) | Benefits, plan cards |
| Bottom (thumb zone) | Primary CTA |

**Rule:** Primary CTA must be in the thumb zone — never below fold, never at top.

---

## Pricing Block Anatomy

### Plan card layout

```
┌─────────────────────────────────┐
│ [Most Popular]                  │  ← badge top
│                                 │
│ Annual                          │  ← duration
│ $59.99/year                     │  ← billed amount (largest)
│ ~$5/month · 7-day free trial    │  ← per-period + trial (smaller)
│                                 │
│        ✓ Selected               │  ← visual selected state
└─────────────────────────────────┘
```

**Apple Rule (3.1.2(c)):** The billed amount ($59.99/year) must be the most prominent text in the pricing block. Per-month / per-week breakdowns must be subordinate.

### 2-plan layout

Side-by-side cards. Equal width. Selected state (border, background, badge) clearly different.

### 3-plan layout

Stacked vertically. Middle = decoy or "popular." Top = premium. Bottom = entry.

OR side-by-side carousel with default centered.

---

## Color & Contrast

### Selected vs unselected plan

- Selected: brand color border, slightly elevated card, clear badge
- Unselected: neutral border, no badge

### CTA contrast

- WCAG AA minimum: 4.5:1 contrast ratio for text on CTA background
- WCAG AAA preferred: 7:1
- Never use color alone to convey meaning (colorblind users)

### Dark mode

Modern apps support both. Don't ship a paywall that breaks in dark mode.

- Hero image: separate asset for dark mode
- Text: invert backgrounds, not just colors
- Plan cards: adjust border colors

---

## Typography

### Hierarchy

| Element | Size (iOS pt) |
|---------|--------------|
| Headline | 28–34pt |
| Subheadline | 17–20pt |
| Benefit bullet | 15–17pt |
| Pricing (billed amount) | 22–28pt |
| Pricing (per-period subordinate) | 13–15pt |
| CTA | 17pt |
| Trust line | 13pt |
| Legal links | 11–12pt |

### Apple Pricing Font Threshold

**Field Report (RevenueFlo 2026):** ~16pt minimum for pricing text correlates with safer compliance. Below 16pt = higher rejection risk.

### Dynamic Type

iOS users can scale system text size up to 200%+. Test paywall at largest accessibility size — does it still fit?

---

## Accessibility (WCAG + iOS Accessibility)

### Required

- VoiceOver labels on all interactive elements
- 44x44pt minimum tap target (Apple HIG)
- Sufficient color contrast (WCAG AA)
- No information conveyed by color alone
- Plan cards readable when selected via keyboard

### Recommended

- Reduce Motion respected (no required animations)
- Dynamic Type up to AX5
- High Contrast mode tested
- Voice Control compatibility

---

## Safe Areas (iOS)

- Top: respect status bar + dynamic island
- Bottom: respect home indicator (34pt)
- Left/right: respect notch on landscape (rare on paywalls)

If paywall has full-bleed hero image, add gradient overlay behind status bar text.

---

## Loading States

### Initial load

Show skeleton or spinner immediately. Never blank screen >500ms.

### Purchase in flight

CTA shows loading state. Disable other interactions. Don't let user re-tap.

### Error states

Specific copy:
- Network: "Couldn't connect. Try again."
- Already purchased: "You're already subscribed. Tap Restore."
- Card declined: "Payment failed. Try a different card."
- Cancel: silent, return to paywall (don't show "You cancelled" — friction)

---

## Animation Guidelines

### What works

- Subtle hero animation (Lottie loop ≤3s)
- Fade-in benefits sequentially (≤300ms each)
- Plan card selection state (≤200ms)

### What hurts

- Flashy intros (delay value perception)
- Distracting background motion (eye doesn't land on CTA)
- Animations that block interaction
- Animations that don't respect Reduce Motion setting

### Adapty 2.9x animation claim
**Vendor_blog Hypothesis** — claims animated paywalls 2.9x convert vs static. Methodology not open. Test in your own app; don't assume the lift transfers.

---

## Mobile Web Paywall (post Epic v. Apple)

If you ship a US-only web checkout (allowed since May 2025):

- Mobile-web layout, NOT iOS sheet replica
- Apple Pay / Google Pay buttons prominent
- Re-entry to app deeplink after purchase
- Disclosure: "External purchase — handled by [your company], not Apple."

---

## Checklist: Before Shipping

- [ ] Above-fold has: close X, headline, plan card, CTA
- [ ] CTA is in thumb zone (bottom third)
- [ ] Billed amount is the most prominent pricing text (Apple Rule)
- [ ] Per-week / per-day breakdown (if any) is visually subordinate
- [ ] Pricing font ≥16pt
- [ ] Tap targets ≥44pt
- [ ] WCAG AA contrast on CTA
- [ ] Dark mode tested
- [ ] Dynamic Type up to AX5 tested
- [ ] VoiceOver labels on all interactive elements
- [ ] Reduce Motion respected
- [ ] Safe areas respected (status bar, home indicator)
- [ ] Loading + error states defined
- [ ] No animations block interaction
- [ ] No information conveyed by color alone

---

## Source pointers

- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- WCAG 2.2: https://www.w3.org/WAI/WCAG22/quickref/
- iOS Dynamic Type: https://developer.apple.com/design/human-interface-guidelines/typography
- RevenueFlo rejections: https://revenueflo.com/blog/common-ios-paywall-rejections-and-the-fixes-that-work
- Adapty Paywall Library (visual reference): https://adapty.io/paywall-library/
