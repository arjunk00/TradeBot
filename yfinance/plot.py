import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ADANIPORTS__EQ__NSE__NSE__5MINUTE_CONVERGED.csv")

df1 = np.array(df["close"])
df1 = np.delete(df1,-1)

df2 = np.array(df["close"])
df2 = np.delete(df2,0)

print(len(df1))
print(len(df2))

plt.scatter(df1, df2)
plt.show()