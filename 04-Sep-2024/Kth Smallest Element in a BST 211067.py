# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(root):
            if not root:
                return 
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        ans.sort()
        return ans[k-1]

        