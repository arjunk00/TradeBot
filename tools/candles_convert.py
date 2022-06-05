import pandas as pd

read_file = pd.read_csv (r'5mins.txt')
read_file.to_csv (r'tatasteel.csv', index=None)