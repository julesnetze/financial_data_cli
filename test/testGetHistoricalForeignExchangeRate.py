from unittest import TestCase

from model.api_calls import get_historical_foreign_exchange_rate


class TestGetForeignExchangeRate(TestCase):

    def test_should_return_float(self):
        date = '2020-12-15'
        currency = 'EUR'
        result = get_historical_foreign_exchange_rate(date, currency)

        self.assertIsInstance(result, float)

    def test_should_raise_when_currency_does_not_exist(self):
        date = '2020-12-15'
        currency = 'Foo'

        with self.assertRaises(KeyError):
            get_historical_foreign_exchange_rate(date, currency)

    def test_should_raise_error_when_date_is_invalid(self):
        date = '2000-01-01'
        currency = 'EUR'

        with self.assertRaises(TypeError):
            get_historical_foreign_exchange_rate(date, currency)
