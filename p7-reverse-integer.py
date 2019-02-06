import pytest


class Solution:
    def is_int32(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 -1 or x < -2**31:
            return False
        return True

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not self.is_int32(x) or x == 0:
            return 0
        elif x < 0:
            return -self.reverse(-x)
        else:
            head = x // 10
            new_integer = x % 10
            while head > 0:
                remainder = head % 10
                head = head // 10
                new_integer = new_integer * 10 + remainder
            if not self.is_int32(new_integer):
                return 0
            return new_integer


class TestCases():
    solution = Solution()

    @pytest.mark.parametrize('x, result', [
        (0, 0),
        (2, 2),
        (123, 321),
        (-123, -321),
        (210, 12),
        (9646324351, 0),
        (1534236469, 0)
    ])
    def test_reverse(self, x: int, result: int):
        assert self.solution.reverse(x) == result
