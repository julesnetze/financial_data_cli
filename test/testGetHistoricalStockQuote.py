from unittest import TestCase

from model.api_calls import get_historical_stock_quote


class TestGetHistoricalStockQuotes(TestCase):

    def test_should_return_float(self):
        ticker = 'AAPL'
        date = '2020-12-15'

        result = get_historical_stock_quote(date, ticker)

        self.assertIsInstance(result, float)
