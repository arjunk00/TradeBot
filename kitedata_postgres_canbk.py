import psycopg2

# $ psql -h localhost -d mydatabase -U myuser -p <port>

conn = psycopg2.connect(database="marubozu_data", user="arjun", password="1234", host="127.0.0.1", port="5432")


# create_table_query = ''' CREATE TABLE ticks
# ( token  integer  NOT NULL,
#   price  double precision);'''
#
# cur=conn.cursor()
# cur.execute(create_table_query)
# conn.commit()

insert_into_table='INSERT INTO canbk(token, t_stamp, ltp, volume_traded) VALUES (%(token)s, %(t_stamp)s, %(ltp)s, %(volume_traded)s)'

def insert_ticks(ticks):
    cur = conn.cursor()
    for tick in ticks:
        cur.execute(insert_into_table, {
            "token": tick["instrument_token"],
            "t_stamp": tick["last_trade_time"],
            "ltp": tick["last_price"],
            "volume_traded":tick["volume_traded"]})
        conn.commit()
