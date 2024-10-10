# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        print(graph)
        distances = {node+1: float('inf') for node in range(n)}
        distances[k] = 0
        received = set()
        visited = set([(0,k)])
        heap = [(0,k)]
        print(heap)

        while heap:
            cost , node = heappop(heap)
            for neigh , i in graph[node]:
                minim = min(distances[neigh] ,cost+i )
                if (minim , neigh ) not  in visited:
                    visited.add((minim , neigh))
                    heappush(heap , (minim ,neigh ))
                    distances[neigh] = minim
            print(heap)
        print(distances)
        ans = 0
        for i,j in distances.items():
            ans = max(j , ans)




        return ans if ans != float('inf') else -1


        