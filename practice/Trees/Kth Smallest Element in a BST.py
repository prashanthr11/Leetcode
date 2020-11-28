# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(root):
            if root:
                q, ret = [root], list([root.val])
                q.append(None)
                while len(q) > 1:
                    front = q.pop(0)
                    if front == None:
                        q.append(None)
                    else:
                        if front.left:
                            q.append(front.left)
                            ret.append(front.left.val)
                        if front.right:
                            q.append(front.right)
                            ret.append(front.right.val)
                return ret
            return []
    
        l = helper(root)
        l.sort()
        return l[k - 1]
