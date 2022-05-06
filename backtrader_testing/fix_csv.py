import csv
import pandas as pd
import datetime
data=pd.read_csv("AARTIIND__EQ__NSE__NSE__MINUTE.csv", usecols=["timestamp"])
# dates = data.tolist()

# data['timestamp'] = data['timestamp'].str.replace('+09:30','')
for date in dates:
    date=date.removesuffix('+09:30')
print(data)
