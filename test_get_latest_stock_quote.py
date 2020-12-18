from unittest import TestCase

from stock_quotes import get_latest_stock_quote


class TestGetLatestStockQuote(TestCase):

    def test_latest_stock_quote(self):
        result = get_latest_stock_quote('AAPL')

        self.assertIsInstance(result, float)