# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """考虑：
    1. 空链表？不考虑
    2. 只有一个节点
    3. 无环
    4. 有环
    """
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        """快慢指针"""
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n2

    s = Solution()
    x = s.hasCycle(n1)
    print(x)
    assert x==False