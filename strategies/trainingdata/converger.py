import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import csv
import pandas as pd
# from stockfunctions import converger
def converger(listofrows): #converge n DOHLCV rows into one
    D = listofrows[0][0]
    O = listofrows[0][1]
    C = listofrows[-1][-2]
    Lh = []
    Ll = []
    V = 0
    for row in listofrows:
        Lh.append(float(row[2]))
        Ll.append(float(row[3]))
        V += float(row[-1])
    H = max(Lh)
    L = min(Ll)

    return [D,O,H,L,C,V]

stock_code = "BAJFINANCE"

df = pd.read_csv(f'{os.path.dirname(os.path.realpath(__file__))}/raw/{stock_code}__EQ__NSE__NSE__MINUTE.csv')
df.bfill(axis='rows',inplace=True)
df.to_csv(f'{os.path.dirname(os.path.realpath(__file__))}/raw/{stock_code}__EQ__NSE__NSE__MINUTE.csv',index=False)

n = 5
rawfile = open(f"{os.path.dirname(os.path.realpath(__file__))}/raw/{stock_code}__EQ__NSE__NSE__MINUTE.csv","r")
processedfile = open(f"{os.path.dirname(os.path.realpath(__file__))}/converged/{stock_code}__EQ__NSE__NSE__{n}MINUTE_CONVERGED.csv","w",newline='')
csvreader = csv.reader(rawfile)
csvwriter = csv.writer(processedfile)

rowlst = []
header = next(csvreader)
csvwriter.writerow(header)
for row in csvreader:
    if len(rowlst) < n:
        rowlst.append(row)
    else:
        convrow = converger(rowlst)
        csvwriter.writerow(convrow)
        rowlst = [row]
    
rawfile.close()
processedfile.close()