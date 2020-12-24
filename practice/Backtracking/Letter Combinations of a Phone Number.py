class Solution:
    def letterCombinations(self, a: str) -> List[str]:

        # Time: O(3^N * 4^N)
        # Space: O(3^N * 4^N)
        
        if not a:
            return []
        
        def solve(a, ret, ln):
            nonlocal l
            if not len(a):
                if len(ret) == ln:
                    l.append(ret)
                return ret
            
            for i in range(len(a)):
                for j in range(len(a[i])):
                    solve(a[i + 1:], ret + a[i][j], ln)
            
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        a = [d[i] for i in a]
        l = list()
        solve(a, '', len(a))
        
        return l
                
