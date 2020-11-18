import bisect

class Solution:
    def nextGreatestLetter(self, a: List[str], t: str) -> str:

        return a[bisect.bisect(a, t) % len(a)]
