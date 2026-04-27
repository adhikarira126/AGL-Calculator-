def buy(df, cash):
    share = 0
    starting_cash = cash
    close = df["Close"]
    singal = df["singal"]

    for i in range(len(df)):
        if singal.iloc[i] == "buy":
            price = close.iloc[i].item()
            if price > 0 and cash > 0:
                share = cash / price
                cash = 0
        elif singal.iloc[i] == "sell":
            price = close.iloc[i].item()
            if share > 0:
                cash = share * price
                share = 0

    if share > 0:
        last_price = close.iloc[-1].item()
        cash = share * last_price
        share = 0

    print("Final cash:", cash)
    print("Profit:", cash - starting_cash)
    return cash