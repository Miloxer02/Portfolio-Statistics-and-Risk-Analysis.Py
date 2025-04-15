# 🧠 Python-Analysis: Portfolio Risk & Simulation System

This project is a fully functional portfolio risk analysis and simulation tool, built in Python and designed to work with real-time financial data from Yahoo Finance and Stooq.  
It automates data retrieval, portfolio analysis, risk measurement, simulations, and Excel export.

---

## 📊 Features

- **Data Collection**
  - Automated download from Yahoo Finance & Stooq
  - Custom date range and frequency
  - Multiticker support

- **Empirical Analysis**
  - Mean, Variance, Std Dev
  - Portfolio variance
  - Correlation & Covariance matrices

- **Risk Metrics**
  - Value at Risk (VaR 95% / 99%)
  - Expected Shortfall (CVaR)
  - Stress Testing

- **Portfolio Optimization**
  - Minimum Variance Portfolio
  - Efficient frontier (planned)
  - Weights calculation using `riskfolio-lib`

- **Simulations**
  - Monte Carlo simulation
  - Next-day price predictions

- **Excel Integration**
  - Auto-export to structured Excel files
  - Daily portfolio valuation & indicators

---

## 🧪 Tech Stack

- `pandas`, `numpy`, `matplotlib`
- `yfinance`, `requests`, `openpyxl`
- `riskfolio-lib`
- `datetime`, `json`, `os`, `glob`

---

📦 Python-Analysis
│
├── Models/
│   ├── Main.py                 # Main pipeline
│   ├── Export_excel.py         # Excel export functions
│   ├── Portfolio_analysis.py   # Risk & statistics
│   ├── Simulation.py           # Monte Carlo simulations
│   └── Config.json             # Ticker list & settings
│
├── Data/                       # Raw or cleaned datasets
├── Excels/                     # Final Excel outputs
├── Requirements.txt
└── README.md

---

✍️ Author

Miłosz Łebecki (Miloxer02)
Quantitative Asset and Risk Management Student
