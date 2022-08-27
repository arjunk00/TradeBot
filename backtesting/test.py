import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("BAJFINANCE__EQ__NSE__NSE__5MINUTE_CONVERGED.csv")
df_close = df['close']
print(df_close)
df_close.plot()
plt.show()