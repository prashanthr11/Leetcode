# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        ln = 0
        d = {}
        while temp:
            d[ln] = temp
            ln += 1
            temp = temp.next
        
        if ln - n == 0:
            return head.next
        x = d[ln - n - 1]
        x.next = x.next.next
        return head
