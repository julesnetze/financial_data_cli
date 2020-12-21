import requests

from convert_date_to_unix import convert_to_unix_date

token = 'bvdnnkf48v6qmf0gg1s0'
base_url = 'https://finnhub.io/api/v1'


def get_latest_stock_quote(ticker):
    r = requests.get(f'{base_url}/quote?symbol={ticker}&token={token}')

    final_number = r.json()["c"]

    return final_number

def get_latest_foreign_exchange_rate(currency):
    r = requests.get(f'{base_url}/forex/rates?base=USD&token={token}')

    final_number = r.json()["quote"][currency]

    return final_number

def get_historical_stock_quote(date, ticker):
    date = convert_to_unix_date(date)

    r = requests.get(
        f'{base_url}/stock/candle?symbol={ticker}&resolution=1&from={date}&to={date}&token={token}')
    final_number = r.json()["c"][0]

    return final_number

def get_historical_foreign_exchange_rate(date, currency):
    date = convert_to_unix_date(date)

    r = requests.get(
        f'{base_url}/forex/candle?symbol=OANDA:{currency}_USD&resolution=D&from={date}&to={date}&token={token}')
    final_number = 1 / r.json()["c"][0]

    return final_number
