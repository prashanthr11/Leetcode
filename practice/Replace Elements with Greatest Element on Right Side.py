class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        ans = [-1]
        for i in range(len(a) - 1, 0, -1):
            ans.append(max(a[i:]))
        return reversed(ans)
