from unittest import TestCase

from model.convert_historical_stock_quotes import convert_historical_stock_quotes

stock_ticker = 'AAPL'

class TestConvertHistoricalStockQuotes(TestCase):

    def test_one_date(self):
        start_date = '2020-12-15'
        end_date = '2020-12-15'
        currency = 'EUR'

        result = convert_historical_stock_quotes(start_date, end_date, stock_ticker, currency)

        self.assertIsInstance(result, float)

    def test_two_dates(self):
        start_date = '2020-12-15'
        end_date = '2020-12-16'
        currency = 'EUR'

        result = convert_historical_stock_quotes(start_date, end_date, stock_ticker, currency)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)