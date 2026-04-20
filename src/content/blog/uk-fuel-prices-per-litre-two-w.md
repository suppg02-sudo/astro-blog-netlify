---
pubDatetime: 2026-04-11T12:00:00Z
title: "UK Fuel Prices Per Litre — Two-Week Tracker (April 2026)"
postSlug: "uk-fuel-prices-per-litre-two-w"
description: "UK Fuel Prices Per Litre — Two-Week Tracker (April 2026)"
tags:
  - others
---

A quick-reference guide to UK petrol and diesel pump prices over the last two weeks. Prices in pence per litre (ppl), sourced from PetrolPrices and government data.

> **TL;DR**: Diesel has surged ~16ppl to ~181ppl, unleaded up ~10ppl to ~152ppl in two weeks. A 55L diesel fill-up now costs nearly £100.

## Quick-Reference: Current Prices

| Fuel | Now (ppl) | 2 Weeks Ago (ppl) | Change | Annual High |
|------|-----------|-------------------|--------|-------------|
| Unleaded (E10) | 152 | 142 | +10 | 152 |
| Super Unleaded | 163 | 153 | +10 | 163 |
| Diesel (B7) | 181 | 165 | +16 | 181 |
| Premium Diesel | 192 | 176 | +16 | 192 |

## Two-Week Price Trend

```chart
{
  "type": "line",
  "data": {
    "labels": ["29 Mar", "31 Mar", "2 Apr", "4 Apr", "6 Apr", "8 Apr", "10 Apr", "11 Apr"],
    "datasets": [
      {
        "label": "Unleaded (ppl)",
        "data": [142, 143, 145, 147, 149, 150, 151, 152],
        "borderColor": "#00ff41",
        "backgroundColor": "rgba(0,255,65,0.1)",
        "tension": 0.3,
        "pointRadius": 4,
        "pointBackgroundColor": "#00ff41",
        "borderWidth": 3,
        "fill": true
      },
      {
        "label": "Diesel (ppl)",
        "data": [165, 167, 170, 173, 176, 178, 180, 181],
        "borderColor": "#ff4081",
        "backgroundColor": "rgba(255,64,129,0.1)",
        "tension": 0.3,
        "pointRadius": 4,
        "pointBackgroundColor": "#ff4081",
        "borderWidth": 3,
        "fill": true
      }
    ]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "title": {
        "display": true,
        "text": "UK Average Pump Prices — Last 2 Weeks (Pence Per Litre)",
        "color": "#ffffff",
        "font": {"size": 16, "weight": "bold"}
      },
      "legend": {
        "labels": {"color": "#ffffff", "font": {"size": 13}}
      }
    },
    "scales": {
      "y": {
        "title": {"display": true, "text": "Pence Per Litre", "color": "#cccccc"},
        "min": 130,
        "max": 190,
        "ticks": {"color": "#cccccc"},
        "grid": {"color": "rgba(255,255,255,0.08)"}
      },
      "x": {
        "ticks": {"color": "#cccccc"},
        "grid": {"color": "rgba(255,255,255,0.08)"}
      }
    }
  }
}
```

## Daily Price Table (Pence Per Litre)

| Date | Unleaded | Diesel | Unleaded Change | Diesel Change |
|------|----------|--------|-----------------|---------------|
| 29 Mar (Sat) | 142.0 | 165.0 | — | — |
| 30 Mar (Sun) | 142.1 | 165.4 | +0.1 | +0.4 |
| 31 Mar (Mon) | 143.0 | 167.0 | +0.9 | +1.6 |
| 1 Apr (Tue) | 144.0 | 168.5 | +1.0 | +1.5 |
| 2 Apr (Wed) | 145.0 | 170.0 | +1.0 | +1.5 |
| 3 Apr (Thu) | 146.2 | 171.8 | +1.2 | +1.8 |
| 4 Apr (Fri) | 147.0 | 173.0 | +0.8 | +1.2 |
| 5 Apr (Sat) | 148.0 | 174.5 | +1.0 | +1.5 |
| 6 Apr (Sun) | 149.0 | 176.0 | +1.0 | +1.5 |
| 7 Apr (Mon) | 149.5 | 177.0 | +0.5 | +1.0 |
| 8 Apr (Tue) | 150.0 | 178.0 | +0.5 | +1.0 |
| 9 Apr (Wed) | 150.8 | 179.2 | +0.8 | +1.2 |
| 10 Apr (Thu) | 151.5 | 180.5 | +0.7 | +1.3 |
| 11 Apr (Fri) | 152.0 | 181.0 | +0.5 | +0.5 |

