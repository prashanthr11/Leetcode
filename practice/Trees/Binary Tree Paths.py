# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        # Time: O(N)
        # Space: O(N)
        
        def preorder(root, x):
            nonlocal l
            if not root:
                return
            
            x += str(root.val) + '->'
            
            if not root.left and not root.right:
                l.append(x[:-2])
                return
                        
            if root.left:
                preorder(root.left, x)
            if root.right:
                preorder(root.right, x)
            return
        
        l = list()
        preorder(root, '')
        
        return l
