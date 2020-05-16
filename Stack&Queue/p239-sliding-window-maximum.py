from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window = []
        result = []
        for i, num in enumerate(nums):
            if i>=k and window[0] <= i-k:
                window.pop(0)
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                result.append(nums[window[0]])
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print(r)