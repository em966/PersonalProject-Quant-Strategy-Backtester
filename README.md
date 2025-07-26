# PersonalProject-Quant-Strategy-Backtester

This project is a simple but extensible **strategy backtesting framework** built in Python using historical stock data from Yahoo Finance. It’s designed to simulate and evaluate systematic trading strategies using real market data.

---

# What It Does:

- Downloads price data (e.g. AAPL) using `yfinance`
- Applies a **momentum-based strategy**:
  - Buy if the 20-day return is greater than 5%
- Simulates trade entries and exits
- Calculates Strategy vs Market Cumulative Returns, Max Drawdown and Sharpe Ratio
- Plots results side-by-side for easy comparison

---

# Strategy Logic

The strategy buys the asset if it shows strong recent momentum:
- `Momentum = (Price_t / Price_{t-20}) - 1`
- Enter a position if `Momentum > 5%`
- Exit if no signal the next day

---


