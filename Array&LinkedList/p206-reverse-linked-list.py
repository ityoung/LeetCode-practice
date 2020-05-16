# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """递归
    执行用时 :56 ms, 在所有 Python3 提交中击败了24.68%的用户
    内存消耗 :18.6 MB, 在所有 Python3 提交中击败了5.88%的用户
    """
    tail = None
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next:
            sub_list = self.reverseList(head.next)
            self.tail.next = head
            head.next = None
            self.tail = head
            return sub_list
        else:
            self.tail = head
            return head

class Solution2:
    """迭代
    执行用时 :36 ms, 在所有 Python3 提交中击败了92.88%的用户
    内存消耗 :14.5 MB, 在所有 Python3 提交中击败了20.59%的用户
    """
    def reverseList(self, head: ListNode) -> ListNode:
        cur, new_head = head, None
        while cur:
            cur.next, new_head, cur = new_head, cur, cur.next
        return new_head



if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution2()
    x = s.reverseList(n1)
    while x.next != None:
        print(x.val)
        x = x.next
    print(x.val)