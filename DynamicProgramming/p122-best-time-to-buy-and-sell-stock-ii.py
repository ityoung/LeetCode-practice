from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold = prices[0]
        for p in prices:
            # 大于则卖，小于则丢弃持有
            if p > hold:
                profit += p - hold
            hold = p
        return profit

if __name__ == '__main__':
    s = Solution()
    r = s.maxProfit([7, 6, 4, 3, 1])
    print(r)
    assert r == 0
