"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
    
        # Time: O(N) where N is the total number of the nodes in the given Tree.
        # Space: O(N)
        
        ret = list()
        if not root:
            return root
        
        q, l = [root], list()
        q.append(None)
        tmp = list()
        
        while len(q) > 1:
            front = q.pop(0)
            if front == None:
                q.append(None)
                l.append(tmp)
                tmp = list()
            else:
                tmp.append(front.val)
                for i in front.children:
                    q.append(i)
        if len(tmp):
            l.append(tmp)
        
        return l
