class Solution:
    
    # Time: O(N ^ 2)
    # Space: O(1)
    
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
        '''
        
        # Time: O(N)
        # Space: O(1)
        
        l = [0] * 3
        
        for i in a:
            l[i] += 1
            
        j = 0
        for i, x in enumerate(l):
            cnt = x
            while cnt:
                a[j] = i
                cnt -= 1
                j += 1
