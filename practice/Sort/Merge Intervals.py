class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        
        # Time: O(N LogN)
        # Space: O(1) excluding returning the result
        
        ret = list()
        
        a.sort()
        mini, maxi = a[0][0], a[0][1]
        
        for i in range(1, len(a)):
            if maxi >= a[i][0]:
                maxi = max(a[i][1], maxi)
            else:
                ret.append([mini, maxi])
                mini, maxi = a[i][0], a[i][1]
                
        ret.append([mini, maxi])
        return ret
