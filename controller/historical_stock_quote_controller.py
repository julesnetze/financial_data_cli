from stock_quotes import get_historical_stock_quote
from view.options_messages import third_option, third_option_output


class HistoricalStockQuoteController:

    def render_option_message(self):
        return third_option()

    def historical_stock_quote(self, date, ticker):
        return get_historical_stock_quote(date, ticker)

    def render_option_ouput(self, quote):
        return third_option_output(quote)