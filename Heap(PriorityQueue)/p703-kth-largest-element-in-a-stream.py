from typing import List

import heapq

class KthLargest:
    """Mini Heap, 只留最大的K个值，其余值丢弃。最小值在最顶端"""
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(3, [4,5,8,2])
# param_1 = obj.add(3)
# param_2 = obj.add(5)
# param_3 = obj.add(10)
# param_4 = obj.add(9)
# param_5 = obj.add(4)
# print(param_1,param_2,param_3,param_4,param_5)