# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, a):
        
        # Time: O(N ^ 2)
        # Space: O(N) Memory for Recursion stack, when the tree is skewed tree!
        
        def solve(root, l):
            if not root:
                if len(l):
                    root = TreeNode(max(l))
                else:
                    return
            
            idx = l.index(max(l))
            root.left = solve(root.left, l[:idx])
            root.right = solve(root.right, l[idx + 1:])
            return root
        
        root = solve(None, a)
        
        return root
