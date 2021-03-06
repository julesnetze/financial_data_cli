import time

from controller.HistoricalStockQuoteController import HistoricalStockQuoteController
from controller.HistoricalStockQuoteConverterController import HistoricalStockQuoteConverterController
from controller.LatestStockQuoteController import LatestStockQuoteController
from controller.LatestStockQuoteConverterController import LatestStockQuoteConverterController
from controller.MessageController import MessageController

message_controller = MessageController()
latest_stock_quote_controller = LatestStockQuoteController()
latest_stock_quote_converter_controller = LatestStockQuoteConverterController()
historical_stock_quote_controller = HistoricalStockQuoteController()
historical_stock_quote_converter_controller = HistoricalStockQuoteConverterController()


def application():
    print(message_controller.render_welcome_message())

    action = 0
    while action != 5:
        print(message_controller.render_options_menu())
        action = int(input("?: "))

        if action == 1:
            print(latest_stock_quote_controller.render_option_message())

            ticker = (input("Ticker: "))
            try:
                quote = latest_stock_quote_controller.latest_stock_quote(ticker)
                print(latest_stock_quote_controller.render_option_output(quote))
            except KeyError:
                print(message_controller.render_error_message())
        elif action == 2:
            print(latest_stock_quote_converter_controller.render_option_message())

            ticker = (input("Ticker: "))
            currency = (input("Currency: "))
            try:
                quote = latest_stock_quote_converter_controller.convert_latest_stock_quote(ticker, currency)
                print(latest_stock_quote_converter_controller.render_option_output(quote, currency))
            except KeyError:
                print(message_controller.render_error_message())
        elif action == 3:
            print(historical_stock_quote_controller.render_option_message())

            ticker = (input("Ticker: "))
            date = (input("Date: "))
            try:
                quote = historical_stock_quote_controller.historical_stock_quote(date, ticker)
                print(historical_stock_quote_controller.render_option_output(quote))
            except KeyError or ValueError:
                print(message_controller.render_error_message())
        elif action == 4:
            print(historical_stock_quote_converter_controller.render_option_message())

            ticker = (input("Ticker: "))
            currency = (input("Currency: "))
            date = (input("Date: "))
            try:
                quote = historical_stock_quote_converter_controller.convert_historical_stock_quote(date, ticker, currency)
                print(historical_stock_quote_converter_controller.render_option_output(quote, currency))
            except KeyError or ValueError:
                print(message_controller.render_error_message())
        time.sleep(5)


if __name__ == '__main__':
    application()
