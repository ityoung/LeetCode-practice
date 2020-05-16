from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff],idx]
            map[num] = idx

if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([2, 7, 11, 15], 9)
    print(r)