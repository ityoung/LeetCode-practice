# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """考虑：
    1. 空链表
    2. 只有一个节点
    3. 奇数个节点
    4. 偶数个节点
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # 利用python类属性可以临时生成，来为self创建一个next，方便简化代码
        # 第一次初始化，tail相当于最开头的空节点，用于使后续流程一致
        tail, tail.next = self, head
        # tail.next、tail.next.next指接下来的第一个与第二个节点
        while tail.next and tail.next.next:
            first = tail.next
            second = first.next
            # 前一段末尾与本次遍历的第二个元素相连、第一二个节点交换位置（即交换指向的节点）
            tail.next, first.next, second.next = second, second.next, first
            # 将第二个节点作为新的链表段的末尾
            tail = first
        # 返回最初始空节点的下一节点，即头节点
        return self.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    s = Solution()
    x = s.swapPairs(n1)
    while x.next != None:
        print(x.val)
        x = x.next
    print(x.val)