from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        prev = None
        curr = root

        ans = float("inf")

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev is not None:
               ans = min(ans, abs(curr.val - prev)) 

            prev = curr.val

            curr = curr.right

        return ans
    
link = 'https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150'
