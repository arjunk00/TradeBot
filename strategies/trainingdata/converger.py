import sys

sys.path.insert(0, '../tools')
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


df = pd.read_csv('strategies\\trainingdata\\raw\\ADANIPORTS__EQ__NSE__NSE__MINUTE.csv')
df.bfill(axis='rows',inplace=True)
df.to_csv('strategies\\trainingdata\\raw\\ADANIPORTS__EQ__NSE__NSE__MINUTE.csv',index=False)

n = 5
rawfile = open(r"strategies\\trainingdata\\raw\\ADANIPORTS__EQ__NSE__NSE__MINUTE.csv","r")
processedfile = open("strategies\\trainingdata\\converged\\ADANIPORTS__EQ__NSE__NSE__{}MINUTE_CONVERGED.csv".format(str(n)),"w",newline='')
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