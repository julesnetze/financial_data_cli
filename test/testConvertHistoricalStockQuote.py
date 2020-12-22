from unittest import TestCase

from model.convert_historical_stock_quote import convert_historical_stock_quote


class TestConvertHistoricalStockQuotes(TestCase):

    def test_should_return_float(self):
        ticker = 'AAPL'
        date = '2020-12-15'
        currency = 'EUR'

        result = convert_historical_stock_quote(date, ticker, currency)

        self.assertIsInstance(result, float)

    def test_should_raise_an_error_when_ticker_does_not_exist(self):
        ticker = 'Foo'
        date = '2020-12-15'
        currency = 'EUR'

        with self.assertRaises(KeyError):
            convert_historical_stock_quote(date, ticker, currency)

    def test_should_raise_an_error_when_currency_does_not_exist(self):
        ticker = 'AAPL'
        date = '2020-12-15'
        currency = 'Foo'

        with self.assertRaises(KeyError):
            convert_historical_stock_quote(date, ticker, currency)

    def test_should_raise_an_error_when_date_is_invalid(self):
        ticker = 'AAPL'
        date = '2000-01-01'
        currency = 'EUR'

        with self.assertRaises(KeyError):
            convert_historical_stock_quote(date, ticker, currency)