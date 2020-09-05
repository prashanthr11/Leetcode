# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head:
            t = head
            t2 = head
            while t:
                if t.next and t:
                    t = t.next.next
                else:
                    return t2
                t2 = t2.next
        return t2
        
