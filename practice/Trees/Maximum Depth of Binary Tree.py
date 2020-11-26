# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(root, cnt):
            if root:
                lft = helper(root.left, cnt + 1)
                rht = helper(root.right, cnt + 1)
                return max(lft, rht)
            else:
                return cnt
        return helper(root, 0)
