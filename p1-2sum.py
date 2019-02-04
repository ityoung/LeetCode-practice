import pytest


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = dict()
        for i, d in enumerate(nums):
            expect = target - d
            if expect in data:
                return [data[expect], i]
            data[d] = i


class TestCase():
    solution = Solution()

    @pytest.mark.parametrize('nums, target, result', [
        ([2, 7, 11, 15], 9, [0, 1])
    ])
    def test_twoSum(self, nums, target, result):
        assert set(self.solution.twoSum(nums, target)) == set(result)
