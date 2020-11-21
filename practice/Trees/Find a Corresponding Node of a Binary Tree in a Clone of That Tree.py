# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, a: TreeNode, b: TreeNode, t: TreeNode) -> TreeNode:
        if b:
            if b.val == t.val:
                return b
            return self.getTargetCopy(a, b.left, t) or self.getTargetCopy(a, b.right, t)
