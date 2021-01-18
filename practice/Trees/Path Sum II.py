# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, x: int) -> List[List[int]]:
        
        # Time: O(N)
        # Space: O(Log N) --> Recursion Stack
        
        def helper(root, x, path):
            if not root:
                return
            
            if root.left == None and root.right == None:
                x -= root.val
                if x == 0:
                    nonlocal l
                    l.append(path + [root.val])
                    
                return
            
            if root.left:
                helper(root.left, x - root.val, path + [root.val])
            
            if root.right:
                helper(root.right, x - root.val, path + [root.val])
                
        l = list()
        
        helper(root, x, [])
        
        return l
