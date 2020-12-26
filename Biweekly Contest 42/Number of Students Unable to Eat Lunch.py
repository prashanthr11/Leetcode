class Solution:
    def countStudents(self, a: List[int], b: List[int]) -> int:
        
        while len(a) and len(b):
            
            for i in b:
                if i in a:
                    flag = True
                    break
                else:
                    return len(a)
            
            if not flag:
                return len(a)
            
            if a[0] == b[0]:
                a.pop(0)
                b.pop(0)
            else:
                tmp = a.pop(0)
                a.append(tmp)
                
        return len(a)
