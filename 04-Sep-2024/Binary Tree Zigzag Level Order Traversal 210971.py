# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = []
        level = 0
        current = []
        queue = deque([(root,0)])

        while queue:

            node,node_level = queue.popleft()
            if not node:
                continue

            if node_level != level:
                levels.append(current)
                current = []
                level += 1
            
            current.append(node.val)
            queue.append((node.left , level + 1))
            queue.append((node.right , level + 1))
        if current:
            levels.append(current)
        
        for i in range(1,len(levels),2):
            levels[i] = levels[i][::-1]


        return levels


        
        