import pytest


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if nums[i] >= target:
                return i
        return length


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('nums, target, result', [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 0, 0),
        ([], 1, 0),
        ([1, 3, 5, 6], 9, 4),
    ])
    def test_searchInsert(self, nums, target, result):
        assert self.solution.searchInsert(nums, target) == result
