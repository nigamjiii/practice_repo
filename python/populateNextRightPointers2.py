

# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            prev = None

            for _ in range(level_size):
                curr = q.popleft()

                if prev:
                    prev.next = curr

                prev = curr

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

        return root

            
link = 'https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/?envType=study-plan-v2&envId=top-interview-150'
                
        