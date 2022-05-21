import psycopg2
import stockfunctions

print(stockfunctions.stock_code_to_token('IDEA'))

# conn=psycopg2.connect(database="marubozu_data", user="arjun", password="1234", host="127.0.0.1", port="5432")
# cur=conn.cursor()
# file=open(r'NSE_tokens.csv', 'r')
# cur.copy_from(file, 'nse_tokens', sep=',')
# conn.commit()
# file.close()