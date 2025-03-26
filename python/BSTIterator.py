from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.head = Node(0)
        self.curr = self.head

        def in_order_ll(node):
            if not node:
                return

            in_order_ll(node.left)
            self.curr.next = Node(node.val)
            self.curr = self.curr.next
            in_order_ll(node.right)

        in_order_ll(root)
        self.curr = self.head
            
    def next(self) -> int:
        if self.curr.next is not None:
            self.curr = self.curr.next
            return self.curr.value
 
    def hasNext(self) -> bool:
        if self.curr and self.curr.next is not None:
            return True
        return False
        

link = 'https://leetcode.com/problems/binary-search-tree-iterator/?envType=study-plan-v2&envId=top-interview-150'