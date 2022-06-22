import csv
import pandas as pd

df = pd.read_csv('strategies\\trainingdata\\raw\\ADANIPORTS__EQ__NSE__NSE__MINUTE.csv')
df.bfill(axis='rows',inplace=True)
df.to_csv('strategies\\trainingdata\\raw\\ADANIPORTS__EQ__NSE__NSE__MINUTE.csv',index=False)

rawfile = open(r"strategies\\trainingdata\\converged\\ADANIPORTS__EQ__NSE__NSE__5MINUTE_CONVERGED.csv","r")
processedfile = open(r"strategies\\trainingdata\\processed\\ADANIPORTS__EQ__NSE__NSE__5MINUTE_TRAINING.csv","w",newline='')
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
