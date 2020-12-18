"""convert and print historical stock quotes in any foreign currency (base currency is USD)

    1. GET historical stock quote
    2. GET historical foreign exchange rates
    3. Convert into another foreign currency

"""
from datetime import datetime, timezone

import requests

token = 'bvdnnkf48v6qmf0gg1s0'
base_url = 'https://finnhub.io/api/v1'


def get_latest_stock_quote(stock_ticker):
    r = requests.get(f'{base_url}/quote?symbol={stock_ticker}&token={token}')

    final_number = r.json()["c"]

    return final_number


def get_historical_stock_quote(start_date, end_date, stock_ticker):
    date_list = start_date.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    start_date = int(datetime(year, month, day, 0, 0, tzinfo=timezone.utc).timestamp())

    date_list = end_date.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    end_date = int(datetime(year, month, day, 0, 0, tzinfo=timezone.utc).timestamp())

    r = requests.get(
        f'{base_url}/stock/candle?symbol={stock_ticker}&resolution=1&from={start_date}&to={end_date}&token={token}')

    if (start_date == end_date):
        final_number = r.json()["c"][0]
    else:
        final_number = [r.json()["c"][0], r.json()["c"][-1]]

    return final_number