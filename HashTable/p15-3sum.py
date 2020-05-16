from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for idx in range(length - 2):
            target = nums[idx]
            if idx > 0 and target == nums[idx - 1]:
                continue
            # 前后双指针
            l, r = idx + 1, length - 1
            while l < r:
                if (nums[l] + nums[r]) < -target:
                    l += 1
                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1
                elif (nums[l] + nums[r]) > -target:
                    r -= 1
                    while (l < r and nums[r] == nums[r + 1]):
                        r -= 1
                else:
                    result.append([target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r + 1]):
                        r -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([-1, 0, 1, 2, -1, -4])
    r2 = s.threeSum([-2, 0, 0, 2, 2])
    print(r, r2)
