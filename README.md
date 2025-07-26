# PersonalProject-Quant-Strategy-Backtester

This project is a simple but extensible **strategy backtesting framework** built in Python using historical stock data from Yahoo Finance. It’s designed to simulate and evaluate systematic trading strategies using real market data.

---

# What It Does:

- **Downloads Historical Price Data**  
  - Uses `yfinance` to fetch adjusted closing prices (default: `AAPL`) from 2020 to 2024

- **Applies Multiple Trading Strategies:**
  1. **SMA Crossover Strategy**  
     - Buys when a short-term moving average (20-day) crosses above a longer-term moving average (50-day)  
     - Exits (goes flat) when the short-term MA drops below the long-term MA  
     - Classic trend-following logic
  2. **Momentum Strategy**  
     - Buys when the current price is more than 1% higher than the price `n` days ago (default: 10-day lookback)  
     - Exits otherwise  
     - Captures strong upward momentum patterns

- **Simulates Strategy Returns**  
  - Computes daily percentage returns of the asset  
  - Applies signal logic to compute strategy returns  
  - Deducts fixed transaction costs (e.g. 0.1%) to model realistic execution

- **Calculates Key Performance Metrics**  
  For each strategy:
  - **Cumulative Return (%):** Final portfolio value vs starting capital  
  - **Sharpe Ratio:** Risk-adjusted return assuming daily rebalancing  
  - **Max Drawdown:** Worst peak-to-trough drop in equity curve

- **Exports Results to CSV**  
  - Compiles and saves performance metrics to `data/results.csv` for easy review

- **(Optional Next Step)**  
  - Code structure allows for future integration into a Streamlit dashboard or parameter optimization framework

---

# Strategy Logic

The strategy buys the asset if it shows strong recent momentum:
- `Momentum = (Price_t / Price_{t-20}) - 1`
- Enter a position if `Momentum > 5%`
- Exit if no signal the next day

---

# To Run:
```bash
python projectcode1.py

