# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        x_left = self.lowestCommonAncestor(root.left, p, q)
        x_right = self.lowestCommonAncestor(root.right, p, q)
        
        if x_left and x_right:
            return root
        
        return x_left if x_left else x_right
