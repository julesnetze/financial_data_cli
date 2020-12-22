from unittest import TestCase

from model.convert_latest_stock_quote import convert_latest_stock_quote


class TestConvertLatestStockQuote(TestCase):
    def test_should_return_float(self):
        result = convert_latest_stock_quote('AAPL', 'EUR')

        self.assertIsInstance(result, float)

    def test_should_raise_an_error_when_ticker_does_not_exist(self):
        with self.assertRaises(KeyError):
            convert_latest_stock_quote('Foo', 'EUR')

    def test_should_raise_an_error_when_currency_does_not_exist(self):
        with self.assertRaises(KeyError):
            convert_latest_stock_quote('AAPL', 'Foo')
