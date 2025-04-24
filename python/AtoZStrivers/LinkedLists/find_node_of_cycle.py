# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Brute Force
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_set = set()

        temp = head
        node = None

        while temp:
            if temp in hash_set:
                return temp
            else:
                hash_set.add(temp)

            temp = temp.next

            if temp == None:
                return node
   
# Optimal         
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None

            
link = 'https://leetcode.com/problems/linked-list-cycle-ii/'
