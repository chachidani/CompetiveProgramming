# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        myGraph = defaultdict(list)
        for row in range(len(graph)):
            myGraph[row] = graph[row]
        
        
        visited = [0 for i in range(len(myGraph))]
        
        def dfs(node,visited):
            print(visited)
            if visited[node] == 0:
                visited[node] = 1
            for nighbour in myGraph[node]:
                if visited[nighbour] == 0 :
                    visited[nighbour] = visited[node] * -1
                    if not dfs(nighbour, visited):
                        return False
                elif visited[nighbour] == visited[node]:
                    return False
                
            return True
        for i in myGraph:
            if visited[i] == 0:
                if not dfs(i,visited):
                    return False
        return True

        

        