# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inde = [0 for i in range(n)]
        for i,j in edges:
            graph[j].append(i)
            graph[i].append(j)
            inde[i] += 1
            inde[j] += 1

        visited = set()
       
        queue = deque()
        for i in range(len(inde)):
            if inde[i] == 1:
                queue.append(i)
                visited.add(i)

        ans = [0]
        while queue:
        
            ans = queue.copy()
            for _ in range(len(queue)):
                node = queue.popleft()

                for i in graph[node]:
                    
                    if i not in visited:
                       
                        inde[i] -= 1
                        if inde[i] == 1:
                            queue.append(i)
                            visited.add(i)

            
        
       
        return ans