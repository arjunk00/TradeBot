import yfinance as yf
import pandas as pd
import datetime

ns = ".NS"
tickers1 = []
df = pd.read_csv('../csv-files/ind_nifty500list.csv', usecols = ['Symbol'], low_memory = False)
for ind in df.index:
     tickers1.append(df['Symbol'][ind])
tickers = [s + ns for s in tickers1]
print(tickers)
# tickers = ["RELIANCE.NS", "TATAMOTORS.NS", "IDEA.NS", "IRCTC.NS", "CANBK.NS", "ITC.NS", "PNB.NS"]
# tickers = ["RELIANCE.NS"]
# df_list = list()
# for ticker in tickers:
#     startdate = datetime.datetime(2022, 2, 20, 9, 15, 00)
#     enddate = datetime.datetime(2022, 2, 21, 15, 30, 00)
#     for i in range(3):
#         data = yf.download(tickers=ticker, interval="5m", start=startdate, end=enddate, group_by='ticker',
#                            auto_adjust=True)
#         startdate += datetime.timedelta(days=60)
#         enddate += datetime.timedelta(days=60)
#         print(startdate)
#         print(enddate)
#
#         df_list.append(data)
#     df = pd.concat(df_list)
#     df.to_csv(ticker + '.csv')
# data.to_csv(ticker+".csv")
path = "../yfinance/csvs/"
for ticker in tickers:
    startdate = datetime.datetime(2022, 2, 20, 9, 15, 00)
    enddate = datetime.datetime(2022, 4, 10, 15, 30, 00)
    data = yf.download(tickers=ticker, interval="5m", start=startdate, end=enddate, group_by='ticker', auto_adjust=True)
    data.to_csv(path + ticker + ".csv")
