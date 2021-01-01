# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        # Method 1 (Heap)
        
        # Time: O(N Log K) --> O(N)
        # Space: O(N)
        
        def dfs(root):
            nonlocal l
            
            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)
            l.append(root.val)
            
            return l
        
        l = list()
        dfs(root)

        heapq.heapify(l)
        
        return heapq.nsmallest(k, l)[-1]
        '''
        
        # Method 2 (Inorder)
        
        # Time: O(N)
        # Space: O(N)
        
        def inorder(root):
            nonlocal l
            if not root:
                return 
            
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
            
            return
        
        l = list()
        inorder(root)
        
        return l[k - 1]
        
        '''
        
        # Time: O(N Log N)
        # Space: O(N)
        
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
        '''
