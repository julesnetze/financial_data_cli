from stock_quotes import get_latest_stock_quote, get_latest_foreign_exchange_rate


def convert_latest_stock_quote(stock_ticker, currency_to_exchange_to):
    stock_price = get_latest_stock_quote(stock_ticker)
    exchange_rate = get_latest_foreign_exchange_rate(currency_to_exchange_to)

    return stock_price * exchange_rate