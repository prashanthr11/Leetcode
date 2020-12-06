class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if n > 0:
            l = list()
            
            for i in range(1, 1 + int(sqrt(n))):
                if not n % i:
                    l.append(i)
                    if i * i != n:
                        l.append(n // i)
                    
            l.sort()
            return l[k - 1] if len(l) >= k else -1
