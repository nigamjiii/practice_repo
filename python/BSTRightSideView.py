from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    
    
link = 'https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150'

        