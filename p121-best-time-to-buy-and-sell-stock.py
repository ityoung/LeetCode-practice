import pytest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :param prices: 当天的股票价格
        :return: 最多能赚的差价
        """
        if not prices:
            return 0
        max_profit = 0
        min_price = max_price = prices[0]
        length = len(prices)
        for idx in range(1, length):
            this_price = prices[idx]
            if this_price > max_price:
                max_price = this_price
                this_profit = max_price - min_price
                max_profit = max(this_profit, max_profit)
            elif this_price < min_price:
                min_price = max_price = this_price
            else:
                continue
        return max_profit


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('prices, profit', [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 1, 5, 3, 6, 4, 0, 1], 5),
        ([7, 6, 5, 4, 3], 0),
        ([], 0)
    ])
    def test_maxProfit(self, prices, profit):
        assert self.solution.maxProfit(prices) == profit
