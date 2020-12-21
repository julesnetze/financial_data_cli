from unittest import TestCase

from model.convert_historical_stock_quote import convert_historical_stock_quote


class TestConvertHistoricalStockQuotes(TestCase):

    def test_should_return_float(self):
        ticker = 'AAPL'
        date = '2020-12-15'
        currency = 'EUR'

        result = convert_historical_stock_quote(date, ticker, currency)

        self.assertIsInstance(result, float)