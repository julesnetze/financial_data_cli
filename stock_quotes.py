"""convert and print historical stock quotes in any foreign currency (base currency is USD)

    1. GET historical stock quote
    2. GET historical foreign exchange rates
    3. Convert into another foreign currency

"""
import requests

from convert_date_to_unix import convert_to_unix_date

token = 'bvdnnkf48v6qmf0gg1s0'
base_url = 'https://finnhub.io/api/v1'


def get_latest_stock_quote(stock_ticker):
    r = requests.get(f'{base_url}/quote?symbol={stock_ticker}&token={token}')

    final_number = r.json()["c"]

    return final_number

def get_latest_foreign_exchange_rate(currency_to_exchange_to):
    r = requests.get(f'{base_url}/forex/rates?base=USD&token={token}')

    final_number = r.json()["quote"][currency_to_exchange_to]

    return final_number

def get_historical_stock_quotes(start_date, end_date, stock_ticker):
    start_date = convert_to_unix_date(start_date)

    end_date = convert_to_unix_date(end_date)

    r = requests.get(
        f'{base_url}/stock/candle?symbol={stock_ticker}&resolution=1&from={start_date}&to={end_date}&token={token}')

    if start_date == end_date:
        final_number = r.json()["c"][0]
    else:
        final_number = [r.json()["c"][0], r.json()["c"][-1]]

    return final_number

def get_historical_foreign_exchange_rates(start_date, end_date, currency_to_exchange_to):
    start_date = convert_to_unix_date(start_date)

    end_date = convert_to_unix_date(end_date)

    r = requests.get(
        f'{base_url}/forex/candle?symbol=OANDA:{currency_to_exchange_to}_USD&resolution=D&from={start_date}&to={end_date}&token={token}')

    if start_date == end_date:
        final_number = 1 / r.json()["c"][0]
    else:
        final_number = [1 / r.json()["c"][0], 1 / r.json()["c"][-1]]

    return final_number
