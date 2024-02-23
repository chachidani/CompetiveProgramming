# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        def cou(node):
            if not node:
                return 0 
            return max(1+cou(node.left),1+cou(node.right))
        return cou(root)


        