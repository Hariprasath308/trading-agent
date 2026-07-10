def moving_average_strategy(df, short_ma, long_ma):
    
    # Calculate Moving Averages
    df["SMA20"] = df["Close"].rolling(window=short_ma).mean()
    df["SMA50"] = df["Close"].rolling(window=long_ma).mean()

    # Not enough data
    if len(df) < long_ma:
        return "HOLD"

    prev = df.iloc[-2]
    curr = df.iloc[-1]

    prev_short = float(prev["SMA20"])
    prev_long = float(prev["SMA50"])
    curr_short = float(curr["SMA20"])
    curr_long = float(curr["SMA50"])

    # BUY Signal
    if prev_short <= prev_long and curr_short > curr_long:
        return "BUY"

    # SELL Signal
    elif prev_short >= prev_long and curr_short < curr_long:
        return "SELL"

    return "HOLD"