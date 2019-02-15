import pytest


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = 1
        for i in range(length -1, -1, -1):
            if digits[i] == 9 and carry == 1:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
                break
        if digits[0] == 0 and carry == 1:
            digits = [1] + digits
        return digits


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('digits, result', [
        ([1, 2, 3], [1, 2, 4]),
        ([0], [1]),
        ([9, 9, 9], [1, 0, 0, 0])
    ])
    def test_plusOne(self, digits, result):
        assert self.solution.plusOne(digits) == result
