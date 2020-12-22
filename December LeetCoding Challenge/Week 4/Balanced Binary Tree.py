# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # Time: O(N) where N is the number of nodes in the given Binary Tree
        # Space: O(1)
        
        def solve(root, cnt):
            nonlocal flag
            if not root:
                return cnt
            lft = solve(root.left, cnt + 1)
            rt = solve(root.right, cnt + 1)
            
            if abs(lft - rt) > 1:
                flag = False
            
            return max(lft, rt)
        
        flag = True
        solve(root, -1)
        
        return flag
