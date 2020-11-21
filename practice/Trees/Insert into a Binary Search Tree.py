# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
        '''
        def add(root, val):
            if root:
                if root.val > val:
                    if root.left:                    
                        add(root.left, val)
                    else:
                        root.left = TreeNode(val)
                elif root.val < val:
                    if root.right:
                        add(root.right, val)
                    else:
                        root.right = TreeNode(val)
        if root:
            tmp = root
            add(root, val)
            return tmp
        else:
            return TreeNode(val)'''
