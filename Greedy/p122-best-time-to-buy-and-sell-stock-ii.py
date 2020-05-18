from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 买入
        # 有更小时，放弃手中持有选择更小买入价
        # 大于买入价，卖出收益，记录
        # 第二次买入前，需要先卖出
        # 收益变小时确定卖出，开始新的交易
        earned = 0
        max_profit = 0
        buy = 10 ** 4
        for p in prices:
            if max_profit <=0 and buy > p:
                buy = p
            elif p-buy < max_profit:
                earned += max_profit
                buy = p
                max_profit = 0
            else:
                max_profit = p-buy

        return earned + max_profit


if __name__ == '__main__':
    s = Solution()
    # r = s.maxProfit([1,2,3,4,5])
    r = s.maxProfit([7,6,4,3,1])
    print(r)
    assert r == 0
    r2 = s.maxProfit([2,1,2,0,1])
    print(r2)