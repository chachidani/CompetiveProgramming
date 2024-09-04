# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def solve(root,curmax,curmin):
            if not root:
                return curmax - curmin
            maxx = max(curmax , root.val)
            minn = min(curmin , root.val)

            left = solve(root.left , maxx , minn)
            right = solve(root.right , maxx , minn)
            return max(left,right)
            
        return solve(root,root.val,root.val)


            
        
        