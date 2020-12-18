from unittest import TestCase

from stock_quotes import get_historical_stock_quote

stock_ticker_APPLE = 'AAPL'
# start_date = '2020-12-15'
# end_date = '2020-12-15'

class TestHistoricalStockQuotes(TestCase):

    def test_one_date(self):
        start_date = '2020-12-15'
        end_date = '2020-12-15'
        result = get_historical_stock_quote(start_date, end_date, stock_ticker_APPLE)
        print(result)

        self.assertIsInstance(result, float)

    def test_two_dates(self):
        start_date = '2020-12-15'
        end_date = '2020-12-16'
        result = get_historical_stock_quote(start_date, end_date, stock_ticker_APPLE)
        print(result)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
