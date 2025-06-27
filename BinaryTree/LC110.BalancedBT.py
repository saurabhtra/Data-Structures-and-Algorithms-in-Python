# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def solver(root):
            if root==None:
                return 0
            lh=solver(root.left)
            if lh==-1:
                return -1
            rh=solver(root.right)
            if rh==-1:
                return -1
            if abs(lh -rh) >1:
                return -1
            
            return 1+max(lh,rh)
        x=solver(root)
        return x != -1
        