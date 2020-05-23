from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxR = minR = ans = nums[0]
        for i in range(1, len(nums)):
            cmp_element = maxR*nums[i], minR*nums[i], nums[i]
            maxR = max(*cmp_element)
            minR = min(*cmp_element)
            ans = max(maxR, ans)
        return ans



if __name__ == '__main__':
    s = Solution()
    r1 = s.maxProduct([2, 3, -2, 4])
    assert r1 == 6
    r2 = s.maxProduct([-2, 0, -1])
    assert r2 == 0
    r3 = s.maxProduct([-2, 1, -1])
    assert r3 == 2
    r4 = s.maxProduct([-2, 6])
    assert r4 == 6
    r5 = s.maxProduct([0])
    assert r5 == 0
