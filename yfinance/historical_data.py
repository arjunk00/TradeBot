import yfinance as yf
import pandas

stock = "IDEA.NS"

idea = yf.Ticker(stock)
hist = idea.history(period="1wk", interval="1m")

print(hist["Open"])
print(hist["Close"])
# print(hist)
