from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_middle(self,head):
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeList(self,L1,L2):
        if not L1:
            return L2
        if not L2:
            return L1

        if L1.val < L2.val:
            L1.next = self.mergeList(L1.next, L2)
            return L1
        else:
            L2.next = self.mergeList(L1, L2.next)
            return L2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(next_to_middle)

        return self.mergeList(left,right)


link = 'https://leetcode.com/problems/sort-list/description/'