
def sma_strategy(data, fast=20, slow=50):
    data['SMA_Fast'] = data['Adj Close'].rolling(fast).mean()
    data['SMA_Slow'] = data['Adj Close'].rolling(slow).mean()
    data['Position'] = 0
    data.loc[data['SMA_Fast'] > data['SMA_Slow'], 'Position'] = 1
    data['Strategy_Return'] = data['Position'].shift(1) * data['Return']
    return data['Strategy_Return']
