from unittest import TestCase

from model.api_calls import get_historical_stock_quote


class TestGetHistoricalStockQuotes(TestCase):

    def test_should_return_float(self):
        ticker = 'AAPL'
        date = '2020-12-15'

        result = get_historical_stock_quote(date, ticker)

        self.assertIsInstance(result, float)

    def test_should_return_error_when_ticker_does_not_exist(self):
        ticker = 'Foo'
        date = '2020-12-15'

        with self.assertRaises(KeyError):
            get_historical_stock_quote(date, ticker)

    def test_should_return_error_when_date_is_invalid(self):
        ticker = 'AAPL'
        date = '2000-01-01'

        with self.assertRaises(KeyError):
            get_historical_stock_quote(date, ticker)