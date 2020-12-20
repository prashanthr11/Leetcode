class Solution:
    def maximumUniqueSubarray(self, a: List[int]) -> int:
        
        # Time: O(N) where N is length of a
        # Space: O(N)
        
        i, ret, ans, j = 0, 0, 0, 0
        s = set()
        
        for i in range(len(a)):
            while a[i] in s:       # O(1)
                ans -= a[j]
                s.remove(a[j])
                j += 1
            s.add(a[i])
            ans += a[i]
            ret = max(ret, ans)
            
        return max(ans, ret)
