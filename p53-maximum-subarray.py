import pytest


class Solution:
    """
    动态规划
    """

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = this_sum = nums[0]
        length = len(nums)
        for i in range(1, length):
            if this_sum > 0:
                this_sum += nums[i]
            else:
                this_sum = nums[i]
            max_sum = max(max_sum, this_sum)
        return max_sum


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('nums, result', [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4, 2], 7),
        ([-1], -1),
        ([-1, 0], 0)
    ])
    def test_maxSubArray(self, nums, result):
        assert self.solution.maxSubArray(nums) == result
