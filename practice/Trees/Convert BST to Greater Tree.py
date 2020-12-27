# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        # Time: O(N) where N is the number of the nodes in the binary tree.
        # Space: O(N)
        
        def inorder(root):
            nonlocal sumi
            
            if not root:
                return None
            
            inorder(root.right)
            root.val += sumi
            sumi = root.val
            inorder(root.left)
            
        sumi = 0
        inorder(root)
        
        return root
