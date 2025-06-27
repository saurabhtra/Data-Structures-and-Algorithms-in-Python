# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def inorder(root,ans):
            if root==None:
                return []
            return [inorder(root.left,ans)]+[root.val]+[inorder(root.right,ans)]
        def postorder(root,ans):
            if root==None:
                return []
            return [inorder(root.left,ans)]+[inorder(root.right,ans)]+[root.val]
        in1=inorder(p,[])
        in2=inorder(q,[])
        ps1=postorder(p,[])
        ps2=postorder(q,[])
        if in1 ==in2 and ps1==ps2:
            return True
        else:
            return False   

        