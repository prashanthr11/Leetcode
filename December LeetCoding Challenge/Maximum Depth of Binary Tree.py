# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return 1 + max(left, right)
        return 0
    
    
        '''
        
        def height(root, cnt):
            if not root:
                return cnt
            left = height(root.left, cnt + 1)
            right = height(root.right, cnt + 1)
            return max(left, right)
        return height(root, 0)
        
        '''
