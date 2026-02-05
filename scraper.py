import yfinance as yf
import json

#Λίστα με τα σύμβολα που θα θέλουμε

tickers=["BTC-USD", "ETH-USD", "AAPL", "TSLA"]

data_to_save={}


for symbol in tickers:
    ticker=yf.Ticker(symbol)
    price = ticker.fast_info['last_price']
    data_to_save[symbol] = round(price,2)


with open('data.json, 'w') as f:
    json.dumo(data_to_save,f)          

print("Data updated successfully")
