---
pubDatetime: 2026-03-15T00:00:00Z
title: "Fertiliser Prices in Europe: 12-Month Price Tracker (March 2025 - March 2026)"
postSlug: "fertiliser-prices-europe-12-month-tracker"
description: "Comprehensive analysis of fertiliser price trends across Europe over the past 12 months, with interactive charts tracking urea, ammonium nitrate, DAP, and potash prices."
tags:
  - fertiliser
  - prices
  - agriculture
  - farming
  - europe
  - commodities
---

## Executive Summary

Fertiliser prices across Europe have experienced significant volatility over the past 12 months, driven by geopolitical tensions, supply chain disruptions, and energy cost fluctuations. This analysis tracks the major fertiliser types used in European agriculture and highlights key market developments.

### Key Findings

- **Urea prices surged 56% year-on-year**, reaching $599.50/tonne in March 2026
- **UK ammonium nitrate** climbed to £406/tonne in December 2025, up from £350/tonne earlier in the year
- **DAP (Diammonium Phosphate)** rose 41% to $554.80/tonne in September 2025
- **Potash prices** increased 23% year-on-year, reaching $286.90/tonne
- **Middle East conflict** in early 2026 caused further supply concerns, with urea jumping 34% in a single month

---

## 12-Month Price Trends

The following charts track fertiliser prices from March 2025 to March 2026, based on data from World Bank Pink Sheet, Trading Economics, AHDB, and industry reports.

### Global Urea Prices (USD/tonne)

{{< chart >}}
{
  type: 'line',
  data: {
    labels: ['Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025', 'Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025', 'Jan 2026', 'Feb 2026', 'Mar 2026'],
    datasets: [{
      label: 'Urea (USD/tonne)',
      data: [385, 360, 342, 337, 340, 343, 461, 445, 430, 420, 424, 445, 599],
      borderColor: 'rgba(59, 130, 246, 1)',
      backgroundColor: 'rgba(59, 130, 246, 0.2)',
      borderWidth: 3,
      fill: true,
      tension: 0.3,
      pointRadius: 4,
      pointHoverRadius: 6
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: { color: '#e5e7eb', font: { size: 14 } }
      },
      tooltip: {
        mode: 'index',
        intersect: false,
        callbacks: {
          label: function(context) {
            return 'Urea: $' + context.parsed.y + '/tonne';
          }
        }
      }
    },
    scales: {
      x: {
        ticks: { color: '#9ca3af' },
        grid: { color: 'rgba(55, 65, 81, 0.5)' }
      },
      y: {
        min: 300,
        max: 650,
        ticks: { 
          color: '#9ca3af',
          callback: function(value) { return '$' + value; }
        },
        grid: { color: 'rgba(55, 65, 81, 0.5)' },
        title: { display: true, text: 'Price (USD/tonne)', color: '#e5e7eb' }
      }
    }
  }
}
{{< /chart >}}

---

### DAP & Phosphate Fertilisers (USD/tonne)

{{< chart >}}
{
  type: 'line',
  data: {
    labels: ['Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025', 'Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025', 'Jan 2026', 'Feb 2026'],
    datasets: [{
      label: 'DAP (USD/tonne)',
      data: [617, 545, 522, 543, 539, 546, 555, 573, 575, 568, 590, 648],
      borderColor: 'rgba(16, 185, 129, 1)',
      backgroundColor: 'rgba(16, 185, 129, 0.2)',
      borderWidth: 3,
      fill: true,
      tension: 0.3
    }, {
      label: 'TSP (USD/tonne)',
      data: [449, 443, 435, 474, 506, 507, 504, 504, 491, 478, 485, 495],
      borderColor: 'rgba(245, 158, 11, 1)',
      backgroundColor: 'rgba(245, 158, 11, 0.2)',
      borderWidth: 3,
      fill: true,
      tension: 0.3
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: { color: '#e5e7eb', font: { size: 14 } }
      },
      tooltip: { mode: 'index', intersect: false }
    },
    scales: {
      x: {
        ticks: { color: '#9ca3af' },
        grid: { color: 'rgba(55, 65, 81, 0.5)' }
      },
      y: {
        min: 400,
        max: 700,
        ticks: { 
          color: '#9ca3af',
          callback: function(value) { return '$' + value; }
        },
        grid: { color: 'rgba(55, 65, 81, 0.5)' },
        title: { display: true, text: 'Price (USD/tonne)', color: '#e5e7eb' }
      }
    }
  }
}
{{< /chart >}}

---

### Potash (MOP) Prices (USD/tonne)

