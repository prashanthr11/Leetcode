# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, x: int) -> bool:
        
        # Time: O(N)
        # Space: O(Log N) Size of the recursion stack
        
        def preorder(root, x, sumi):
            if not root:
                return
            
            if root.left is None and root.right is None:
                sumi += root.val
                if x == sumi:
                    nonlocal flag
                    flag = True
                    return
                
            if root.left:
                preorder(root.left, x, sumi + root.val)
            if root.right:
                preorder(root.right, x, sumi + root.val)
            
        flag = False
        preorder(root, x, 0)
        
        return flag
