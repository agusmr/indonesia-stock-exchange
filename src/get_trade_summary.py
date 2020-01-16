import json
import psycopg2
import requests
from datetime import datetime, timedelta

with open('connection.json') as f:
    CONNECTION = json.load(f)

PSQL_CONNECT = psycopg2.connect(
    host=CONNECTION.get('host'),
    port=CONNECTION.get('port'),
    database=CONNECTION.get('database'),
    user=CONNECTION.get('user'),
    password=CONNECTION.get('password')
)
CUR = PSQL_CONNECT.cursor()
LISTED_COMPANY = len(
    requests.get('https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s').json()
)
TRADING_DATE = datetime.now().strftime('%Y-%m-%d')

def main():

    url = f'https://idx.co.id/umbraco/Surface/TradingSummary/GetStockSummary?date={TRADING_DATE}&start=0&length={LISTED_COMPANY}'
    data = requests.get(url).json().get('data')

    for d in data:
        try:
            CUR.execute(
                """
                INSERT INTO trade_summary (
                    ticker_code,
                    previous,
                    open_price,
                    first_trade,
                    high_price,
                    low_price,
                    closing_price,
                    change_price,
                    trading_volume,
                    trading_value,
                    frequency,
                    index_individual,
                    offer,
                    offer_volume,
                    bid,
                    bid_volume,
                    listed_share,
                    tradeable_share,
                    weight_for_index,
                    foreign_sell,
                    foreign_buy,
                    non_regular_volume,
                    non_regular_value,
                    non_regular_frequency,
                    trading_date,
                    created_at
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                """,
                (
                    d.get('StockCode'),
                    int(d.get('Previous')),
                    int(d.get('OpenPrice')),
                    int(d.get('FirstTrade')),
                    int(d.get('High')),
                    int(d.get('Low')),
                    int(d.get('Close')),
                    int(d.get('Change')),
                    int(d.get('Volume')),
                    int(d.get('Value')),
                    int(d.get('Frequency')),
                    int(d.get('IndexIndividual')),
                    int(d.get('Offer')),
                    int(d.get('OfferVolume')),
                    int(d.get('Bid')),
                    int(d.get('BidVolume')),
                    int(d.get('ListedShares')),
                    int(d.get('TradebleShares')),
                    int(d.get('WeightForIndex')),
                    int(d.get('ForeignSell')),
                    int(d.get('ForeignBuy')),
                    int(d.get('NonRegularVolume')),
                    int(d.get('NonRegularValue')),
                    int(d.get('NonRegularFrequency')),
                    TRADING_DATE,
                    datetime.now() + timedelta(hours = 7)
                )
            )
            PSQL_CONNECT.commit()
        except psycopg2.errors.UniqueViolation:
            PSQL_CONNECT.rollback()
            pass

    CUR.close()
    PSQL_CONNECT.close()

if __name__ == "__main__":
    main()
