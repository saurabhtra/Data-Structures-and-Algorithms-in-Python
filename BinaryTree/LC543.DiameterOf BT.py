# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root.left==None and root.right==None:
            return 0
        self.diameter=0
        def solver(root):
            if root==None:
                return 0
            lh=solver(root.left)
            rh=solver(root.right)
            self.diameter =max(self.diameter,lh+rh)
            return 1+max(lh,rh)
        solver(root)
        return self.diameter
        