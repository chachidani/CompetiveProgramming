# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dell(node,el):
            if not node:
                return 
            
            elif node.val > el:
                node.left =  dell(node.left,el)
            elif node.val <el:
                node.right = dell(node.right,el)
            elif node.val == el:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = found(node.right)
                node.val = temp.val
            
                node.right = dell(node.right,temp.val)
            return node
        def found(node):
            cur = node
            while cur.left:
                cur = cur.left
            return cur
        return dell(root,key)

        



       
        
        


        
        