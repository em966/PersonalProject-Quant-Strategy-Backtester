
def compute_metrics(strategy_ret, market_ret, name, cost):
    strategy_ret = strategy_ret - cost
    cumulative_strategy = (1 + strategy_ret).cumprod()
    cumulative_market = (1 + market_ret).cumprod()
    
    sharpe = (strategy_ret.mean() / strategy_ret.std()) * (252 ** 0.5)
    max_dd = ((cumulative_strategy / cumulative_strategy.cummax()) - 1).min()

    return {
        "Strategy": name,
        "Total Return (%)": cumulative_strategy.iloc[-1] * 100 - 100,
        "Sharpe Ratio": sharpe,
        "Max Drawdown (%)": max_dd * 100
    }
