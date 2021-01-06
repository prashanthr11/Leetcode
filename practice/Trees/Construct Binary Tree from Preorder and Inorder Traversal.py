# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> TreeNode:
        
        # Time: O(N)
        # Space: O(N)
        
        def build(root, p, i):
            if not i:
                return root
            
            tmp = p.pop(0)
            idx = i.index(tmp)
            
            if not root:
                root = TreeNode(tmp)
            
            root.left = build(root.left, p, i[:idx])
            root.right = build(root.right, p, i[idx + 1:])
            
            return root
    
        return build(None, p, i)
