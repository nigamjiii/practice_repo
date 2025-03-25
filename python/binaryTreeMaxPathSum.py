# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def sum(node):
            if node is None:
                return 0

            left_gain = max(sum(node.left),0)
            right_gain = max(sum(node.right), 0)

            # To calculate if max sum lies in this part of tree
            current_path_sum = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_path_sum)

            # max Value which it can contribute to upwards
            return node.val + max(left_gain, right_gain)

        sum(root)
        
        return self.max_sum 
    
link = 'https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150'