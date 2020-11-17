# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root:
            q, l = [root], list()
            
            while len(q):
                front = q.pop()
                l.append(front.val)
                
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            
            ans = 987987979798
            
            l.sort()
            for i in range(1, len(l)):
                ans = min(ans, abs(l[i - 1] - l[i]))
            return ans
