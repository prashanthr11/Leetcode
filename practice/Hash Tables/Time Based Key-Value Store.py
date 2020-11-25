from collections import defaultdict as dt
from bisect import bisect_left

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dt(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        tmp = self.d[key]
        if tmp:
            i = bisect_left(tmp, (timestamp, chr(127)))
            return tmp[i - 1][1] if i else ''
        
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
