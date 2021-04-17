class Solution:
    def getMaximumXor(self, nums: List[int], maxi: int) -> List[int]:
        def solve(n):
            tmp = (2**maxi) - 1
            tmp = bin(tmp)[2:]
            b = bin(n)[2:]
            if len(b) < len(tmp):
                b = '0' * (len(tmp) - len(b)) + b
            
            ans = ''
            for i in range(len(tmp)):
                if tmp[i] == '1':
                    if b[i] == '1':
                        ans += '0'
                    else:
                        ans += '1'
                else:
                    if b[i] == '0':
                        ans += '1'
                    else:
                        ans += '0'
                        
            return int(ans, 2)
        

        pref = [0]
        for i in nums:
            pref.append(pref[-1] ^ i)
            
        ret = list()
        lst = solve(pref[-1])
        ans = pref[-1] ^ lst
        ret.append(lst)
        for i in range(len(pref) - 2, 0, -1):
            tmp = ans ^ pref[i]
            ret.append(tmp)
            
        return ret
