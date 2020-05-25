from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mini = prices[0]
        max_profit = 0
        for i in prices[1:]:
            if i < mini:
                mini = i
            else:
                max_profit = max(i - mini, max_profit)
        return max_profit

if __name__ == '__main__':
    s = Solution()
    r = s.maxProfit([7,6,4,3,1])
    print(r)
    assert r == 0
