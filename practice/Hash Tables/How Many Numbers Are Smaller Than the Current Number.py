class Solution:
    def smallerNumbersThanCurrent(self, a: List[int]) -> List[int]:
        ret = list()
        for i in a:
            cnt = 0
            for j in a:
                if i > j:
                    cnt += 1
            ret.append(cnt)
        return ret
        
