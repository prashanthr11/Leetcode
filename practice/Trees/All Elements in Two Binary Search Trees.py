# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, a: TreeNode, b: TreeNode) -> List[int]:
        
        # Time: O(N LogN)
        # Space: O(N)
        
        def preorder(root):
            nonlocal l
            
            if not root:
                return 
            
            l.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        l = list()
        preorder(a)
        preorder(b)
        
        return sorted(l)
