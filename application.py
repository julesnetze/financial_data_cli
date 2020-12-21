import time

from controller.historical_stock_quote_controller import HistoricalStockQuoteController
from controller.latest_stock_quote_controller import LatestStockQuoteController
from controller.latest_stock_quote_converter_controller import LatestStockQuoteConverterController
from model.convert_historical_stock_quotes import convert_historical_stock_quote
from stock_quotes import get_historical_stock_quote
from view.options_messages import options_message
from view.welcome_message import render_welcome_message

fourth_option_message = """
    Insert the Stock Ticker, the Currency and the Date to Obtain Historical Stock Quote in Specific Currency
"""

print(render_welcome_message())
print(options_message())

latest_stock_quote_controller = LatestStockQuoteController()
latest_stock_quote_converter_controller = LatestStockQuoteConverterController()
historical_stock_quote_controller = HistoricalStockQuoteController()

action = 0
while action != 5:
    action = int(input("?: "))

    if (action == 1):
        print(latest_stock_quote_controller.render_option_message())

        ticker = (input("Ticker: "))
        quote = latest_stock_quote_controller.latest_stock_quote(ticker)

        print(latest_stock_quote_controller.render_option_ouput(quote))
    elif (action == 2):
        print(latest_stock_quote_converter_controller.render_option_message())

        ticker = (input("Ticker: "))
        currency = (input("Currency: "))
        quote = latest_stock_quote_converter_controller.convert_latest_stock_quote(ticker, currency)

        print(latest_stock_quote_converter_controller.render_option_ouput(quote, currency))
    elif(action == 3):
        print(historical_stock_quote_controller.render_option_message())

        ticker = (input("Ticker: "))
        date = (input("Date: "))
        quote = historical_stock_quote_controller.historical_stock_quote(date, ticker)

        print(historical_stock_quote_controller.render_option_ouput(quote))

    elif(action == 4):
        print(fourth_option_message)

        ticker = (input("Ticker: "))

        currency = (input("Currency: "))

        date = (input("Date: "))

        print(f'{convert_historical_stock_quote(date, date, ticker, currency)} {currency}')

    time.sleep(5)
    print(options_message())