{{< chart >}}
{
  type: 'line',
  data: {
    labels: ['Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025', 'Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025', 'Jan 2026', 'Feb 2026'],
    datasets: [{
      label: 'Potash MOP (USD/tonne)',
      data: [300, 305, 307, 310, 301, 294, 287, 278, 281, 293, 310, 325],
      borderColor: 'rgba(139, 92, 246, 1)',
      backgroundColor: 'rgba(139, 92, 246, 0.2)',
      borderWidth: 3,
      fill: true,
      tension: 0.3,
      pointRadius: 4
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: { color: '#e5e7eb', font: { size: 14 } }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            return 'Potash: $' + context.parsed.y + '/tonne';
          }
        }
      }
    },
    scales: {
      x: {
        ticks: { color: '#9ca3af' },
        grid: { color: 'rgba(55, 65, 81, 0.5)' }
      },
      y: {
        min: 250,
        max: 350,
        ticks: { 
          color: '#9ca3af',
          callback: function(value) { return '$' + value; }
        },
        grid: { color: 'rgba(55, 65, 81, 0.5)' },
        title: { display: true, text: 'Price (USD/tonne)', color: '#e5e7eb' }
      }
    }
  }
}
{{< /chart >}}

---

## UK & European Specific Prices

### UK Fertiliser Prices (GBP/tonne)

The AHDB tracks UK-specific fertiliser prices, which show similar trends but with regional variations:

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['Mar 2025', 'Jun 2025', 'Sep 2025', 'Dec 2025', 'Jan 2026', 'Feb 2026'],
    datasets: [{
      label: 'Granular Urea (£/tonne)',
      data: [380, 350, 365, 424, 410, 445],
      backgroundColor: 'rgba(59, 130, 246, 0.7)',
      borderColor: 'rgba(59, 130, 246, 1)',
      borderWidth: 1
    }, {
      label: 'Ammonium Nitrate (£/tonne)',
      data: [370, 355, 375, 406, 385, 420],
      backgroundColor: 'rgba(239, 68, 68, 0.7)',
      borderColor: 'rgba(239, 68, 68, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: { color: '#e5e7eb', font: { size: 14 } }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            return context.dataset.label + ': £' + context.parsed.y + '/tonne';
          }
        }
      }
    },
    scales: {
      x: {
        ticks: { color: '#9ca3af' },
        grid: { color: 'rgba(55, 65, 81, 0.5)' }
      },
      y: {
        min: 300,
        max: 500,
        ticks: { 
          color: '#9ca3af',
          callback: function(value) { return '£' + value; }
        },
        grid: { color: 'rgba(55, 65, 81, 0.5)' },
        title: { display: true, text: 'Price (£/tonne)', color: '#e5e7eb' }
      }
    }
  }
}
{{< /chart >}}

---

## Year-on-Year Price Comparison

{{< chart >}}
{
  type: 'bar',
  data: {
    labels: ['Urea', 'DAP', 'Potash (MOP)', 'TSP'],
    datasets: [{
      label: 'March 2025',
      data: [385, 617, 300, 449],
      backgroundColor: 'rgba(99, 102, 241, 0.7)',
      borderColor: 'rgba(99, 102, 241, 1)',
      borderWidth: 1
    }, {
      label: 'March 2026',
      data: [599, 648, 325, 495],
      backgroundColor: 'rgba(236, 72, 153, 0.7)',
      borderColor: 'rgba(236, 72, 153, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: { color: '#e5e7eb', font: { size: 14 } }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            return context.dataset.label + ': $' + context.parsed.y + '/tonne';
          }
        }
      }
    },
    scales: {
      x: {
        ticks: { color: '#9ca3af' },
        grid: { color: 'rgba(55, 65, 81, 0.5)' }
      },
      y: {
        min: 0,
        max: 700,
        ticks: { 
          color: '#9ca3af',
          callback: function(value) { return '$' + value; }
        },
        grid: { color: 'rgba(55, 65, 81, 0.5)' },
        title: { display: true, text: 'Price (USD/tonne)', color: '#e5e7eb' }
      }
    }
  }
}
{{< /chart >}}

---

## Key Market Drivers

### 1. Geopolitical Tensions

The **Middle East conflict** that began in early 2026 has severely disrupted fertiliser supply chains:

- **Strait of Hormuz**: Approximately one-third of global fertiliser trade passes through this shipping route
- **Iranian exports**: Account for ~4.5% of global oil supply, affecting nitrogen fertiliser production costs
- **Urea spike**: Prices rose 33.7% in a single month (February-March 2026)
- **Middle East plant closures**: Several fertiliser plants halted production due to feedstock shortages

### 2. Energy Costs

Natural gas accounts for **60-80% of nitrogen fertiliser production costs**:

- European TTF gas prices averaged €11-15/MWh through 2025
- Energy-intensive European producers face competitive pressure from regions with cheaper gas
- Some European plants reduced capacity due to unfavourable economics

