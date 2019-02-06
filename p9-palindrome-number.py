import pytest


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        new_integer = 0
        while x > new_integer:
            new_integer = new_integer * 10 + x % 10
            x = x // 10
        # 考虑偶数长度与奇数长度
        return new_integer == x or new_integer // 10 == x


class TestCases():
    solution = Solution()

    @pytest.mark.parametrize('x, result', [
        (11, True),
        (121, True),
        (0, True),
        (1, True),
        (-121, False),
        (123, False),
        (10, False),
        (1000021, False)
        # (9646324351, 0),
        # (1534236469, 0)
    ])
    def test_isPalindrome(self, x: int, result: bool):
        assert self.solution.isPalindrome(x) == result
