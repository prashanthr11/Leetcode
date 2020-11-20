# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        sumi = 0
        def dfs(root):
            nonlocal sumi
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                sumi += abs(left - right)
                return left + right + root.val
            else:
                return 0
        dfs(root)
        return sumi
