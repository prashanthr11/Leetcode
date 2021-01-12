class Solution:
    def allPathsSourceTarget(self, a: List[List[int]]) -> List[List[int]]:

        # Time: O(2 ^ N) If all the nodes are connected i.e., for every i < j, there an outgoing path from i to j.
        # Space: O(1)

        ret, ln = list(), len(a)

        def solve(s, t, l, path):
            if s == t:
                nonlocal ret
                ret.append(path + [s])
                return

            for i in l:
                solve(i, t, a[i], path + [s])


        solve(0, ln - 1, a[0], [])

        return ret