# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        ans = ListNode()
        current = ans
        car = 0

        while l1 or l2 or car:
            c1 = l1.val if l1 else 0
            c2 = l2.val if l2 else 0

            s = c1 + c2 + car

            current.next = ListNode(s % 10)
            car = s // 10
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans.next

link = 'https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150'