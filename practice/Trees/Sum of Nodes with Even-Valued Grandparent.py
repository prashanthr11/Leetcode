# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root):
        
        # Time: O(N)
        # Space: O(Log N)
        
        def solve(root, parent, grandparent):
            if not root:
                return
            
            root.parent = parent
            root.grandparent = grandparent
            
            if root.grandparent and root.grandparent.val % 2 == 0:
                self.ret += root.val
            
            solve(root.left, root, root.parent)
            solve(root.right, root, root.parent)
        
        self.ret = 0        
        solve(root, parent = None, grandparent = None)
        
        return self.ret
