# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hash_map = {}
        n = len(inorder)
        for i in range(n):
            hash_map[inorder[i]] = i

        def build(post_st, post_end, in_st, in_end):
            if post_st > post_end or in_st > in_end:
                return None

            selfNode = TreeNode(postorder[post_end])
            rootIndex = hash_map[postorder[post_end]]
            left_size = rootIndex - in_st

            selfNode.left = build(
                post_st, post_st + left_size - 1, in_st, rootIndex - 1
            )
            selfNode.right = build(
                post_st + left_size, post_end - 1, rootIndex + 1, in_end
            )

            return selfNode

        return build(0, n - 1, 0, n - 1)
    
link = 'https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150'
