import requests

from model.convert_date_to_unix import convert_to_unix_date

token = 'bvdnnkf48v6qmf0gg1s0'
base_url = 'https://finnhub.io/api/v1'


def get_latest_stock_quote(ticker):
    response = requests.get(f'{base_url}/quote?symbol={ticker}&token={token}')
    stock_quote = response.json()["c"]
    if stock_quote == 0:
        raise KeyError
    return stock_quote


def get_latest_foreign_exchange_rate(currency):
    response = requests.get(f'{base_url}/forex/rates?base=USD&token={token}')
    exchange_rate = response.json()["quote"][currency]
    return exchange_rate


def get_historical_stock_quote(date, ticker):
    date = convert_to_unix_date(date)

    response = requests.get(
        f'{base_url}/stock/candle?symbol={ticker}&resolution=1&from={date}&to={date}&token={token}')
    stock_quote = response.json()["c"][0]

    return stock_quote


def get_historical_foreign_exchange_rate(date, currency):
    date = convert_to_unix_date(date)

    response = requests.get(
        f'{base_url}/forex/candle?symbol=OANDA:{currency}_USD&resolution=D&from={date}&to={date}&token={token}')
    exchange_rate = 1 / response.json()["c"][0]

    return exchange_rate
