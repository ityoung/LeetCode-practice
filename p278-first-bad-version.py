import pytest


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version: int) -> bool:
    if version < 5:
        return False
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while (left < right):
            mid = (right + left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


class TestCase:
    solution = Solution()

    @pytest.mark.parametrize('n, result', [
        (5, 5)
    ])
    def test_firstBadVersion(self, n, result):
        assert self.solution.firstBadVersion(n) == result
