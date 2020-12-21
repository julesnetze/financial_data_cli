from unittest import TestCase

from model.convert_historical_stock_quotes import convert_historical_stock_quote

ticker = 'AAPL'

class TestConvertHistoricalStockQuotes(TestCase):

    def test_one_date(self):
        date = '2020-12-15'
        currency = 'EUR'

        result = convert_historical_stock_quote(date, ticker, currency)

        self.assertIsInstance(result, float)