class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        l = [0] + a + [0]
        cnt = 0
        
        for i in range(1, len(l) - 1):
            if l[i] == l[i - 1] == l[i + 1] == 0:
                cnt += 1
                l[i] = 1
        
        return cnt >= n
        
        '''  
        # Naive Solution
        
        def place(l, i):
            ln = len(l)
            if i == 0 and ln == 1:
                return True
            if i == 0:
                return l[1] == 0
            if i < ln - 1:
                return l[i] == l[i - 1] == l[i + 1] == 0
            if i == ln - 1:
                return l[-1] == l[-2] == 0
            
        while n:
            tmp = n
            for i in range(len(a)):
                if not a[i]:
                    if place(a, i):
                        a[i] = 1
                        tmp -= 1
                        break
            if tmp == n:
                break
            n = tmp
            
        return n == 0
        '''
