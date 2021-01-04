class Solution:
    def checkArithmeticSubarrays(self, a: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        # Time: O(L * N logN) where L is the Queries and N is Length of the subarray (Length of a - R + l)
        # Space: O(1)
        
        def check(l):
            if len(l) > 1:
                l.sort()
                ans = l[1] - l[0]
                
                for i in range(2, len(l)):
                    if ans != l[i] - l[i - 1]:
                        return False
                
            return True
        
        ret = list()
        
        for i in range(len(l)):
            ret.append(check(a[l[i]:r[i] + 1]))
        
        return ret
