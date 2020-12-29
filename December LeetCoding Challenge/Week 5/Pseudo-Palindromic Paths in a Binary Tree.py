from collections import Counter as di

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        # Time: O(N * K) where N is the number of the nodes and K is the leaf nodes count
        # Space: O(N)
        
        def canFormPalindrome(s):
            d = di(s)
            cnt = 0
            
            for i in d.values():
                cnt += (i % 2)
                
            return cnt <= 1
        
        def preorder(root):
            nonlocal l, ans
            
            if not root:
                return
            
            l.append(root.val)
            if root.left or root.right:
                preorder(root.left)
                preorder(root.right)
                l.pop()
            else:
                if canFormPalindrome(l):
                    ans += 1
                l.pop()
                
        l, ans = list(), 0
        preorder(root)
        
        return ans
