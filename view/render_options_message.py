def render_options_message():
    options_message = """
    What would you like to do?

    1 - Obtain Latest Stock Quote
    2 - Obtain Latest Stock Quote in Specific Currency
    3 - Obtain Historical Stock Quote
    4 - Obtain Historical Stock Quote in Specific Currency
    5 - Exit
"""
    return options_message

# def render_first_option():
#     first_option_message = """
#     Insert the Stock Ticker to Obtain Latest Stock Quote
# """
#
#     ticker = (input("Ticker: "))
#
#     print(f'{get_latest_stock_quote(ticker)} USD')
#