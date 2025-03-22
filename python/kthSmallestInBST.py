# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Naive Approach: T.C O(n) and S.C O(n+h)
class Solution:
    def in_order_traversal(self, root):
        a = []

        if root is None:
            return a

        a.extend(self.in_order_traversal(root.left))
        a.append(root.val)
        a.extend(self.in_order_traversal(root.right))

        return a

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.in_order_traversal(root)[k-1]
        
# Optimized Approach: T.C O(n) and S.C O(h)       
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        current = root

        while stack or current:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1

            if count == k:
                return current.val

            current = current.right
            
            
link = 'https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150'