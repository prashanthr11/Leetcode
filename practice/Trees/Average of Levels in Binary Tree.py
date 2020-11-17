# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root:
            res = list()
            q1, q2 = list(), list()
            q1.append(root)
            
            while len(q1) or len(q2):
                top_level = list()
                while len(q1):
                    front = q1.pop(0)
                    top_level.append(front.val)
                    
                    if front.left:
                        q2.append(front.left)
                        
                    if front.right:
                        q2.append(front.right)
                        
                bottom_level = list()
                while len(q2):
                    front = q2.pop(0)
                    bottom_level.append(front.val)
                    
                    if front.left:
                        q1.append(front.left)
                        
                    if front.right:
                        q1.append(front.right)
                        
                if len(top_level):
                    res.append(sum(top_level) / len(top_level))
                if len(bottom_level):
                    res.append(sum(bottom_level) / len(bottom_level))
            return res
