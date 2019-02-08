import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        head = tail = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        if not l1 or not l2:
            tail.next = l1 or l2

        return head.next


def intergerListToListNode(numbers: list) -> ListNode:
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node: ListNode) -> str:
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class TestCases(object):
    solution = Solution()

    @pytest.mark.parametrize('l1, l2, result', [
        ([1, 2, 4], [1, 3, 4], '[1, 1, 2, 3, 4, 4]'),
        ([1, 2, 4, 4], [1, 3, 4], '[1, 1, 2, 3, 4, 4, 4]'),
        ([], [], '[]'),
        ([], [1, 3, 4], '[1, 3, 4]'),
        ([1, 3, 4], [], '[1, 3, 4]'),
        ([2], [1], '[1, 2]'),
    ])
    def test_mergeTwoLists(self, l1, l2, result):
        l1_LN = intergerListToListNode(l1)
        l2_LN = intergerListToListNode(l2)
        assert listNodeToString(self.solution.mergeTwoLists(l1_LN, l2_LN)) == result
