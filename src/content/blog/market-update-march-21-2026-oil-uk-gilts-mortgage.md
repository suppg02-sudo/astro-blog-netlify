---
pubDatetime: 2026-03-21T19:25:00Z
title: "Market Update March 21, 2026: Oil, UK Gilts & Mortgage Rates"
postSlug: "market-update-march-21-2026-oil-uk-gilts-mortgage"
description: "Latest market analysis with 24h/48h/52w data for oil, UK gilts, natural gas, and agricultural commodities"
tags:
  - mortgages
  - uk-gilts
  - oil
  - economics
  - natural-gas
  - commodities
---

# Market Update: March 21, 2026

*Last Updated: 2026-03-21T19:25Z | Data Sources: Investing.com, Bank of England, money.co.uk*

---

## Executive Summary

| Indicator | Current | 24h Change | 48h Change | 52w Change |
|-----------|---------|------------|------------|------------|
| **Brent Crude** | $105.67/bbl | -1.97% | -2.74% | **+50.1%** |
| **WTI Crude** | $92.99/bbl | -2.68% | -1.03% | **+38.0%** |
| **UK 2Y Gilt** | 4.41% | +29.8 bps | - | - |
| **UK 5Y Gilt** | 4.46% | +17.8 bps | - | - |
| **UK 10Y Gilt** | 4.85% | +10.3 bps | - | - |
| **UK 30Y Gilt** | 5.12% | - | - | - |
| **US Nat Gas** | $3.13/MMBtu | +0.16% | +0.61% | -22.3% |
| **EU TTF Gas** | €48.50/MWh | **+35.0%** | - | - |

---

## 1. Oil Prices: Brent & WTI

Oil prices remain elevated with Brent above $100/bbl, though pulling back slightly in the last 24-48 hours. Year-over-year gains remain substantial at +50% for Brent and +38% for WTI.

| Metric | Brent | WTI |
|--------|-------|-----|
| **Current** | $105.67/bbl | $92.99/bbl |
| **24h Change** | -1.97% | -2.68% |
| **48h Change** | -2.74% | -1.03% |
| **52w Change** | +50.08% | +38.00% |

### Key Drivers:
- **Geopolitical tensions** in Middle East affecting supply routes
- **OPEC+ production decisions** maintaining price support
- **Global demand concerns** as economic growth slows

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['24h Change', '48h Change', '52w Change'],
    datasets: [{
      label: 'Brent Crude (%)',
      data: [-1.97, -2.74, 50.08],
      backgroundColor: 'rgba(255, 107, 53, 0.7)',
      borderColor: 'rgba(255, 107, 53, 1)',
      borderWidth: 1
    }, {
      label: 'WTI Crude (%)',
      data: [-2.68, -1.03, 38.00],
      backgroundColor: 'rgba(78, 205, 196, 0.7)',
      borderColor: 'rgba(78, 205, 196, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: true, position: 'top' },
      title: { display: true, text: 'Oil Price Changes (%)' }
    },
    scales: {
      y: { beginAtZero: false }
    }
  }
}
{{< /chart >}}

---

## 2. UK Bond Market: Gilt Yields

UK gilt yields surged across the curve, with the 2-year seeing the largest move (+29.8 bps). The yield curve remains upward sloping, indicating normal market conditions.

| Gilt | Current | 24h Change (bps) | Interpretation |
|------|---------|------------------|----------------|
| **2-Year** | 4.41% | +29.8 | Short-term rates rising |
| **5-Year** | 4.46% | +17.8 | Medium-term following |
| **10-Year** | 4.85% | +10.3 | Long-term more stable |
| **30-Year** | 5.12% | - | Long end anchored |

### Yield Curve Analysis

| Metric | Value | Signal |
|--------|-------|--------|
| **2Y-10Y Spread** | +44 bps | Normal (expansionary) |
| **5Y-30Y Spread** | +66 bps | Normal |

