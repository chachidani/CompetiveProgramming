# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

#Python3 Code
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def postOrder(root):
            if not root:
                return
            for node in root.children:
                postOrder(node)
                res.append(node.val)
        
        if not root:
            return []
        postOrder(root)
        res.append(root.val)
        return res