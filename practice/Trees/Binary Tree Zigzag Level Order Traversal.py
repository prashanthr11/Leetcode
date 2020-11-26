# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(root):
            if root:
                q, ret, l = [root], list(), list()
                q.append(None)

                while len(q) > 1:
                    front = q.pop(0)
                    if front == None:
                        q.append(None)
                        ret.append(l)
                        l = list()
                    else:
                        l.append(front.val)
                        if front.left:
                            q.append(front.left)
                        if front.right:
                            q.append(front.right)
                if len(l):
                    ret.append(l)

                tmp = len(ret)
                for i in range(1, tmp, 2):
                    ret[i] = ret[i][::-1]

                return ret
            return root
        return helper(root)
