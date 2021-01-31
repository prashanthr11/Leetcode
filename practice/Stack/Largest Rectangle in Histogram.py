class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        
        # Time: O(N)
        # Space: O(N)
        
        l = list()
        maxi, ret = 0, 0
        
        for i, v in enumerate(a):
            # if not l or a[l[-1]] <= v:
            #     l.append(i)
            # else:
            while len(l) and a[l[-1]] > v:
                tmp = l.pop()
                if len(l):
                    maxi = max(maxi, a[tmp] * (i - l[-1] - 1))
                else:
                    maxi = max(maxi, a[tmp] * i)
            l.append(i)
        
        x = len(a)
        while len(l):
            tmp = l.pop()
            if len(l):
                maxi = max(maxi, a[tmp] * (x - l[-1] - 1))
            else:
                maxi = max(maxi, a[tmp] * x)

        return maxi
