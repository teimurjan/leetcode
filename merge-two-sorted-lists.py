from __future__ import annotations
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pivot = ListNode(-1)

        prev = pivot
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next, l1 = l1, l1.next
            else:
                prev.next, l2 = l2, l2.next

            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return pivot.next


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        expected = ListNode(1)
        expected.next = ListNode(1)
        expected.next.next = ListNode(2)
        expected.next.next.next = ListNode(3)
        expected.next.next.next.next = ListNode(4)
        expected.next.next.next.next.next = ListNode(4)

        actual = s.mergeTwoLists(l1, l2)
        while actual.next:
            self.assertEqual(actual.val, expected.val)

            actual, expected = actual.next, expected.next


if __name__ == "__main__":
    unittest.main()
