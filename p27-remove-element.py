import pytest


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        count = 0
        for i in range(length - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
                count += 1
        return length - count


class TestCases(object):
    solution = Solution()

    @pytest.mark.parametrize('nums, val, result', [
        ([3, 2, 2, 3], 2, 2),
        ([3, 2, 2, 3], 1, 4),
        ([0,1,2,2,3,0,4,2], 2, 5)
    ])
    def test_removeElement(self, nums, val, result):
        assert self.solution.removeElement(nums, val) == result
