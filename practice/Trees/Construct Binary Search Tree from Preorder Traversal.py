# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        
        # Time: O(N Log N)
        # Space: O(N)
        
        def solve(root, l):
            if not root:
                if len(l):
                    root = TreeNode(l[0])
                else:
                    return
            
            idx = bisect.bisect(l, l.pop(0))
            root.left = solve(root.left, l[:idx])
            root.right = solve(root.right, l[idx:])
            return root
        
        root = solve(None, preorder)
        return root
        
