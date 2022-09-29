import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from trainer import makepickle

df = pd.read_csv("BAJFINANCE__EQ__NSE__NSE__5MINUTE_CONVERGED.csv")
# print(df.isnull().sum())
df = df.drop(columns=['timestamp', 'volume'])
feature = ["open", "high", "low", "close"]
X = df[feature]
output = df.close
output.at[0] = np.nan
output = output.dropna()
print(df.columns)
X = X.drop(len(X)-1)
y = output
print(X)
print(y)
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(y_train.shape)
lr = LinearRegression()
lr.fit(x_train, y_train)
prediction = lr.predict(x_test)
lr.score(x_test,y_test)

makepickle(lr,"linear_regression_new")
#4132.05