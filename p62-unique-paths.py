import pytest


class Solution:
    """
    动态规划二维数组解法。
    二维数组的第一行与第一列值均为1，其他单元的值为该单元左+该单元上的值
    """

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]


class Solution2:
    """
    动态规划单数组解决方法。
    数组中的值表示该行/列的最后一个值的大小，当计算完毕，数组的最后一位即为所求值
    """

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        # 已经初始化第一列为1，及计算的次数应当减1
        for i in range(m - 1):
            up_cell = 1
            for j in range(1, n):
                dp[j] = dp[j] + up_cell
                up_cell = dp[j]
        return dp[-1]


class TestCase:
    solution = Solution()
    solution2 = Solution2()

    @pytest.mark.parametrize("m, n, result", [
        (2, 3, 3),
        (1, 2, 1),
        (7, 3, 28)
    ])
    def test_uniquePaths(self, m: int, n: int, result: int):
        assert self.solution.uniquePaths(m, n) == result
        assert self.solution2.uniquePaths(m, n) == result
