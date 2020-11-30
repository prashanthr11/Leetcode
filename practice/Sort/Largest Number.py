class Largest_Number(str):
    def __lt__(a, b):
        return a + b > b + a


class Solution:
    def largestNumber(self, a: List[int]) -> str:
        a = ''.join(sorted(list(map(str, a)), key = Largest_Number))
        return a if int(a) else '0'
