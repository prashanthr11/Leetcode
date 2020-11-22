# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        ret = dummy
        
        while True:
            
            if not l1:
                ret.next = l2
                break
                
            if not l2:
                ret.next = l1
                break
            
            if l1.val < l2.val:
                ret.next = l1
                l1 = l1.next
            else:
                ret.next = l2
                l2 = l2.next
                
            ret = ret.next
            
        return dummy.next
