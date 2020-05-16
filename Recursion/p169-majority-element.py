from typing import List

class Solution:
    """
    执行用时 :60 ms, 在所有 Python3 提交中击败了51.08%的用户 O(n)
    内存消耗 :15.2 MB, 在所有 Python3 提交中击败了6.90%的用户 O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:
        map = dict()
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        max_ = 0
        max_num = None
        for n, v in map.items():
            if v > max_:
                max_, max_num = v, n
        return max_num

class Solution2:
    """
    题干重点：多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素，利用类似栈的方式找最多出现的值
    执行用时 :48 ms, 在所有 Python3 提交中击败了80.79%的用户 O(n)
    内存消耗 :15.1 MB, 在所有 Python3 提交中击败了6.90%的用户 O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        now_num = None
        now_count = 0
        for n in nums:
            if now_count == 0:
                now_count += 1
                now_num = n
                continue
            if n == now_num:
                now_count += 1
            else:
                now_count -= 1
        return now_num

if __name__ == '__main__':
    s = Solution2()
    r = s.majorityElement([2,2,1,1,1,2,2])
    print(r)