from collections import Counter as di

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def helper(self, root, idx, l):
        if not root:
            return l
        l.append(idx)
        lft = self.helper(root.left, 2 * idx + 1, l)
        rt = self.helper(root.right, 2 * idx + 2, l)
        return l

    def __init__(self, root: TreeNode):
        l = self.helper(root, 0, [])
        self.d = di(l)

    def find(self, target: int) -> bool:
        return self.d[target]


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
