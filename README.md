# Portfolio Risk & Return Analyzer

A Python-based system for analyzing financial assets through empirical return statistics and risk measures.  
The project supports real-time data from Yahoo Finance and Stooq, and produces clear, Excel-exportable outputs.

---

## Features

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

## VaR Interpretation by Interval

The Value at Risk (VaR) and Expected Shortfall (ES) are calculated differently depending on the time horizon:

| Interval         | Method               | Formula                              | Output Scale |
|------------------|----------------------|--------------------------------------|--------------|
| `1D`, `3D`, `5D` | Scaled log-returns   | `VaR = logVaR_1D * sqrt(n)`          | Log-return   |
| `10D`, `1M`, `Annual` | % loss conversion | `VaR = - (1 - exp(logVaR_nD))`     | Percentage   |

---

## Python Packages

- `pandas`
- `numpy`
- `os`
- `yfinance`
- `xlsxwriter`

---

## Project Structure

- Models/  
  &nbsp;&nbsp; ├── Main.py – Main function
  &nbsp;&nbsp; ├── Export_excel.py – Excel export functions  
  &nbsp;&nbsp; ├── Portfolio_analysis.py – Risk & statistics calculations
  &nbsp;&nbsp; ├── Download_Stooq.py – Data from stooq
  &nbsp;&nbsp; ├── Download_Yahoo.py – Data from Yahoo Finance  
  &nbsp;&nbsp; └── Config.py – Configuration: tickers, sources, intervals, dates

- Data/ – ticker list  
- Excels/ – Final Excel outputs with full statistics  
- Requirements.txt – List of required Python packages  
- README.md – Project documentation and usage guide

---

## How To Use

1. Clone or download
2. Open `Config.py` and add your tickers (stooq or yfinance)
3. Set your preferred time frame for the data 
4. Run Main.py

---

Author

**Miłosz Łebecki** (Miloxer02)  
_Quantitative Asset and Risk Management Student_
