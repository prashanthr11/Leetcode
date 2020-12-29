# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        # Tiem: O(N)
        # Space: O(N)
        
        def elements(root):
            ret = list()
            if not root:
                return ret
                
            q, l = [root], list()
            ret = list([root.val])
            q.append(None)
            
            while len(q) > 1:
                front = q.pop(0)
                if front == None:
                    ret.append(l)
                    l = list()
                    q.append(None)
                    
                else:
                    l.append(front)
                    if front.left:
                        q.append(front.left)
                    if front.right:
                        q.append(front.right)
                
            if len(l):
                ret.append(l)
                
            return ret[-1]
        
        def lca(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            
            lft = lca(root.left, p, q)
            rt = lca(root.right, p, q)
            
            if lft and rt:
                return root
            
            return lft if lft else rt
        
        l = elements(root)

        return lca(root, l[0].val, l[-1].val)
