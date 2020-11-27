# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def helper(root):
            if root:
                q, ret, l = [root], list([root.val]), list()
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
                return ret
            return []
        l = helper(root)
        return sum(l[-1])
