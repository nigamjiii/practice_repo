# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        curr = head
        prev = None

        while curr:
            temp = curr.next # find next
            curr.next = prev # assign curr
            prev = curr # move previous
            curr = temp # move curr

        return prev


link = 'https://leetcode.com/problems/reverse-linked-list/'