def options_menu():
    message = """
    What would you like to do?

    1 - Obtain Latest Stock Quote
    2 - Obtain Latest Stock Quote in Specific Currency
    3 - Obtain Historical Stock Quote
    4 - Obtain Historical Stock Quote in Specific Currency
    5 - Exit
"""
    return message


def first_option():
    message = """
    Insert the Stock Ticker to Obtain Latest Stock Quote(e.g. AAPL)
"""
    return message


def first_option_output(quote):
    quote_formatted = "{:.2f}".format(quote)
    message = f'{quote_formatted} USD'
    return message


def second_option():
    message = """
    Insert the Stock Ticker and Currency to Obtain Latest Stock Quote in Specific Currency(e.g. AAPL, EUR)
"""
    return message


def second_option_ouput(quote, currency):
    quote_formatted = "{:.2f}".format(quote)
    message = f'{quote_formatted} {currency}'
    return message


def third_option():
    message = """
    Insert the Stock Ticker and the Date to Obtain Historical Stock Quote (e.g. AAPL, 2020-12-15)
"""
    return message


def third_option_output(quote):
    quote_formatted = "{:.2f}".format(quote)
    message = f'{quote_formatted} USD'
    return message


def fourth_option():
    message = """Insert the Stock Ticker, the Currency and the Date to Obtain Historical Stock Quote in Specific Currency(e.g. AAPL, EUR, 2020-12-15) """
    return message


def fourth_option_output(quote, currency):
    quote_formatted = "{:.2f}".format(quote)
    message = f'{quote_formatted} {currency}'
    return message
