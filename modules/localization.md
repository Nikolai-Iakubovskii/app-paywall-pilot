# Localization

Localization is the **#1 LTV win-rate test category** in Adapty's 2026 platform data — 62.3% of localization A/Bs win, vs 34.6% for visual/copy. Don't skip this.

---

## Pricing Across Markets

### Adapty 2026 H&F data (large_scale_report)

- **4.4x pricing variance** across markets
- **EU apps charge 29–39% more than NA**
- **IN/SEA RLTV is ~46% of NA** on annual

### Recommended pricing tiers (annual, USD-equivalent)

| Tier | Markets | Multiplier vs US |
|------|---------|------------------|
| Premium | DE, JP, CH, SE, NO | 1.3x |
| Standard | US, UK, FR, AU, CA, NL | 1.0x |
| Mid | BR, MX, PL, ZA | 0.6x |
| Low | IN, ID, TR, EG, PH | 0.3x |

**Source:** Adapty 2026 H&F regional pricing index. Real numbers will vary per category — H&F has highest willingness-to-pay; gaming/AI lower variance.

---

## App Store Pricing Strategy

### Option 1: Auto-tier ("Store rules")

Apple auto-converts your USD price to local-currency-rounded charm prices. Easy, low-maintenance.

**Pros:**
- Zero setup
- Charm prices automatic ($9.99 → €9.99 → ¥1500 etc.)
- App Store handles FX shifts

**Cons:**
- Same price across all of EU = leaving money on table in DE/CH
- Same price across all of LatAm = pricing too high in BR vs CL
- No geo-tier differentiation possible

### Option 2: Manual per-territory

Set each territory's price individually in App Store Connect.

**Pros:**
- Capture EU surplus (29–39% premium opportunity)
- Right-size emerging markets (don't price out of reach)
- Match category benchmarks per region

**Cons:**
- Setup time per territory (180+ App Store territories)
- Must update with major FX shifts
- Reporting complexity

### Option 3: Geo-tier (separate SKU per region)

Like ChatGPT Go @ $8 for India. You create a separate App Store product for the region.

**Pros:**
- Massive emerging-market unlock
- Can have different feature sets per tier

**Cons:**
- Engineering complexity (which SKU to show, by user IP/locale)
- App Store SKU management
- Restore Purchase logic across SKUs

### Recommendation

**Top 5 revenue markets: manual per-territory**
**Other markets: auto-tier**
**Emerging markets >5% of installs: geo-tier**

Re-review pricing annually.

---

## Copy Localization

### Length expansion factors (vs English)

| Locale | Expansion | Implication |
|--------|-----------|-------------|
| German | +30–40% | Headlines need short EN source |
| French | +20–30% | CTA buttons may wrap |
| Spanish | +15–25% | Manageable |
| Italian | +20–30% | Similar to French |
| Portuguese (BR) | +20–30% | Similar to Spanish |
| Russian | +10–20% chars; visually denser | Test on real device |
| Japanese | -20–30% | Often shorter |
| Korean | -10–20% | Compact |
| Chinese (Simplified) | -30–50% | Plenty of room |
| Arabic | +5–15% + RTL flip | Mirror entire layout |
| Turkish | +20–30% | Long compound words |
| Polish | +10–25% | Similar to RU |

### CTA length budgets

| Locale | Max characters |
|--------|---------------|
| EN | 25 |
| DE | 35 |
| FR | 30 |
| ES | 28 |
| RU | 22 |
| JA | 18 |
| ZH | 12 |

If your EN CTA is 25 chars, German translation may not fit a button. Either shorten EN OR make button width flexible.

### Tone & formality

| Locale | Default formality |
|--------|------------------|
| EN-US | Casual (you) |
| EN-UK | Slightly formal |
| DE | Formal "Sie" by default; casual "du" for younger audiences |
| FR | Formal "vous" almost always |
| ES (Spain) | "tú" for consumer apps |
| ES (LatAm) | "tú" except Argentina ("vos") |
| JA | Polite form (です/ます) baseline |
| KO | Polite form baseline |
| RU | "ты" for consumer apps; "вы" for B2B/finance |
| AR | Formal in business; informal among peers |

**Test both Sie/du for German.** Headspace and Duolingo use "du" successfully.

---

## Number Formatting

| Locale | Format example |
|--------|---------------|
| EN-US | $9.99 |
| EN-UK | £9.99 |
| DE/FR/ES (EU) | 9,99 € (comma decimal, space, suffix) |
| RU | 9,99 ₽ |
| JA | ¥1,000 (no decimals) |
| ZH | ¥99 (no decimals) |
| AR | ٩٫٩٩ ر.س. (Arabic numerals + RTL) |
| BR | R$ 9,99 |
| IN | ₹ 99 (no decimals on most app prices) |

### Per-period framing in non-EN

- **EN:** "$0.16/day"
- **DE:** "0,16 €/Tag" (NOT "/Day")
- **JA:** "¥20/日"
- **AR:** "ر.س. 0٫16 يوميًا" (RTL flip)

---

## RTL (Arabic, Hebrew)

**Required when shipping AR/HE:**
- Mirror entire layout horizontally
- Number stays LTR (Arabic numerals are visually mirrored but represent same digit)
- Currency symbol position flips
- Icons that imply direction (arrows, progress bars) flip
- Plan cards: read right-to-left

iOS handles much of this via UIKit/SwiftUI semanticContentAttribute, but custom layouts need manual handling.

---

## Cultural Considerations

### Trust signals vary by market

| Market | Trust lever |
|--------|-------------|
| US | "Cancel anytime" + clear pricing |
| DE | GDPR compliance, formal tone, "Datenschutz" front and center |
| JP | Brand authority, third-party endorsements |
| KR | Social proof (KakaoTalk integration, peer recommendations) |
| CN | Local platform integration (WeChat Pay) — but App Store China is different ecosystem |
| FR | Government / academic endorsements |
| BR | Local payment methods (PIX, Boleto) — limited on iOS |

### Imagery

- Avoid US-centric stock photos
- Use locally-relevant scenarios (weather, food, fashion)
- Skin tone diversity in international markets
- Cultural sensitivity: Halal/Kosher mentions for relevant markets, gender norms

---

## Testing Localization

### Process

1. **Translate** professionally (not Google Translate). Native speakers, ideally with marketing copy experience.
2. **Review by native speaker** — translation accuracy ≠ marketing voice.
3. **A/B test** — 62.3% LTV win rate per Adapty justifies the effort.
4. **Monitor refund rate by region** — high refunds may indicate copy mismatch (overpromise translated literally creates issues).

### Automation tools

- Adapty / RevenueCat / Apphud paywall builders: localization built-in
- Weblate / Lokalise / Phrase: industry-standard l10n platforms
- App Store Connect: localized metadata for each territory

### Common mistakes

- Translating CTA button without checking width
- Forgetting to localize price formats (still showing "$" in EU)
- Not localizing trust line ("Cancel anytime" reads weird in some cultures)
- Hardcoded English in error states
- Not testing RTL — even one un-flipped element looks broken

---

## Source pointers

- Adapty 2026 paywall experiments win rates: https://adapty.io/blog/paywall-experiments-playbook/
- Adapty H&F regional pricing: https://adapty.io/blog/health-fitness-app-subscription-benchmarks/
- AppsFlyer 2026 (geo growth): https://www.appsflyer.com/resources/reports/subscription-marketing/
- Apple App Store Connect pricing: https://developer.apple.com/help/app-store-connect/manage-subscriptions/
- iOS internationalization: https://developer.apple.com/design/human-interface-guidelines/inclusion
