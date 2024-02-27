# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minn = min(p.val,q.val)
        maxx = max(p.val,q.val)
        def common(minn,maxx,root):
            if not root:
                return 
            if minn <= root.val <= maxx:
                return root
            elif minn > root.val:
                return common(minn,maxx,root.right)
            elif maxx < root.val:
                return common(minn,maxx,root.left)
        return common(minn,maxx,root)


        