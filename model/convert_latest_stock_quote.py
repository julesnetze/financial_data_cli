from model.api_calls import get_latest_stock_quote, get_latest_foreign_exchange_rate


def convert_latest_stock_quote(ticker, currency):
    quote = get_latest_stock_quote(ticker)
    exchange_rate = get_latest_foreign_exchange_rate(currency)

    return quote * exchange_rate