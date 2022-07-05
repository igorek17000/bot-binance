import unittest
from unittest.mock import MagicMock

from core import Prices


class PricesTest(unittest.TestCase):


    def test_getAllPricePairSuccessful(self):
        """
            Check structure of getAllPricePair
        :return:
        """

        # Class instance
        prices = Prices('', '')

        # Get price pair
        price = prices.getAllPricePair()

        # Get first position
        first = price.__getitem__(0)
        length = len(first)

        # Expected Result
        self.assertTrue(length == 2)
        self.assertTrue(first.__contains__("price"))
        self.assertTrue(first.__contains__("symbol"))


    def test_getAllPricePairException(self):
        """
            Throws error because any price pair was found
        :return:
        """

        # Class instance
        prices = Prices('', '')


        # Mock result of get_all_tickers
        dummyResult = []
        prices.client.get_all_tickers = MagicMock(return_value=dummyResult)

        # Expected result
        with self.assertRaises(Exception) as context:
            prices.getAllPricePair()  # Get price pair

        self.assertEqual(context.exception.__class__.__name__, 'PriceException')


    def test_getPricePairSuccessful(self):
        """
            Successful execution
        :return:
        """

        # Class instance
        prices = Prices('', '')

        # Mock result of getAllPricePair
        dummyResult = [
            {'symbol': 'ETHBTC',    'price': '0.06700200'},
            {'symbol': 'LUNABUSD',  'price': '1.97550000'},
            {'symbol': 'LTCBTC',    'price': '0.00234200'}
        ]
        prices.getAllPricePair = MagicMock(return_value=dummyResult)

        # Get price pair
        price = prices.getPricePair('LUNABUSD')

        # Expected Result
        expected = [{'price': '1.97550000', 'symbol': 'LUNABUSD'}]
        self.assertEqual(expected, price)


    def test_getPricePairException(self):
        """
            Throws exception for not finding the pair
        :return:
        """


        # Class instance
        prices = Prices('', '')

        # Mock result of getAllPricePair
        dummyResult = [ {'symbol': 'LTCBTC', 'price': '0.06700200'}, ]
        prices.getAllPricePair = MagicMock(return_value=dummyResult)


        # Expected result
        with self.assertRaises(Exception) as context:
            prices.getPricePair('LUNABUSD')  # Get price pair

        self.assertEqual(context.exception.__class__.__name__, 'PriceException')
        self.assertEqual(context.exception.__getattribute__("message"), "Price pair LUNABUSD was not found.")



    def test_getRepeatedlyPricesSuccessful(self):
        """
            Successful execution
        :return:
        """

        # Class instance
        prices = Prices('', '')

        # Mock result of getPricePair
        dummyGetPricePair = [
            [{'symbol': 'LUNABUSD', 'price': '2.10850001'}],
            [{'symbol': 'LUNABUSD', 'price': '2.10850003'}],
            [{'symbol': 'LUNABUSD', 'price': '2.10850007'}]
        ]
        Prices.getPricePair = MagicMock(side_effect=dummyGetPricePair)


        # Get price pairs
        result = prices.getRepeatedlyPrices('LUNABUSD', 3)

        # Expected result
        dummyResult = ['2.10850001', '2.10850003', '2.10850007']
        length = len(result)

        self.assertTrue(length == 3)
        self.assertEqual(dummyResult, result)



    def test_getRepeatedlyPricesException(self):
        """
            Throws exception for no finding the target repetitions
        :return:
        """

        # Class instance
        prices = Prices('', '')

        # Mock result of getPricePair
        dummyGetPricePair = [
            [{'symbol': 'LUNABUSD', 'price': '2.10850001'}],
            [{'symbol': 'LUNABUSD', 'price': '2.10850004'}]
        ]
        Prices.getPricePair = MagicMock(side_effect=dummyGetPricePair)


        # Expected result
        repetitions = 3
        with self.assertRaises(Exception) as context:
            prices.getRepeatedlyPrices('LUNABUSD', repetitions)  # Get price pairs

        self.assertEqual(context.exception.__class__.__name__, 'PriceException')
        self.assertEqual(context.exception.__getattribute__("message"),
                         f'The price pair were not found for {repetitions} repetitions.')



if __name__ == '__main__':
    unittest.main()