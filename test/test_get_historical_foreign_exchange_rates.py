from unittest import TestCase

from stock_quotes import get_historical_foreign_exchange_rates


class TestGetForeignExchangeRate(TestCase):

    def test_one_date(self):
        start_date = '2020-12-15'
        end_date = '2020-12-15'
        currency = 'EUR'
        result = get_historical_foreign_exchange_rates(start_date, end_date, currency)

        self.assertIsInstance(result, float)

    def test_two_dates(self):
        start_date = '2020-12-15'
        end_date = '2020-12-16'
        currency = 'EUR'

        result = get_historical_foreign_exchange_rates(start_date, end_date, currency)
        print(result)
        self.assertIsInstance(result, list)
        self.assertEqual(2, len(result))
