from unittest import TestCase

from model.convert_latest_stock_quote import convert_latest_stock_quote


class TestConvertLatestStockQuote(TestCase):
    def test_should_return_float(self):
        result = convert_latest_stock_quote('AAPL', 'EUR')

        self.assertIsInstance(result, float)
