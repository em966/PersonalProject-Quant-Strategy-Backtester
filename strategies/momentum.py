
def momentum_strategy(data, window=10):
    data['Momentum'] = data['Adj Close'] / data['Adj Close'].shift(window)
    data['Position'] = 0
    data.loc[data['Momentum'] > 1.01, 'Position'] = 1
    data['Strategy_Return'] = data['Position'].shift(1) * data['Return']
    return data['Strategy_Return']
