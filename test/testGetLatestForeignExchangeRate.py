from unittest import TestCase

from model.api_calls import get_latest_foreign_exchange_rate


class TestGetLatestForeignExchangeRates(TestCase):

    def test_should_return_float(self):
        result = get_latest_foreign_exchange_rate('EUR')

        self.assertIsInstance(result, float)

    def test_should_raise_an_error_when_currency_does_not_exist(self):
        with self.assertRaises(KeyError):
            get_latest_foreign_exchange_rate('Foo')

