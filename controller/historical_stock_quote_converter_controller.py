from model.convert_historical_stock_quote import convert_historical_stock_quote
from view.options_messages import fourth_option, fourth_option_output


class HistoricalStockQuoteConverterController:

    def render_option_message(self):
        return fourth_option()

    def convert_historical_stock_quote(self, date, ticker, currency):
        return convert_historical_stock_quote(date, ticker, currency)

    def render_option_ouput(self, quote, currency):
        return fourth_option_output(quote, currency)