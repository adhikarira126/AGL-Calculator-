from Fetcher import inputdata
from indicators import postive_point, MACD
from backtest import buy
import sqlite3

ticker = input("Enter stock name (e.g. AAPL): ")
days = int(input("Enter how many days: "))
cash = int(input("Enter starting cash: "))

df = inputdata(ticker, days)
postive_point(df)
MACD(df)
buy(df, cash)