# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def depth(root,c,ans):
            
            if not root:
                return ans
            if not root.left and not root.right:
                return min(c,ans)
        
            left = depth(root.left,c+1,ans)
            right = depth(root.right,c+1,ans)
            return min(left,right)
            
        return depth(root,1,10**5)
        
       
        