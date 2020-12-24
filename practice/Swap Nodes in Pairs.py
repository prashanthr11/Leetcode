# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l = list()
        tmp = head
        while head:
            l.append(head)
            head = head.next
        if len(l) > 1:
            r1, r2 = l[1::2] + [None], l[::2] + [None]

            head = r1[0]
            for i in range(len(r1) - 1):
                r1[i].next = r2[i]
                if r1[i + 1]:
                    r2[i].next = r1[i + 1]
                else:
                    r2[i].next = r2[i + 1]

            return head
        return tmp
