class Solution:
    def averageWaitingTime(self, a: List[List[int]]) -> float:
        
        # Time: O(N) Where N is the length of the given list.
        # Space: O(1)
        
        ans = time = 0
        
        for k, v in a:
            time = max(time, k) + v
            ans += time - k
            
        
        return ans / len(a)
