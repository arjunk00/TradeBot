import csv
import pandas as pd

stock_code = "ADANIPORTS"

df = pd.read_csv('strategies\\trainingdata\\raw\\{}__EQ__NSE__NSE__MINUTE.csv'.format(stock_code))
df.bfill(axis='rows',inplace=True)
df.to_csv('strategies\\trainingdata\\raw\\{}__EQ__NSE__NSE__MINUTE.csv'.format(stock_code),index=False)

rawfile = open("strategies\\trainingdata\\converged\\{}__EQ__NSE__NSE__5MINUTE_CONVERGED.csv".format(stock_code),"r")
processedfile = open("strategies\\trainingdata\\processed\\{}__EQ__NSE__NSE__5MINUTE_TRAINING.csv".format(stock_code),"w",newline='')
csvreader = csv.reader(rawfile)
csvwriter = csv.writer(processedfile)


#checks current row to find ideal signal for previous
rowlst = []
header = next(csvreader)
header.append("Movement")
csvwriter.writerow(header)
for row in csvreader:
    if len(rowlst) < 1:
        rowlst.append(row)
    else:
        rowlst.append(row)
        prevrow = rowlst[0]
        currow = rowlst[1]
        if currow[1] >= currow[-2]:
            sig = 0
        else:
            sig = 1
        prevrow.append(sig)
        csvwriter.writerow(prevrow)
        del rowlst[0]

rawfile.close()
processedfile.close()              
