# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def traverse(node):
            if node is None:
                return None

            if node == p:
                return p

            if node == q:
                return q

            left = traverse(node.left)
            right = traverse(node.right)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
            else:
                return None

        return traverse(root)
    
    
link = 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-interview-150'
