class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        # Time: O(N)
        # Space: O(1) As the returned list doesn't taken into the account.
        
        ret = list()
        highest, lowest = len(s), 0
        
        for i in s:
            if i == 'I':
                ret.append(lowest)
                lowest += 1
            else:
                ret.append(highest)
                highest -= 1
            
        ret.append(highest) # As highest or lowest becomes equal.
            
        return ret
