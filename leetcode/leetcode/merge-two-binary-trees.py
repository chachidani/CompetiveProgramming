# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        newNode = TreeNode()
        def merge(root1,root2,newNode):
            if root1 and root2:
                newNode.val = root1.val + root2.val
                newNode.left = merge(root1.left,root2.left,TreeNode())
                newNode.right = merge(root1.right,root2.right,TreeNode()) 
                return newNode 
            elif root1:
                newNode = root1
                return newNode 
            elif  root2:
                newNode = root2 
                return newNode 
            else:
                return None
        return merge(root1,root2,newNode)
        



        