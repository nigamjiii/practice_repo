# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        if not head.next:
            return False

        slow = head.next
        fast = head.next.next

        while slow != None and fast != None:
            if slow.next == fast.next:
                return True

            slow = slow.next
            fast = fast.next.next if fast.next != None else None

        return False

link = 'https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150'