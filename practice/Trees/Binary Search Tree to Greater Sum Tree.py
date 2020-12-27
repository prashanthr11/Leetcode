# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        # Time: O(N) where N is the number of nodes in the binary tree.
        # Space: O(N)
        
        def assign(root, l):
            nonlocal i
            
            if not root:
                return
            
            assign(root.left, l)
            root.val = l[i]
            i += 1
            assign(root.right, l)
        
        def inorder(root):
            nonlocal l
            
            if not root:
                return
            
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
            
        l = list()
        inorder(root)
        l = l[::-1]
        
        pre = [0]
        
        for i in l:
            pre.append(pre[-1] + i)
            
        pre = pre[1:][::-1]
        
        i = 0
        assign(root, pre)
        
        return root
