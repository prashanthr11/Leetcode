# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time: O(N)
    # Space: O(N)
    
    def balanceBST(self, root):
        def inorder(root):
            nonlocal l
            if not root:
                return
                
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
            
        def buildbst(start, end):
            
            if start > end:
                return
            mid = (end + start) // 2
            root = TreeNode(l[mid])
            root.left = buildbst(start, mid - 1)
            root.right = buildbst(mid + 1, end)
            return root
            
        l = list()
        inorder(root)
        return buildbst(0, len(l) - 1)
