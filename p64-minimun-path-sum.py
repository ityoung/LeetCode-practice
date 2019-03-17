import pytest
from typing import List


class Solution:
    """
    动态规划一维数组解法
    """

    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        m = len(grid)
        if m == 0:
            return 0
        if m == 1:
            return sum(grid[0])
        n = len(grid[0])
        dp = [grid[0][0]]
        # 为第一列先累加
        for j in range(1, m):
            dp.append(dp[j - 1] + grid[j][0])
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[j] = dp[j] + grid[j][i]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[j][i]
        return dp[-1]


class Solution2:
    """
    动态规划直接修改原二维数组解法, 不过会消耗更多内存
    """

    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        m = len(grid)
        if m == 0:
            return 0
        if m == 1:
            return sum(grid[0])
        n = len(grid[0])
        # 为第一行和第一列先累加
        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for j in range(1, m):
            grid[j][0] = grid[j - 1][0] + grid[j][0]
        for i in range(1, n):
            for j in range(1, m):
                grid[j][i] = min(grid[j - 1][i], grid[j][i - 1]) + grid[j][i]
        return grid[-1][-1]


class TestCase:
    solution = Solution()
    solution2 = Solution2()

    @pytest.mark.parametrize('grid, result', [
        ([[1, 3, 1],
          [1, 5, 1],
          [4, 2, 1]], 7),
        ([[1, 2],
          [1, 1]], 3),
        ([[1, 2],
          [5, 6],
          [1, 1]], 8)
    ])
    def test_minPathSum(self, grid, result):
        assert self.solution.minPathSum(grid) == result
        assert self.solution2.minPathSum(grid) == result
