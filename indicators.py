import pandas as pd

def postive_point(df):
    delta = df["Close"].diff()
    df["gains"] = delta.clip(lower=0)
    df["lossess"] = delta.clip(upper=0)
    avg_gain = df["gains"].rolling(5).mean()
    avg_loss = df["lossess"].abs().rolling(5).mean()
    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))
    df["sma"] = df["Close"].rolling(5).mean()
    df["singal"] = "hold"
    df.loc[df["rsi"] < 30, "singal"] = "buy"
    df.loc[df["rsi"] > 70, "singal"] = "sell"

def MACD(df):
    day = df["Close"]
    day_12 = day.rolling(12).mean()
    day_26 = day.rolling(26).mean()
    macd = day_12 - day_26
    day_9 = macd.rolling(9).mean()
    df["macd"] = macd
    df["day_9"] = day_9
    df["singal"] = "hold"
    df.loc[df["macd"] < df["day_9"], "singal"] = "sell"
    df.loc[df["macd"] > df["day_9"], "singal"] = "buy"