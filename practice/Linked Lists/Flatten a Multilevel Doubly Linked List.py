"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    # Time: O(N)
    # Space: O(N)
    
    def flatten(self, head: 'Node') -> 'Node':
        def solve(tmp):
            nonlocal l
            while tmp:
                l.append(tmp)
                if tmp.child:
                    solve(tmp.child)
                tmp = tmp.next
        
        if not head:
            return head
        
        l = list()
        tmp = head
        while tmp:
            l.append(tmp)
            if tmp.child:
                solve(tmp.child)
            tmp = tmp.next
        
        head = l[0]

        for i in range(len(l)):
            l[i].child = None
            if i == 0:
                l[i].prev = None
                if len(l) == 1:
                    l[i].next = None
                else:
                    l[i].next = l[i + 1]
            elif i == len(l) - 1:
                l[i].next = None
                l[i].prev = l[i - 1]
            else:
                l[i].next = l[i + 1]
                l[i].prev = l[i - 1]
            

        return head
