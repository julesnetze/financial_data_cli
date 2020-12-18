from stock_quotes import get_historical_stock_quotes, get_historical_foreign_exchange_rates


def convert_historical_stock_quotes(start_date, end_date, stock_ticker, currency_to_exchange_to):
    stock_prices = get_historical_stock_quotes(start_date, end_date, stock_ticker)
    exchange_rates = get_historical_foreign_exchange_rates(start_date, end_date, currency_to_exchange_to)

    if start_date == end_date:
        final_number = stock_prices * exchange_rates
    else:
        final_number = [stock_prices[0] * exchange_rates[0], stock_prices[1] * exchange_rates[1]]

    return final_number

