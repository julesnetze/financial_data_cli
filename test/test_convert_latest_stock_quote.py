from unittest import TestCase

from convert_latest_stock_quote import convert_latest_stock_quote


class TestConvertLatestStockQuote(TestCase):
    def test_convert_latest_stock_quote(self):
        result = convert_latest_stock_quote('AAPL', 'EUR')

        self.assertIsInstance(result, float)
