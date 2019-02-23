import pytest


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2, length):
            dp.append(min(dp[i - 2] + cost[i], dp[i - 1] + cost[i]))
        return min(dp[-1], dp[-2])


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('cost, result', [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
    ])
    def test_minCostClimbingStairs(self, cost, result):
        assert self.solution.minCostClimbingStairs(cost) == result
