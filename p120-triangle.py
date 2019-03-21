import pytest
from typing import List


class Solution:
    """自顶向下。两种解法复杂度差不多，解法二更巧妙一些。"""

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        dp = [0] * length
        dp[0] = triangle[0][0]
        for i in range(1, length):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]

        minimal = dp[0]
        for i in dp[1:]:
            minimal = i if i < minimal else minimal
        return minimal


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 从倒数第二行开始，自底向上
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


class TestCase:
    solution = Solution()
    solution2 = Solution2()

    @pytest.mark.parametrize('triangle, result', [
        ([[2]], 2),
        ([[2], [3, 4], ], 5),
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-1], [-2, -3]], -4),
        ([[-1], [3, 2], [-3, -1, -2]], -1)
    ])
    def test_minimumTotal(self, triangle, result):
        assert self.solution.minimumTotal(triangle) == result
        assert self.solution2.minimumTotal(triangle) == result
