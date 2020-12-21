from unittest import TestCase

from model.api_calls import get_latest_stock_quote


class TestGetLatestStockQuote(TestCase):

    def test_latest_stock_quote(self):
        result = get_latest_stock_quote('AAPL')

        self.assertIsInstance(result, float)