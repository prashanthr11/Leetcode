class Solution:
    def countPairs(self, a: List[int]) -> int:
        
        # Time: O(21 * N) --> O(N) where N is the length of the list
        # Space: O(N)
        
        cnt = 0
        d = Counter()
        
        for i in a:
            for j in range(22):
                cnt += d[(1 << j) - i]
            d[i] += 1
            
        return cnt % (10**9 + 7)
