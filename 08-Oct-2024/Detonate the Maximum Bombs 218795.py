# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombs.sort()
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for  j in range(len(bombs)):
                if i == j:
                    continue
                a,b,c = bombs[i]
                x,y,r = bombs[j]
                d = sqrt((x-a)**2 + (y-b)**2)
                if c >= d:
                    graph[i].append(j)
        
        def solve(node , visited):
              
            
            visited.add(node)
            found = 1
            for neigh in graph[node]:
                if neigh not in visited:
                    found += solve(neigh , visited)
            return found
            

        count = 0
        for i in range(len(bombs)):
            visited = set([])
            m = solve(i ,visited)
            count = max(m , count)


        return count

        