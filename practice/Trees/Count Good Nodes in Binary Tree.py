# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder(root, maxi):
            if not root:
                return
            
            if maxi <= root.val:
                maxi = root.val
                self.cnt += 1
                

            preorder(root.left, maxi)
            preorder(root.right, maxi)
            
            
        self.cnt = 0
        preorder(root, root.val)
        
        return self.cnt
