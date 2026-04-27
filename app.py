from flask import Flask, request, jsonify, send_file
from Fetcher import inputdata
from indicators import postive_point, MACD
from backtest import buy

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello World</p>"

@app.route("/ui")
def ui():
    return send_file("index.html")

@app.route("/backtest", methods=["POST"])
def backtest():
    data = request.json
    ticker = data["ticker"]
    days = int(data["days"])
    cash = float(data["cash"])
    
    df = inputdata(ticker, days)
    postive_point(df)
    MACD(df)
    result = buy(df, cash)
    
    return jsonify({"result": result})

app.run(debug=True, host='0.0.0.0', port=5001)