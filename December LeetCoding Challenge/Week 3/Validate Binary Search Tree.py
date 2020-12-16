# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isbst(root, mini, maxi):
            if not root:
                return True
            
            if root.val <= mini or root.val >= maxi:
                return False
            
            lft = isbst(root.left, mini, root.val)
            rt = isbst(root.right, root.val, maxi)
            
            return True if lft and rt else False
        
        return isbst(root, -2 ** 32, 2 ** 32)
