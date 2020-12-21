import time

from model.convert_historical_stock_quotes import convert_historical_stock_quotes
from model.convert_latest_stock_quote import convert_latest_stock_quote
from stock_quotes import get_latest_stock_quote, get_historical_stock_quotes
from view.render_options_message import render_options_message
from view.render_welcome_message import render_welcome_message

first_option_message = """
    Insert the Stock Ticker to Obtain Latest Stock Quote
"""

second_option_message = """
    Insert the Stock Ticker and Currency to Obtain Latest Stock Quote in Specific Currency
"""

third_option_message = """
    Insert the Stock Ticker and the Date to Obtain Historical Stock Quote
"""

fourth_option_message = """
    Insert the Stock Ticker, the Currency and the Date to Obtain Historical Stock Quote in Specific Currency
"""

print(render_welcome_message())
print(render_options_message())

action = 0
while action != 5:
    action = int(input("?: "))

    if (action == 1):
        print(first_option_message)

        ticker = (input("Ticker: "))

        print(f'{get_latest_stock_quote(ticker)} USD')

    elif (action == 2):
        print(second_option_message)

        ticker = (input("Ticker: "))

        currency = (input("Currency: "))

        print(f'{convert_latest_stock_quote(ticker, currency)} {currency}')

    elif(action == 3):
        print(third_option_message)

        ticker = (input("Ticker: "))

        date = (input("Date: "))

        print(f'{get_historical_stock_quotes(date, date, ticker)} USD')

    elif(action == 4):
        print(fourth_option_message)

        ticker = (input("Ticker: "))

        currency = (input("Currency: "))

        date = (input("Date: "))

        print(f'{convert_historical_stock_quotes(date, date, ticker, currency)} {currency}')

    time.sleep(5)
    print(render_options_message())