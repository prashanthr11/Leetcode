class Solution:
    def fourSumCount(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        
        l1, l2 = list(), list()
        
        for i in a:
            for j in b:
                l1.append(i + j)
                
        for i in c:
            for j in d:
                l2.append(i + j)
        
        d = collections.Counter(l1)
        
        cnt = 0
        for i in l2:
            if d[-i] > 0:
                cnt += d[-i]
                
        return cnt
