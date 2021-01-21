class Solution:
    def insert(self, head, j, idx):
        if idx == 0:
            tmp = ListNode(j, head)
            self.head = tmp
            return
        ln = 0
        while head:
            ln += 1
            if ln == idx:
                head.next = ListNode(j, head.next)
                return
            head = head.next
        
        
    def createTargetArray(self, a, ind):
        '''
        # Using Insert Function
        # Time: O(N * N) N for moving the elements to right and it repeats for N times.
        # Space: O(1)
        
        ret = list()
        
        for i, j in enumerate(a):
            ret.insert(ind[i], j)
            
        return ret
        '''
        
        # Using LinkedList
        # Time: O(N * N)
        # Space: O(N) Memory for storing the elemetns in the linkedlist.
        
        self.head = None
        for i, j in enumerate(a):
            self.insert(self.head, j, ind[i])
            
        ret = list()
        while self.head:
            ret.append(self.head.val)
            self.head = self.head.next
            
        return ret
