import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
lr = LinearRegression()

df = pd.read_csv("ADANIPORTS__EQ__NSE__NSE__5MINUTE_CONVERGED.csv")

X = np.array(df["close"])
X = np.delete(X, -1)
X = X.reshape(-1, 1)

y = np.array(df["close"])
y = np.delete(y, 0)
y = y.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.33, random_state=42)

lr.fit(x_train, y_train)
print(lr.score)
prediction = lr.predict(x_test)
print(lr.score(x_train, y_train))
print(lr.score(x_test,y_test))
print(metrics.mean_squared_error(y_test,prediction))
print(metrics.r2_score(y_test,prediction))

plt.scatter(x_test, prediction)
plt.scatter(x_test, y_test)
plt.show()