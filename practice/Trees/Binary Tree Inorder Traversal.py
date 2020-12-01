# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            nonlocal ret
            if root:
                left = dfs(root.left)
                ret.append(root.val)
                right = dfs(root.right)
                
            return ret
        
        ret = list()
        return dfs(root)
