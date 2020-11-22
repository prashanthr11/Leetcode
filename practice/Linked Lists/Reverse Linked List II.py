# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        l = list()
        tmp = head
        if tmp:
            while tmp:
                l.append(tmp)
                tmp = tmp.next
                
            if m == 1:
                head = l[n - 1]
                l[0].next = l[n - 1].next
                
                for i in range(n - 1, m - 1, -1): 
                    l[i].next = l[i - 1]
                return head
                
            
            l[m - 1].next = l[n - 1].next
            
            # first, last = l[n - 1], l[n - 1].next
            for i in range(n - 1, m - 1, -1): 
                l[i].next = l[i - 1]
            # l[i].next = last
            l[m - 2].next = l[n - 1]
                
        return head
