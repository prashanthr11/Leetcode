# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, l: ListNode, a: int, b: int, q: ListNode) -> ListNode:
        x, tmp = l, l
        while x:
            if x.val == b:
                last = x.next
                break
            x = x.next
        
        while tmp.next:
            if tmp.next.val == a:
                tmp.next = q
                
            tmp = tmp.next
        tmp.next = last
        return l
