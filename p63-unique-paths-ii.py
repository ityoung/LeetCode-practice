import pytest
from typing import List


class Solution:
    """
    先初始化第一行和第一列，最后oj系统上的执行速度要比方法二略快一些些(56ms vs 70ms)
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        has_obstacle = False
        for i in range(1, m):
            if has_obstacle:
                dp[i][0] = 0
            elif obstacleGrid[i][0] == 1:
                has_obstacle = True
                dp[i][0] = 0
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[0][j:] = [0] * (n-j)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

class TestCase:
    solution = Solution()
    solution2 = Solution2()

    @pytest.mark.parametrize("obstacleGrid, result", [
        ([[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]], 2),
        ([[0, 0, 0],
          [1, 0, 0],
          [0, 0, 0]], 3),
        ([[0, 1, 0],
          [0, 0, 0],
          [0, 0, 0]], 3),
        ([[1, 1, 0],
          [0, 0, 0],
          [0, 0, 0]], 0),
    ])
    def test_uniquePaths(self, obstacleGrid: List[List[int]], result: int):
        assert self.solution.uniquePathsWithObstacles(obstacleGrid) == result
        assert self.solution2.uniquePathsWithObstacles(obstacleGrid) == result
