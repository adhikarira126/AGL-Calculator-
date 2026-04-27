import yfinance as yf
import pandas as pd
from datetime import date, timedelta

def inputdata(company_name, how_long_ago):
    today = date.today()
    start = today - timedelta(days=how_long_ago)
    data = yf.download(company_name, start=start, end=today)
    df = data.reset_index()
    df["ticker"] = company_name
    df = df[["Date", "Open", "High", "Low", "Close", "ticker"]]
    return df