class Solution:
    def reverseBits(self, n: int) -> int:
        # Time: O(Log N)
        # Space: O(1)

        '''
        def to_binary(n):
            ret = ''

            n = abs(n)
            while n:
                ret += str(n % 2)
                n //= 2

            ret += ('0' * abs(32 - len(ret)))


            return ret

        s = to_binary(n)

        s = s[::-1]

        res = 0
        for i in range(len(s)):
            if int(s[i]):
                res += (2 ** i)

        return res
        
        '''
        
        s = bin(n)[2:][::-1]
        s += ('0' * abs(32 - len(s)))
        
        return int(s, 2)
    
