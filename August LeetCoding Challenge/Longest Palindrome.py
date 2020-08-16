from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s) 
        l = list(d.values())
        if len(l) == 1:
            return l[0]
        ans = 0
        n = list()
        for i in l:
            if i % 2 == 0:
                ans += i
            else:
                n.append(i)
        if len(n):
            ans += max(n)
            n.remove(max(n))
            for i in n:
                if i - 1 > 1:
                    ans += i - 1
        return ans
