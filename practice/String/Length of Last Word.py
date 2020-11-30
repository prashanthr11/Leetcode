class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret = s.split()
        
        if ret:
            return len(ret[-1])
        return 0