**Interpretation**: The positive 2Y-10Y spread of +44 bps indicates a normal upward-sloping yield curve, suggesting markets expect economic expansion rather than recession.

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['2-Year', '5-Year', '10-Year', '30-Year'],
    datasets: [{
      label: 'Yield (%)',
      data: [4.41, 4.46, 4.85, 5.12],
      backgroundColor: 'rgba(54, 162, 235, 0.7)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1
    }, {
      label: '24h Change (bps)',
      data: [29.8, 17.8, 10.3, 0],
      backgroundColor: 'rgba(255, 99, 132, 0.7)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1,
      yAxisID: 'y1'
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: true, position: 'top' },
      title: { display: true, text: 'UK Gilt Yields & 24h Changes' }
    },
    scales: {
      y: { beginAtZero: false, title: { display: true, text: 'Yield (%)' } },
      y1: { position: 'right', beginAtZero: true, title: { display: true, text: 'Change (bps)' }, grid: { drawOnChartArea: false } }
    }
  }
}
{{< /chart >}}

---

## 3. Natural Gas: US vs Europe

European natural gas prices spiked dramatically (+35% 24h) at the TTF hub, while US Henry Hub remained relatively stable. This divergence highlights ongoing energy security concerns in Europe.

| Market | Current | 24h Change | 48h Change | 52w Change |
|--------|---------|------------|------------|------------|
| **US Henry Hub** | $3.13/MMBtu | +0.16% | +0.61% | -22.3% |
| **EU TTF** | €48.50/MWh | **+35.0%** | - | - |

### Alert Status

- **EU TTF**: Above €50/MWh threshold - supply concerns
- **US Henry Hub**: Below historical averages - ample supply

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['US Henry Hub', 'EU TTF'],
    datasets: [{
      label: '24h Change (%)',
      data: [0.16, 35.0],
      backgroundColor: ['rgba(75, 192, 192, 0.7)', 'rgba(255, 159, 64, 0.7)'],
      borderColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 159, 64, 1)'],
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: true, position: 'top' },
      title: { display: true, text: 'Natural Gas 24h Price Changes' }
    },
    scales: {
      y: { beginAtZero: true, title: { display: true, text: 'Change (%)' } }
    }
  }
}
{{< /chart >}}

---

## 4. Agricultural Commodities

| Commodity | Current | YoY Change |
|-----------|---------|------------|
| **Wheat** | $607.90/bu | +9% |
| **Soybeans** | $1,171.00/bu | +16% |
| **Corn** | $485.00/bu | +3% |

Agricultural prices remain elevated year-over-year, driven by weather disruptions and strong demand.

---

## 5. Fertilisers

| Fertiliser | Current | 3m Change |
|------------|---------|-----------|
| **Urea** | $420.50/t | -3.67% |
| **DAP** | $580.00/t | +8.2% |
| **Potash** | $285.00/t | +5.4% |

---

## 6. Industrial Metals

| Metal | Current | 24h Change | 48h Change |
|-------|---------|------------|------------|
| **Copper** | $5.52/lb | +0.02% | -1.36% |
| **Aluminium** | $2,644/t | -0.50% | -0.14% |

---

## Key Takeaways

1. **Oil remains elevated** - Brent at $105.67/bbl with +50% YoY gain despite short-term pullback
2. **UK gilt yields surging** - 2Y yield up 29.8 bps in 24h, indicating rate expectations rising
3. **EU gas crisis alert** - TTF spiked +35% in 24h, signaling supply concerns
4. **Yield curve normal** - 2Y-10Y spread at +44 bps, no recession signal yet
5. **Agricultural strength** - Wheat +9%, Soybeans +16% YoY

---

## Alert Status Summary

| Indicator | Status | Threshold |
|-----------|--------|-----------|
| Brent Oil | **HIGH** | >$100/bbl |
| EU Natural Gas | **CRITICAL** | >€50/MWh |
| UK 2Y Gilt | **WATCH** | >5% yield |
| Yield Curve | **NORMAL** | 2Y-10Y > 0 bps |

---

## Data Sources

- **Investing.com** - Real-time commodity prices
- **Bank of England** - Base rate, monetary policy
- **money.co.uk** - UK mortgage rates
- **OilPrice.com** - Energy market analysis
- **Trading Economics** - Economic indicators

---

*Analysis compiled: 2026-03-21T19:25Z*