# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in flights:
            graph[v].append((u,w))
        dp = [[float('inf') for i in range(n)]for j in range(k+2)]
        dp[0][src] = 0


        for row in range(1 , k+2):
            dp[row][src] = 0
            for col in range(n):
                for u,w in graph[col]:
                    dp[row][col] =  min(dp[row-1][u] + w  , dp[row][col])
                

        print(dp)
        return dp[k+1][dst] if dp[k+1][dst]  != float('inf') else -1
        