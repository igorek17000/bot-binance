import unittest

from rules.PricesRules import PricesRules


class PricesTest(unittest.TestCase):


    def test_PricesIncreaseTrue(self):
        """
            Successful execution with true result
        :return:
        """

        # Dummy result of GetRepeatedlyPrices
        dummyGetRepeatedlyPrices = ['2.10850001', '2.10850003', '2.10850005']

        # Get result
        result = PricesRules.consecutiveIncrease(dummyGetRepeatedlyPrices)

        # Expected Result
        self.assertTrue(result)


    def test_PricesIncreaseFalse(self):
        """
            Successful execution with false result
        :return:
        """

        # Dummy result of GetRepeatedlyPrices
        dummyGetRepeatedlyPrices = ['2.10850001', '2.10850005', '2.10850003']

        # Get result
        result = PricesRules.consecutiveIncrease(dummyGetRepeatedlyPrices)

        # Expected Result
        self.assertFalse(result)




if __name__ == '__main__':
    unittest.main()