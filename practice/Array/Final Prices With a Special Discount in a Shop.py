class Solution:
    def finalPrices(self, a: List[int]) -> List[int]:
        ret = list()
        
        for i in range(len(a)):
            flag = True
            for j in range(i + 1, len(a)):
                if a[i] >= a[j]:
                    ret.append(a[i] - a[j])
                    flag = False
                    break
            if flag:
                ret.append(a[i])
                
        return ret