## Cost Per Fill-Up Reference

Based on a standard 55-litre tank:

| Fuel | Fill-Up Cost Now | Fill-Up 2 Weeks Ago | Extra Per Tank |
|------|-----------------|---------------------|----------------|
| Unleaded | £83.60 | £78.10 | +£5.50 |
| Diesel | £99.55 | £90.75 | +£8.80 |

### Monthly Impact (4 fill-ups)

| Fuel | Extra Per Month | Extra Per Year (projected) |
|------|----------------|---------------------------|
| Unleaded | +£22.00 | +£286 |
| Diesel | +£35.20 | +£458 |

## Supermarket vs Brand Pricing

| Retailer Type | Unleaded (ppl) | Diesel (ppl) | Savings vs Average |
|---------------|---------------|-------------|-------------------|
| Supermarket Avg | 148–150 | 177–179 | 2–4ppl |
| Major Brands (Shell, BP, Esso) | 154–158 | 184–188 | -2 to -6ppl |
| Motorway Services | 165–175 | 195–205 | -13 to -23ppl |
| Independent | 149–155 | 179–185 | -3 to +3ppl |

## Regional Breakdown

| Region | Unleaded (ppl) | Diesel (ppl) |
|--------|---------------|-------------|
| London | 154–158 | 184–188 |
| South East | 153–156 | 183–186 |
| South West | 151–154 | 181–184 |
| Midlands | 150–153 | 180–183 |
| North West | 149–152 | 179–182 |
| North East | 149–151 | 179–181 |
| Yorkshire | 149–152 | 179–182 |
| Scotland | 151–155 | 181–185 |
| Wales | 150–153 | 180–183 |
| Northern Ireland | 148–151 | 178–181 |

> [!TIP] Save Money
> Supermarkets consistently offer the lowest prices — typically 2–4ppl below the national average. Use apps like PetrolPrices to compare local stations before filling up.

## Tax Breakdown Per Litre

For unleaded at 152ppl:

| Component | Pence | Percentage |
|-----------|-------|-----------|
| Fuel Duty | 52.95 | 34.8% |
| VAT (20%) | 25.33 | 16.7% |
| Product + Delivery | 73.72 | 48.5% |
| **Total Tax** | **78.28** | **51.5%** |

For diesel at 181ppl:

| Component | Pence | Percentage |
|-----------|-------|-----------|
| Fuel Duty | 52.95 | 29.3% |
| VAT (20%) | 30.17 | 16.7% |
| Product + Delivery | 97.88 | 54.1% |
| **Total Tax** | **83.12** | **45.9%** |

## Why Prices Are Rising

The primary driver is the US–Israeli strikes on Iran (28 February 2026), which triggered:

- **Wholesale diesel up 41.3ppl** (74% rise) — far exceeding the 16ppl retail increase
- **Wholesale unleaded up 20ppl** — compared to 10ppl at the pump
- Retailers absorbing some costs through existing stock, but margins are unsustainable
- Biodiesel blending benefit collapsed from ~8ppl to under 1ppl
- Strait of Hormuz disruption fears tightening global supply

## Price Forecast

| Fuel | Current | Short-Term (2-4 weeks) | Medium-Term (3-6 months) |
|------|---------|----------------------|------------------------|
| Unleaded | 152ppl | 155–160ppl | 145–165ppl (volatile) |
| Diesel | 181ppl | 185–190ppl | 170–195ppl (volatile) |

Analysts warn diesel needs to rise another 10–15ppl for retailer margins to return to historic norms. The September expiry of the 5ppl duty cut would add a further 6ppl (with VAT) to both fuels.

## Government Action Tracker

| Country | Action | Status |
|---------|--------|--------|
| UK | 5ppl duty cut (6ppl with VAT) | Active, expires September 2026 |
| Ireland | Fuel duty cut | Implemented |
| Norway | Fuel tax reduction | Implemented |
| Australia | Fuel excise cut | Implemented |
| France | Financial support for farmers | Announced |
| Poland | Price ceilings | Implemented |
| UK | Additional measures | None announced |

The UK Treasury is collecting an estimated **£6.4 million per day** in additional VAT revenue from the price surge. Industry bodies continue to lobby for duty cuts or temporary VAT relief.

> [!WARNING] Prices Rising
> These are UK national averages. Individual forecourt prices vary significantly. Motorway service stations charge 15–25ppl above average. Always check local prices before filling up.

**Tags**: uk-fuel-prices, petrol, diesel, cost-of-living, fuel-duty, energy-prices
**Categories**: Analysis, UK Economy, Reference