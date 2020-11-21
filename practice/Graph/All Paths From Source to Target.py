from collections import defaultdict as dt

class Solution:
    def allPathsSourceTarget(self, a: List[List[int]]) -> List[List[int]]:
        def dfs(root, l, lst):
            if len(d[root]):
                l.append(root)
                for i in d[root]:
                    dfs(i, l, lst)
                l.pop()
            else:
                if root == lst:
                    nonlocal ans
                    ans.append(l + [root])
                elif lst in l:
                    ans.append(l[:l.index(lst) + 1])
                return
            
             
        d = dt(list)
        for i in range(len(a)):
            d[i] = a[i]
        ans, l = list(), list()
        lst = len(a) - 1
        dfs(0, l, lst)
        return ans
