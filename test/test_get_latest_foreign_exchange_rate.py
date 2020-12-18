from unittest import TestCase

from stock_quotes import get_latest_foreign_exchange_rate


class TestGetLatestForeignExchangeRates(TestCase):

    def test_single_currency(self):
        result = get_latest_foreign_exchange_rate('EUR')

        self.assertIsInstance(result, float)
