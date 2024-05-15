# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)

                queue.append(node.left)
            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)

                queue.append(node.right)
        # print(graph)
        visted = set()
        visted.add(target.val)
        ans = deque([target.val])
        c = 0
        while ans:
            if c == k:
                break
            for _ in range(len(ans)):
                popped = ans.popleft()
                
                for nigh in graph[popped]:
                    
                    if nigh not in visted:
                        ans.append(nigh)
                        visted.add(nigh)
            c += 1
        
        
        res = []
        for i in ans:
            res.append(i)
        return res


        

        