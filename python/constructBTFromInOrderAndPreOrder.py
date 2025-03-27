# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = {}
        n = len(inorder)
        for i in range(n):
            hash_map[inorder[i]] = i

        def build(pre,l_ind, r_ind):
            if l_ind > r_ind:
                return None

            selfNode = TreeNode(preorder[pre])
            rootIndex = hash_map[preorder[pre]]
            left_size = rootIndex - l_ind # left subtree size

            selfNode.left = build(pre + 1, l_ind, rootIndex - 1)
            selfNode.right = build(pre + left_size + 1, rootIndex + 1, r_ind)

            return selfNode

        return build(0, 0, n - 1)
    
link = 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan-v2&envId=top-interview-150'
