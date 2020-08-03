class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = ""
        for i in s:
            if i.isupper():
                ret += i.lower()
            elif i.islower():
                ret += i
            elif i.isdigit():
                ret += i
        return ret == ret[::-1]
        
