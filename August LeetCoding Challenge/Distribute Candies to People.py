class Solution:
    def distributeCandies(self, a: int, b: int) -> List[int]:
        ans = [0 for i in range(b)]
        i = 0
        
        while i + 1 < a:
            ans[i % b] += i + 1
            a -= i + 1
            i += 1
            
        ans[i % b] += a
        
        return ans
