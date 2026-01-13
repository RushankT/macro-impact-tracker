# Macro Event Impact Tracker

An interactive dashboard that analyzes how macroeconomic events such as
inflation releases (CPI) and policy rate decisions impact equity markets
across India and the United States.

This project focuses on empirical market reactions rather than prediction,
with explicit handling of real-world data limitations.

---

## 🚀 Live Dashboard

https://macro-impact-tracker.streamlit.app

---

## 📊 Features

- Event-day and next-day market reaction analysis
- Comparison of macro event impact across India and the US
- Interactive filtering by country, event type, and asset
- Event-level transparency with auditable outputs
- Robust handling of historical and intraday data constraints

---

## 🧠 Key Insights

- Policy rate announcements tend to show stronger next-day reactions than
  same-day moves.
- CPI releases exhibit higher return dispersion, indicating uncertainty-
  driven volatility.
- US markets generally price macroeconomic information faster than Indian
  markets.
- Macro events primarily act as volatility catalysts rather than reliable
  directional signals.

---

## ⚙️ Methodology

### Data Sources
- US macroeconomic data: FRED (Federal Reserve Economic Data)
- India macroeconomic data: Official Government and RBI releases
- Market price data: Yahoo Finance

### Event Alignment
- Macro events are aligned to their official release timestamps.
- Market reactions are calculated using equity index closing prices.

### Return Definitions
- Event-Day Return:
  Close (event day) vs previous trading day close
- Next-Day Return:
  Close (next trading day) vs event day close

### Intraday Analysis
- Intraday analysis is limited by historical data availability from free
  data providers.
- Where intraday data is unavailable, daily reactions are used for
  consistency and robustness.

### Design Philosophy
- Emphasis on empirical insight over prediction
- Transparent assumptions and reproducible methodology
- Explicit acknowledgment of real-world data constraints

---

## 🛠️ Tech Stack

- Python
- Pandas
- Streamlit
- Plotly
- Yahoo Finance
- FRED API

---

## 📁 Project Structure

macro-impact-tracker/
├── app.py
├── data/
│   ├── daily_reactions.csv
│   └── intraday_reactions.csv
├── requirements.txt
└── README.md

---

## 👤 Author

Rushank Talwar

Macro × Markets × Product
