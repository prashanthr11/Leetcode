# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time: O(N)
    # Space: O(N)
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def solve(root, maxi, mini):
            if not root:
                return maxi - mini
            
            maxi = max(maxi, root.val)
            mini = min(mini, root.val)
            lft = solve(root.left, maxi, mini)
            rt = solve(root.right, maxi, mini)
            
            return max(lft, rt)
        
        return solve(root, 0, float('inf'))
