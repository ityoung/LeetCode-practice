import pytest
from typing import List


class Solution:
    def rob1(self, nums: 'List[int]') -> 'int':
        """
        LeetCode-cn上评论中的一种巧妙的动态规划解法
        :param nums:
        :return:
        """
        last = 0
        now = 0
        for i in nums:
            # 每个最大和最多能与之后的元素进行两次加和再对比
            last, now = now, max(last + i, now)
        return now

    def rob2(self, nums: 'List[int]') -> 'int':
        """
        常规的动态规划解法
        :param nums:
        :return:
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(dp[0], nums[1]))
        for i in range(2, length):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        return dp[-1]


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('nums, result', [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 7, 9, 3, 1, 3], 14),
        ([0], 0),
        ([2, 1, 1, 2], 4),
        ([], 0)
    ])
    def test_rob(self, nums, result):
        assert self.solution.rob1(nums) == result
        assert self.solution.rob2(nums) == result
