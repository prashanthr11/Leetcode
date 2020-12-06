class Solution:
    def interpret(self, a: str) -> str:
        a = a.replace('()', 'o').replace('(al)','al')
        
        return a
