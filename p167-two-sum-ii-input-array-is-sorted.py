import pytest


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = dict()
        length = len(nums)
        i1 = 0
        i2 = length - 1
        sum_result = nums[i1] + nums[i2]
        while i1 < i2:
            if sum_result == target:
                return [i1 + 1, i2 + 1]
            elif sum_result < target:
                i1 += 1
            else:
                i2 -= 1
            sum_result = nums[i1] + nums[i2]

        # for i1 in range(0, length - 1):
        #     print('i1: ', i1)
        #     d1 = nums[i1]
        #     print('d1: ', d1)
        #     for i2 in range(length, i1, -1):
        #         print('i2: ', i2)
        #         d2 = nums[i2]
        #         print('d2: ', d2)
        #         sum_result = d1 + d2
        #         if sum_result == target:
        #             return [d1, d2]
        #         elif sum_result > target:
        #             continue
        #         else:
        #             break


class TestCase():
    solution = Solution()

    @pytest.mark.parametrize('nums, target, result', [
        ([2, 7, 11, 15], 9, [1, 2])
    ])
    def test_twoSum(self, nums, target, result):
        assert set(self.solution.twoSum(nums, target)) == set(result)


if __name__ == '__main__':
    pytest.main()