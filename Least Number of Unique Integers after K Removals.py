class Solution:
    from collections import Counter
    def findLeastNumOfUniqueInts(self, a: List[int], k: int) -> int:
        d = Counter(a)
        l = list(d.values())
        l.sort(reverse = True)
        t = len(l) - 1 
        for i in range(k):
            if l[t] > 0:
                l[t] -= 1
            else:
                l.pop()
                t = len(l) - 1
                l[t] -= 1
        l = [i for i in l if i > 0]
        return len(l)
                
