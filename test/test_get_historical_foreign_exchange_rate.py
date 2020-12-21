from unittest import TestCase

from stock_quotes import get_historical_foreign_exchange_rate


class TestGetForeignExchangeRate(TestCase):

    def test_one_date(self):
        date = '2020-12-15'
        currency = 'EUR'
        result = get_historical_foreign_exchange_rate(date, currency)

        self.assertIsInstance(result, float)
