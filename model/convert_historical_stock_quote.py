from model.api_calls import get_historical_stock_quote, get_historical_foreign_exchange_rate


def convert_historical_stock_quote(date, ticker, currency):
    quote = get_historical_stock_quote(date, ticker)
    exchange_rate = get_historical_foreign_exchange_rate(date, currency)

    return quote * exchange_rate

