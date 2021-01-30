# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, a: List[int]) -> TreeNode:
        
        # Time: O(N)
        # Space: O(N)
        
        def build(start, end):
            if start > end:
                return
            mid = (start + end) // 2
            root = TreeNode(a[mid])
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            return root
        
        return build(0, len(a) - 1)
