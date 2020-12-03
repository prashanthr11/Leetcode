# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import choice

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        current = self.head
        scope = 1
        chosen_value = 0
        
        while current:
            if random.random() < 1 / scope:
                chosen_value = current.val
            current = current.next
            scope += 1

        return chosen_value

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
