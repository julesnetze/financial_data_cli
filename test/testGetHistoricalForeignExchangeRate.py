from unittest import TestCase

from model.api_calls import get_historical_foreign_exchange_rate


class TestGetForeignExchangeRate(TestCase):

    def test_should_return_float(self):
        date = '2020-12-15'
        currency = 'EUR'
        result = get_historical_foreign_exchange_rate(date, currency)

        self.assertIsInstance(result, float)
