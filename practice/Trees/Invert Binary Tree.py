# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # Time: O(N) where N is the nodes in the binary tree
        # Space: O(1)
        
        if not root:
            return None
        
        lt = self.invertTree(root.left)
        rt = self.invertTree(root.right)
        
        root.left = rt
        root.right = lt
        
        return root
