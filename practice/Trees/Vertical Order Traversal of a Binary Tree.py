# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        # Time: O(N log N)
        # Space: O(N)
        
        def bfs(root):      # O(N) N: Number of nodes in the Binary Tree
            q, l = list(), list()
            if root:
                q = [root]
                while len(q):
                    front = q.pop(0)
                    l.append(front.val)
                    if front.left:
                        q.append(front.left)
                    if front.right:
                        q.append(front.right)
            return l
        
        def helper(root, ht, cnt):  # O(N) N: Number of nodes in the Binary Tree
            nonlocal d
            if root:
                d[ht].append((cnt, root.val))
                helper(root.left, ht - 1, cnt + 1)
                helper(root.right, ht + 1, cnt + 1)
            return d

            
        d = collections.defaultdict(list)
        d = helper(root, 0, 0)
        l = bfs(root)
        ret = list()
        
        for k, v in sorted(d.items()):      # O(N log N) As sorting of the nodes inorder to get according to their arrivals
            tmp = sorted(v)
            ret.append([i[1] for i in tmp])
            
        return ret
