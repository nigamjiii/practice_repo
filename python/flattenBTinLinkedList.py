from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None

        def rev_pre_order(node):
            nonlocal prev
            if not node:
                return

            rev_pre_order(node.right)
            rev_pre_order(node.left)

            node.right = prev
            node.left = None
            prev = node

        rev_pre_order(root)
        
link = 'https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150'
