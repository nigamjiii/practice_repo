# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node = ListNode()
        temp = node

        while list1 and list2:
            new_node = ListNode()

            if list1.val < list2.val:
                new_node.val = list1.val
                list1 = list1.next
            else:
                new_node.val = list2.val
                list2 = list2.next

            temp.next = new_node
            temp = temp.next

        while list1:
            new_node = ListNode()

            new_node.val = list1.val
            list1 = list1.next

            temp.next = new_node
            temp = temp.next

        while list2:
            new_node = ListNode()

            new_node.val = list2.val
            list2 = list2.next

            temp.next = new_node
            temp = temp.next

        return node.next
    
link = 'https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150'
