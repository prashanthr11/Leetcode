"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def elements(root):
            ret = list()
            if root:
                q, ret, l = [root], list(), list()
                q.append(None)
                while len(q) > 1:
                    front = q.pop(0)
                    if front == None:
                        ret.append(l)
                        q.append(None)
                        l = list()
                    else:
                        l.append(front)
                        if front.left:
                            q.append(front.left)
                        if front.right:
                            q.append(front.right)
                if len(l):
                    ret.append(l)
            return ret
        
        l = elements(root)
        if len(l):
            for i in l:
                for j in range(len(i) - 1):
                    i[j].next = i[j + 1]

            return l[0][0]
        return root
