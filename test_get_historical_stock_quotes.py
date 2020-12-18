from unittest import TestCase

from stock_quotes import get_historical_stock_quotes

stock_ticker_APPLE = 'AAPL'


class TestGetHistoricalStockQuotes(TestCase):

    def test_one_date(self):
        start_date = '2020-12-15'
        end_date = '2020-12-15'

        result = get_historical_stock_quotes(start_date, end_date, stock_ticker_APPLE)

        self.assertIsInstance(result, float)

    def test_two_dates(self):
        start_date = '2020-12-15'
        end_date = '2020-12-16'

        result = get_historical_stock_quotes(start_date, end_date, stock_ticker_APPLE)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
