from collections import Counter as di

class Solution:
    def topKFrequent(self, a: List[int], b: int) -> List[int]:
        d = di(a)
        ans = list()
        
        for i in d.most_common(b):
            ans.append(i[0])
        
        return ans
        
