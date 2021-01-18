"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        # Time: O(N) where N is the total number of nodes
        # Space: O(Log N) Space for Recursion Stack
        
        def helper(root, cnt):
            if not root:
                return
            
            nonlocal ret
            ret = max(ret, cnt)
            
            for i in root.children:
                helper(i, cnt + 1)
                
        ret = 0
        helper(root, 1)
        
        return ret
        
