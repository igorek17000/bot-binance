from binance import Client

class PricesRules:

    client = None

    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    @staticmethod
    def consecutiveIncrease(allPrices):
        """
            Check if all prices are increasing
        :param allPrices: list of prices
        :return: bolean
        """

        # Check if prices are incremental
        lastPrice = float(0)
        for item in allPrices:

            itemF = float(item)

            # Check if price is higher than previous
            if( itemF > lastPrice):
                lastPrice = itemF
            else:
                return False

        return True
