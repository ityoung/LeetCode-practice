import pytest

# TODO: enhance. This solution takes 92ms
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        index = 0

        while index < length - 1:
            if nums[index] == nums[index + 1]:
                del nums[index]
                length -= 1
            else:
                index += 1
        return length


class TestCase(object):
    solution = Solution()

    @pytest.mark.parametrize('nums, result', [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ])
    def test_removeDuplicates(self, nums, result):
        assert self.solution.removeDuplicates(nums) == result
