# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        # Time: O(N)
        # Space: O(N)
        
        l = list()
        tmp = head
        
        while tmp:
            l.append(ListNode(tmp.val))
            tmp = tmp.next
            
        l[k - 1], l[-k] = l[-k], l[k - 1]
        
        head = l[0]
        for i in range(1, len(l)):
            l[i - 1].next = l[i]
            
        return head