### 3. Trade Policy Changes

The **EU proposed tariffs on Russian and Belarusian fertilisers**:

- Starting July 2025, tariffs of €40-45/tonne
- Rising to €315-430/tonne by 2028
- Russia and Belarus supply significant volumes of potash and nitrogen fertilisers to Europe
- **Update March 2026**: EU temporarily suspended some tariffs due to supply concerns

### 4. Chinese Export Restrictions

China maintained **export restrictions on nitrogen fertilisers** throughout 2025:

- Limited phosphate exports to support domestic battery production
- Removed significant supply from global markets
- Contributed to upward price pressure globally

---

## Fertiliser Price Index Trend

The World Bank Fertiliser Price Index (2010=100) shows the overall market movement:

{{< chart >}}
{
  type: 'line',
  data: {
    labels: ['Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025', 'Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025', 'Jan 2026', 'Feb 2026'],
    datasets: [{
      label: 'World Bank Fertiliser Index',
      data: [133, 128, 125, 124, 126, 128, 136, 138, 140, 138, 142, 145],
      borderColor: 'rgba(234, 179, 8, 1)',
      backgroundColor: 'rgba(234, 179, 8, 0.2)',
      borderWidth: 3,
      fill: true,
      tension: 0.3,
      pointRadius: 5,
      pointHoverRadius: 7
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top',
        labels: { color: '#e5e7eb', font: { size: 14 } }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            return 'Index: ' + context.parsed.y + ' (2010=100)';
          }
        }
      }
    },
    scales: {
      x: {
        ticks: { color: '#9ca3af' },
        grid: { color: 'rgba(55, 65, 81, 0.5)' }
      },
      y: {
        min: 115,
        max: 155,
        ticks: { color: '#9ca3af' },
        grid: { color: 'rgba(55, 65, 81, 0.5)' },
        title: { display: true, text: 'Index (2010=100)', color: '#e5e7eb' }
      }
    }
  }
}
{{< /chart >}}

---

## Impact on European Farmers

### Rising Input Costs

According to AHDB's Agricultural Price Index:

- **Overall input costs rose 2.4%** in the 12 months to November 2025
- Fertiliser was the **primary driver** of input cost inflation
- UK farmers face **NPK fertiliser price increases of ~£75/tonne** since early 2026

### Farmer Responses

1. **Early purchasing**: Industry bodies urge farmers to buy early to avoid spring backlogs
2. **Reduced application rates**: Some farmers reduced nitrogen usage by 4kg/ha on average
3. **Alternative products**: Increased interest in organic fertilisers and precision application

### NFU Concerns (March 2026)

The UK National Farmers Union raised concerns with Defra:

- Lack of price transparency in fertiliser markets
- Some farmers not receiving prices until delivery
- Need for confidence in supply continuity
- Access to natural gas for horticultural production

---

## Outlook for 2026

### Price Forecasts

| Fertiliser | Current (Mar 2026) | 12-Month Forecast |
|------------|-------------------|-------------------|
| Urea | $599/tonne | $685/tonne |
| DAP | $648/tonne | $680/tonne |
| Potash | $325/tonne | $360/tonne |

### Key Risk Factors

1. **Middle East conflict duration**: Extended disruptions could push prices higher
2. **EU CBAM implementation**: Carbon border adjustment may increase costs further
3. **Natural gas prices**: Any spike in European gas prices will affect nitrogen fertiliser
4. **Currency movements**: GBP/USD fluctuations affect UK import costs
5. **Chinese export policy**: Any easing of restrictions could ease global supply

---

## Data Sources

- **World Bank Pink Sheet**: Monthly commodity price data
- **Trading Economics**: Real-time fertiliser price tracking
- **AHDB (Agriculture & Horticulture Development Board)**: UK fertiliser prices
- **Yara International**: European market reports and production data
- **USDA Economic Research Service**: Global fertiliser market analysis
- **ICIS (Independent Commodity Intelligence Services)**: Market price assessments
- **DTN/Progressive Farmer**: US retail fertiliser price surveys
- **NFU (National Farmers Union)**: UK farming input cost reports

---

## Conclusion

Fertiliser prices in Europe have risen significantly over the past 12 months, with urea showing the most dramatic increase at over 56% year-on-year. The combination of geopolitical tensions, energy costs, trade policy changes, and supply chain disruptions has created a challenging environment for European farmers.

The outlook suggests continued price pressure through 2026, with farmers advised to plan purchases carefully and consider efficiency measures to manage input costs. Policy decisions around EU tariffs, carbon border adjustments, and energy markets will be key determinants of future price movements.

*Last updated: 15 March 2026*