import yfinance as yf
import pandas as pd
import os
from strategies.sma_crossover import sma_strategy
from strategies.momentum import momentum_strategy
from utils.metrics import compute_metrics

TICKER = 'AAPL'
START = '2020-01-01'
END = '2024-12-31'
TRANSACTION_COST = 0.001  # 0.1%

# --- Load Data ---
data = yf.download(TICKER, start=START, end=END)
data['Return'] = data['Adj Close'].pct_change().fillna(0)

# --- Apply Strategies ---
strategies = {
    "SMA Crossover": sma_strategy,
    "Momentum": momentum_strategy,
}

results = []

for name, strategy_fn in strategies.items():
    strat_returns = strategy_fn(data.copy())
    metrics = compute_metrics(strat_returns, data['Return'], name, TRANSACTION_COST)
    results.append(metrics)

# --- Save to CSV ---
result_df = pd.DataFrame(results)
os.makedirs("data", exist_ok=True)
result_df.to_csv("data/results.csv", index=False)
print(result_df)
