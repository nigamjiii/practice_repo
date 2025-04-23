# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Basic approach
class Solution:
    def deleteNode(self, node):
        curr = node
        prev = None

        while curr.next:
            temp = curr.next

            temp.val, curr.val = curr.val, temp.val

            prev = curr
            curr = temp

        prev.next = None
        
# Smart approach according to question
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
link = 'https://leetcode.com/problems/delete-node-in-a-linked-list/description/'