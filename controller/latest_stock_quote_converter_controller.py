from model.convert_latest_stock_quote import convert_latest_stock_quote
from view.options_messages import second_option, second_option_ouput


class LatestStockQuoteConverterController:

    def render_option_message(self):
        return second_option()

    def convert_latest_stock_quote(self, ticker, currency):
        return convert_latest_stock_quote(ticker, currency)

    def render_option_ouput(self, quote, currency):
        return second_option_ouput(quote, currency)