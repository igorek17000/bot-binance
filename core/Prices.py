from binance import Client

from exceptions.PriceException import PriceException
from utils.DateUtils import DateUtils



class Prices:

    client = None

    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)


    def getAllPricePair(self) :
        """
            Get all pair prices
        :return:    collection with all pair prices
        """
        result = self.client.get_all_tickers()

        if(len(result) > 0):
            return result
        else:
            raise PriceException("Any price pair was not found.")


    def getPricePair(self, pairCoins):
        """
            Get a price pair of coins
        :param pairCoins:   name of a pair
        :return:    list with symbol and price
        """

        # Get and filter the list
        result = list(
            filter(
                lambda x: x['symbol'] == pairCoins,
                self.getAllPricePair()
            )
        )

        # Result
        if  len(result) > 0:
            return result
        else:
            raise PriceException(f'Price pair {pairCoins} was not found.')


    def getRepeatedlyPrices(self, pairCoins, numTimes, secondsSleep=0.0):
        """
            Get the pair price up to repetitions number
        :param pairCoins:       coins par
        :param numTimes:        repetitions number
        :param secondsSleep:    time to sleep every loop
        :return:    all prices
        """

        def getLine():
            DateUtils.delaySeconds(secondsSleep)
            return self.getPricePair(pairCoins).__getitem__(0).get("price")

        allPrices = list( map( lambda x: getLine(), range(numTimes) ) )


        # Result has to be at least equal to target repetitions
        if( len(allPrices) >= numTimes ):
            return allPrices
        else:
            raise PriceException(f'The price pair were not found for {str(numTimes)} repetitions.')
