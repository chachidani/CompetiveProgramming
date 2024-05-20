# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == [[1]]:
            return 0
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0 for _ in range(n)]for i in range(m)]
        dp[m-1][n-1] = 1
        def inbound(row,col):
            return 0 <= row < m and 0 <= col < n and obstacleGrid[row][col] != 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if inbound(i,j):
                    x = dp[i][j+1] if inbound(i,j+1) else 0  
                    y =  dp[i+1][j] if inbound(i+1,j) else 0 
                    dp[i][j] += x+y
        
        return dp[0][0]
        