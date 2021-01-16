from collections import Counter as di

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        # Time: O(N)
        # Space: O(N)
        
        ret = 0
        d = di()
        
        def solve(root, flag, cnt):
            nonlocal ret, d
            if not root:
                ret = max(ret, cnt)
                return ret
            
            if d[root]:
                return d[root]
            
            if flag == 'left':
                d[root] = max(d[root], solve(root.left, 'right', cnt + 1))
            else:
                d[root] = max(d[root], solve(root.right, 'left', cnt + 1))
            return d[root]
        
        def preorder(root):
            if not root:
                return 
            
            if root.left:
                solve(root.left, 'right', 0)
            
            if root.right:
                solve(root.right, 'left', 0)
                
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        
        return ret
