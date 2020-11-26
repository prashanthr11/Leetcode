# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def get_elements(root):
            if not root:
                return [[]]
            
            q, ret = [root], list()
            ret.append([root.val])
            l = list()
            q.append(None)
            
            while len(q) > 1:
                front = q.pop(0)
                if front == None:
                    ret.append(l)
                    l = list()
                    q.append(None)
                else:
                    if front.left:
                        q.append(front.left)
                        l.append(front.left.val)
                    else:
                        l.append(None)
                    if front.right:
                        q.append(front.right)
                        l.append(front.right.val)
                    else:
                        l.append(None)
            return ret
        
        if root:
            l = get_elements(root)

            for i in l:
                if i != i[::-1]:
                    return False
        return True
