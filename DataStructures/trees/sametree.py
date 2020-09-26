"""

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, p,q):
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val!=q.val:
            return False

        return p.val==q.val and self.helper(p.left, q.left) and self.helper(p.right, q.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return self.helper(p,q)
        
