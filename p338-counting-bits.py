import pytest
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num+1):
            dp.append(dp[i >> 2] + (i % 2))
        return dp


class TestCase:
    solution = Solution()

    @pytest.mark.parametrize('num, result', [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2])
    ])
    def test_countBits(self, num, result):
        assert self.solution.countBits(num) == result
