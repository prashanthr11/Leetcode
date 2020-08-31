class Solution:
    def containsPattern(self, a: List[int], m: int, k: int) -> bool:
        if k == 1 and len(a) > 1:
            return True
        a = ''.join(str(i) for i in a)
        
        for i in range(len(a) - m + 1):
            if a[i:i + m] * k in a:
                return True
        return False
      
      #   Naive approach
#         if len(a) >= m * k:
#             tq = 0
#             while tq < len(a):
#                 x = []
#                 for i in range(tq,len(a),m):
#                     st = a[i:i+m]
#                     x.append(st)
#                 # print(x)
#                 cnt = 1
#                 for i in range(1, len(x)):
#                     if x[i] == x[i - 1]:
#                         cnt += 1
#                     else:
#                         cnt = 1
#                     if cnt >= k:
#                         return True
#                 tq += 1

#         else:
#             return False
        
