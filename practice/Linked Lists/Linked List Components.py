# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: ListNode, a: List[int]) -> int:
        
        # Time: O(N + len(a)) N is lenth of the linked list
        # Space: O(len(a))
        
        cnt = 0
        s = set(a)
        
        while head:
            if head.val in s and getattr(head.next, 'val', None) not in s:
                cnt += 1
            head = head.next
        
        return cnt
                
