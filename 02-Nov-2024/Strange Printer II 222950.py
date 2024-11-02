# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        squares = defaultdict(lambda: [float("inf"),0,float("inf"),0])
        n = len(targetGrid)
        m = len(targetGrid[0])
        colors = set()

        for i in range(n):
            for j in range(m):
                color = targetGrid[i][j]
                colors.add(color)
                squares[color][0] = min(squares[color][0],i)
                squares[color][1] = max(squares[color][1],i)
                squares[color][2] = min(squares[color][2],j)
                squares[color][3] = max(squares[color][3],j)


        graph = defaultdict(list)
        indegree = defaultdict(int)

        for node in colors:
            visited = set([node])
            for i in range(squares[node][0], squares[node][1] + 1):
                for j in range(squares[node][2], squares[node][3] + 1):
                    if targetGrid[i][j] not in visited:
                        indegree[targetGrid[i][j]] += 1
                        visited.add(targetGrid[i][j])
                        graph[node].append(targetGrid[i][j])
                        
        
        queue = deque()
        for i in colors:
            if i not in indegree:
                queue.append(i)

        res = 0
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            res += 1
        
        return res == len(colors)