import psycopg2
from stockfunctions import token_to_stock_code

# $ psql -h localhost -d mydatabase -U myuser -p <port>

conn = psycopg2.connect(database="marubozu_data", user="admin", password="xtremebutter", host="192.168.1.25", port="5432")


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
        create_ifnot_exists = 'CREATE TABLE IF NOT EXISTS {}(token BIGINT NOT NULL, t_stamp TIMESTAMP WITHOUT TIME ZONE NOT NULL, ltp DOUBLE PRECISION, volume_traded BIGINT,total_bids BIGINT, total_offers BIGINT)'.format(token_to_stock_code(tick['instrument_token']))
        cur.execute(create_ifnot_exists)
        insert_into_table='INSERT INTO {}(token, t_stamp, ltp, volume_traded, total_bids, total_offers) VALUES (%(token)s, %(t_stamp)s, %(ltp)s, %(volume_traded)s, %(total_bids)s, %(total_offers)s)'.format(token_to_stock_code(tick['instrument_token']))
        depth = tick['depth']
        bidask_info = {'total_bids':0,'total_offers':0}
        for i in depth['buy']:
            bidask_info['total_bids'] += i['quantity']*i['orders']
        for j in depth['sell']:
            bidask_info['total_offers'] += i['quantity']*i['orders']
        cur.execute(insert_into_table, {
            "token": tick["instrument_token"],
            "t_stamp": tick["last_trade_time"],
            "ltp": tick["last_price"],
            "volume_traded": tick["volume_traded"],
            "total_bids": bidask_info['total_bids'],
            "total_offers": bidask_info['total_offers']})
        conn.commit()
