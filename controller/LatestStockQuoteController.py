from model.api_calls import get_latest_stock_quote
from view.options_messages import first_option, first_option_output


class LatestStockQuoteController:

    def render_option_message(self):
        return first_option()

    def latest_stock_quote(self, ticker):
        return get_latest_stock_quote(ticker)

    def render_option_output(self, quote):
        return first_option_output(quote)


