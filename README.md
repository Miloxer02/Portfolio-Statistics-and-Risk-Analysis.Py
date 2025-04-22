# 🧠 Python-Analysis: Portfolio Risk & Return System

This project is a fully functional portfolio risk analysis tool, built in Python and designed to work with real-time financial data from Yahoo Finance and Stooq.  
It automates data retrieval, portfolio statistics computation, risk measurement, and clean Excel export.

---

## 📊 Features

- **Data Collection**
  - Automated download from Yahoo Finance & Stooq
  - Custom date range and interval
  - Multi-asset support

- **Statistical Analysis**
  - Log return based calculations
  - Mean, Variance, Standard Deviation
  - Skewness, Kurtosis

- **Risk Metrics**
  - Value at Risk (VaR 95% / 99%)
  - Expected Shortfall (ES / CVaR)
  - Max Drawdown, CAGR, Calmar Ratio

- **Excel Integration**
  - Auto-export to Excel with structured tabs
  - Support for intervals: 1D, 3D, 5D, 10D, 1M, Annual
  - Precision formatting & adaptive column widths

---

## ⚠️ VaR Interpretation by Interval

The Value at Risk (VaR) and Expected Shortfall (ES) are calculated differently depending on the time horizon:

| Interval         | Method               | Formula                              | Output Scale |
|------------------|----------------------|--------------------------------------|--------------|
| `1D`, `3D`, `5D` | Scaled log-returns   | `VaR = logVaR_1D * sqrt(n)`          | Log-return   |
| `10D`, `1M`, `Annual` | % loss conversion | `VaR = - (1 - exp(logVaR_nD))`     | Percentage   |

---

## 🧪 Tech Stack

- `pandas`
- `numpy`
- `os`
- `yfinance`
- `xlsxwriter`

---

## 📁 Project Structure

- Models/  
  &nbsp;&nbsp; ├── Main.py – Main pipeline  
  &nbsp;&nbsp; ├── Export_excel.py – Excel export functions  
  &nbsp;&nbsp; ├── Portfolio_analysis.py – Risk & statistics calculation  
  &nbsp;&nbsp; ├── Download_Stooq.py – Fetch data from stooq.pl  
  &nbsp;&nbsp; ├── Download_Yahoo.py – Fetch data from Yahoo Finance  
  &nbsp;&nbsp; └── Config.py – Configuration: tickers, sources, intervals, dates

- Data/ – Raw ticker lists and external datasets  
- Excels/ – Final Excel outputs with full statistics  
- Requirements.txt – List of required Python packages  
- README.md – Project documentation and usage guide

---

✍️ Author

**Miłosz Łebecki** (Miloxer02)  
_Quantitative Asset and Risk Management Student_
