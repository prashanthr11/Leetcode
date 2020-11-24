# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def helper(root):
            q1 = [root]
            ret = list()
            q2 = list()
            
            while len(q1) or len(q2):
                
                l1 = list()
                
                while len(q1):
                    front = q1.pop(0)
                    l1.append(front.val)
                    if front.left:
                        q2.append(front.left)
                    if front.right:
                        q2.append(front.right)
                
                l2 = list()

                while len(q2):
                    front = q2.pop(0)
                    l2.append(front.val)
                    if front.left:
                        q1.append(front.left)
                    if front.right:
                        q1.append(front.right)
                ret.append(l1)
                ret.append(l2)

            return ret
        
        def even(l):
            if len(l):
                if l[0] % 2 == 0 or l[-1] % 2 == 0:
                    return False

            for i in range(1, len(l)):
                if l[i] % 2 == 0 or l[i] <= l[i - 1]:
                    return False

            return True

        def odd(l):
            if len(l):
                if l[0] % 2 == 1 or l[-1] % 2 == 1:
                    return False

            for i in range(1, len(l)):
                if l[i] % 2 == 1 or l[i] >= l[i - 1]:
                    return False
            
            return True
            
        l = helper(root)

        for i in range(len(l)):
            if i % 2:
                if not odd(l[i]):
                    return False
            else:
                if not even(l[i]):
                    return False
        return True
