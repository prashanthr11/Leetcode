# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def elements(root):
            q, ret = list([root]), list()
            while len(q):
                front = q.pop(0)
                ret.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            return ret
        
        l = elements(root)
        l.sort()

        ret = TreeNode(l[0])
        tmp = ret
        
        for i in l[1:]:
            ret.right = TreeNode(i)
            ret = ret.right
        return tmp
