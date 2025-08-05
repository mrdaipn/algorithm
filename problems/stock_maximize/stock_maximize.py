from typing import List


class StockMaximize:

    def __call__(self, prices: List):
        d = len(prices) - 1
        profit = 0

        while d >= 0:
            buying_day = self.find_the_start_buying_day_since_sell_day_d(prices, d)
            profit += (d - buying_day) * prices[d] - sum(prices[buying_day:d])
            d = buying_day - 1

        return profit

    def find_the_start_buying_day_since_sell_day_d(self, prices, d):
        farest_smaller_price_day = d
        while True:
            if farest_smaller_price_day < 1:
                break
            if prices[farest_smaller_price_day - 1] <= prices[d]:
                farest_smaller_price_day -= 1
            else:
                break
        return farest_smaller_price_day
