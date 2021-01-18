from collections import Counter as di

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        # Time: O(N)
        # Space: O(N)
        
        def postorder(root):
            nonlocal d
            
            if not root:
                return False
            
            lft = postorder(root.left)
            rt = postorder(root.right)

            d[root.val + lft + rt] += 1
            return root.val + lft + rt
        
        d = di()        
        postorder(root)
        
        ans = list()
        if len(d):
            maxi = max(d.values())
            for k, v in d.items():
                if v == maxi:
                    ans.append(k)
                    
        return ans
