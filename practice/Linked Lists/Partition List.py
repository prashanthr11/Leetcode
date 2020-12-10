# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        a1, b1 = ListNode(0), ListNode(0)
        
        a, b = a1, b1
        while head:
            if head.val < x:
                a1.next = head
                a1 = a1.next                
            else:
                b1.next = head
                b1 = b1.next
            head = head.next
        
        b1.next = None    
        a1.next = b.next
        return a.next
        
