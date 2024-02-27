# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        c = 0
        def count(root):
            nonlocal c
            if not root:
                return 
            c += 1
        
            count(root.left)
            count(root.right)
            
        
        count(root)
        return c

        