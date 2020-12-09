# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: TreeNode):
        def inorder(root):
            nonlocal l
            if root:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
            return l
        
        l = list()
        l = inorder(root)
        self.tmp = TreeNode(-1)
        head = self.tmp
        
        for i in l:
            head.right = TreeNode(i)
            head = head.right
            

    def next(self) -> int:
        if self.tmp.right:
            self.tmp = self.tmp.right
            return self.tmp.val
        
        return -1

    def hasNext(self) -> bool:
        return self.tmp.right


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
