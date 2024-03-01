# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def find(root):
            nonlocal store
            if not root:
                return 
            store[root.val] = store.get(root.val , 0)+1
            find(root.left)
            find(root.right)
        store = {}
        find(root)
        ans = []
        l = max(store.values())
        for i,val in store.items():
            if val == l:
                ans.append(i)

        return ans
        