# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        # Time: O(N)
        # Space: O(N)

        def inorder(root):
            nonlocal l
            if not root:
                return
            
            inorder(root.left)
            l.add(root.val)
            inorder(root.right)
            
        l = set()
        inorder(root)

        
        for i in l:
            if k - i != i and k - i in l:
                return True
            
        return False
