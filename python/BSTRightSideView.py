from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS solution: LEVEL ORDER TRAVERSAL
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                curr = queue.popleft()

                if i == level_size - 1:
                    ans.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return ans
    
# DFS solution: REVERSE PRE ORDER TRAVERSAL    
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []

        def rev_pre_order(node, level):
            if node is None:
                return 

            if level == len(ans):
                ans.append(node.val)

            rev_pre_order(node.right, level + 1)
            rev_pre_order(node.left, level + 1)

        rev_pre_order(root, 0)
        return ans
    
    
link = 'https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150'

        