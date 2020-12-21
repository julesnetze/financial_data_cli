from unittest import TestCase

from model.api_calls import get_latest_stock_quote


class TestGetLatestStockQuote(TestCase):

    def test_should_return_float(self):
        result = get_latest_stock_quote('AAPL')

        self.assertIsInstance(result, float)

    def test_should_return_zero_when_ticker_does_not_exist(self):
        result = get_latest_stock_quote('Foo')

        self.assertEqual(0, result)

