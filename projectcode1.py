# Quant Strategy Backtesting Notebook

# --- Step 1: Import Libraries ---
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Step 2: Download Data ---
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2024-12-31')
data = data[['Close']]
data['Returns'] = data['Close'].pct_change()
data.dropna(inplace=True)

# --- Step 3: Define Strategy Logic ---
# Example: Simple momentum strategy
lookback = 20
data['Momentum'] = data['Close'].pct_change(lookback)
data['Signal'] = 0
data.loc[data['Momentum'] > 0.05, 'Signal'] = 1  # Buy signal if 20-day return > 5%
data['Position'] = data['Signal'].shift(1)

# --- Step 4: Simulate PnL ---
data['Strategy_Returns'] = data['Position'] * data['Returns']
data.dropna(inplace=True)

# --- Step 5: Evaluate Performance ---
cumulative_strategy = (1 + data['Strategy_Returns']).cumprod()
cumulative_market = (1 + data['Returns']).cumprod()

# --- Step 6: Plot Results ---
plt.figure(figsize=(12, 6))
plt.plot(cumulative_strategy, label='Strategy')
plt.plot(cumulative_market, label='Market')
plt.title(f"{ticker} Strategy vs Market")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.grid()
plt.show()

# --- Step 7: Print Metrics ---
def sharpe(returns, risk_free=0.00):
    return np.sqrt(252) * (returns.mean() - risk_free) / returns.std()

def max_drawdown(series):
    peak = series.cummax()
    drawdown = (series - peak) / peak
    return drawdown.min()

print("--- Performance Metrics ---")
print(f"Total Return (Strategy): {cumulative_strategy.iloc[-1] - 1:.2%}")
print(f"Total Return (Market): {cumulative_market.iloc[-1] - 1:.2%}")
print(f"Sharpe Ratio (Strategy): {sharpe(data['Strategy_Returns']):.2f}")
print(f"Sharpe Ratio (Market): {sharpe(data['Returns']):.2f}")
print(f"Max Drawdown (Strategy): {max_drawdown(cumulative_strategy):.2%}")
print(f"Max Drawdown (Market): {max_drawdown(cumulative_market):.2%}")
