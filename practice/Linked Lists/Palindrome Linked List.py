# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        '''
        # Time: O(N)
        # Space: O(N)
        
        l = list()
        
        while head:
            l.append(head.val)
            head = head.next
            
        return l == l[::-1]
        '''
        
        # Time: O(N)
        # Space: O(1)
        
        def reverse(head):
            prev = None
            tmp = head
            
            while tmp:
                tmp = tmp.next
                head.next = prev
                prev = head
                head = tmp
            
            return prev
            
        if not head or not head.next:
            return True
        
        if not head.next.next:
            return head.next.val == head.val
        
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        tmp = slow.next if fast else slow
        
        tmp = reverse(tmp)
        
        while tmp:
            if head.val != tmp.val:
                return False
            
            tmp = tmp.next
            head = head.next
        
        return True
