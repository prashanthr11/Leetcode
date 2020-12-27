class Solution:
    def distanceBetweenBusStops(self, l: List[int], x: int, y: int) -> int:
        
        # Time: O(N) --> All the elements are visited once.
        # Space: O(1)
        
        ln = len(l)
        ans = cnt = 0
        
        a, b = min(x, y), max(x, y)
        for i in range(a, b):
            ans += l[i]
        
        for i in range(b, ln + a):
            cnt += l[i % ln]
        
        return min(ans, cnt)
