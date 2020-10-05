class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        def helper(a):
            a = str(a)
            sumi = 0
            for i in a:
                sumi += int(i) ** 2
            return sumi
        while n > 1:
            st.add(n)
            n = helper(n)
            if n in st:
                return False
        if n == 1:
            return True
        return False
        
