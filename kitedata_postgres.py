import psycopg2
from stockfunctions import token_to_stock_code

# $ psql -h localhost -d mydatabase -U myuser -p <port>

conn = psycopg2.connect(database="marubozu_data", user="arjun", password="1234", host="127.0.0.1", port="5432")


# create_table_query = ''' CREATE TABLE ticks
# ( token  integer  NOT NULL,
#   price  double precision);'''
#
# cur=conn.cursor()
# cur.execute(create_table_query)
# conn.commit()



def insert_ticks(ticks):
    cur = conn.cursor()
    for tick in ticks:
        create_ifnot_exists = 'CREATE TABLE IF NOT EXISTS {}(token BIGINT NOT NULL, t_stamp TIMESTAMP WITHOUT TIME ZONE NOT NULL, ltp DOUBLE PRECISION, volume_traded BIGINT)'.format(token_to_stock_code(tick['instrument_token']))
        cur.execute(create_ifnot_exists)
        insert_into_table='INSERT INTO {}(token, t_stamp, ltp, volume_traded) VALUES (%(token)s, %(t_stamp)s, %(ltp)s, %(volume_traded)s)'.format(token_to_stock_code(tick['instrument_token']))
        cur.execute(insert_into_table, {
            "token": tick["instrument_token"],
            "t_stamp": tick["last_trade_time"],
            "ltp": tick["last_price"],
            "volume_traded":tick["volume_traded"]})
        conn.commit()
