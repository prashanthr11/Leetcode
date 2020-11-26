# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
    
        q, ret, l = [root], list(), list()
        q.append(None)
        
        while len(q) > 1:
            front = q.pop(0)
            
            if front == None:
                ret.append(l)
                q.append(None)
                l = list()
            else:
                l.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
                    
        if len(l):
            ret.append(l)
            
        return ret
    
    
