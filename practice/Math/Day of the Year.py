from calendar import isleap

class Solution:
    def dayOfYear(self, a: str) -> int:
        
        a = a.split('-')
        d = {'01' : 31, '03': 31, '05': 31, '07': 31, '08': 31, '10': 31, '12': 31,'04': 30, '06': 30, '09': 30, '11': 30, '02':28}
        
        if isleap(int(a[0])):
            d['02'] += 1
            
        ret = 0
        for i in range(1, int(a[1])):
            if i < 10:
                tmp = '0' + str(i)
                ret += d[tmp]
            else:
                ret += d[str(i)]
            
        return ret + int(a[2])
        
