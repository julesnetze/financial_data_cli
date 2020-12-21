def options_message():
    options_message = """
    What would you like to do?

    1 - Obtain Latest Stock Quote
    2 - Obtain Latest Stock Quote in Specific Currency
    3 - Obtain Historical Stock Quote
    4 - Obtain Historical Stock Quote in Specific Currency
    5 - Exit
"""
    return options_message


def first_option():
    message = """
    Insert the Stock Ticker to Obtain Latest Stock Quote
"""
    return message


def first_option_output(quote):
    message = f'{quote} USD'
    return message


def second_option():
    message = """
    Insert the Stock Ticker and Currency to Obtain Latest Stock Quote in Specific Currency
"""
    return message


def second_option_ouput(quote, currency):
    message = f'{quote} {currency}'
    return message


def third_option():
    message = """
    Insert the Stock Ticker and the Date to Obtain Historical Stock Quote
"""
    return message


def third_option_output(quote):
    message = f'{quote} USD'
    return message


def fourth_option():
    message = """
    Insert the Stock Ticker, the Currency and the Date to Obtain Historical Stock Quote in Specific Currency
"""
    return message


def fourth_option_output(quote, currency):
    message = f'{quote} {currency}'
    return message
