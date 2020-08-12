class Solution:
    def hIndex(self, a: List[int]) -> int:
        if len(a) == 0:
            return 0
        else:
            a.sort(reverse=True)
            ans=0
            for i in range(len(a)):
                if i + 1 <= a[i]:
                    ans = i + 1
                else:
                    return ans
            return ans
