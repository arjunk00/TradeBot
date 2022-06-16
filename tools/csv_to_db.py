import psycopg2
import os
# import tools.stockfunctions as stockfunctions
conn=psycopg2.connect(database="training_data", user="admin", password="xtremebutter", host="192.168.1.63", port="5432")
cur=conn.cursor()
# print(stockfunctions.stock_code_to_token('IDEA'))
L = os.listdir("/home/fernblade/TradeBot/tools/FullDataCsv")
for i in L:
    st = i[0:-4].lower()
    # query = 'CREATE TABLE {} AS (SELECT * FROM aartiind__eq__nse__nse__minute);'.format(st)
    # cur.execute(query)
    file=open(r'/home/fernblade/TradeBot/tools/FullDataCsv/'+i, 'r')
    cur.copy_from(file, st, sep=',')
    conn.commit()
    # file.close()

conn.close()