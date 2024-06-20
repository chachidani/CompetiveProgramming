# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m
        dp = [[-1 for i in range(m)]for j in range(n)]
        dp[-1] = matrix[-1]
        for i in range(n):
            dp[i][-1] = int(matrix[i][-1])
        
        l = 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if int(matrix[i][j]) == 0:
                    dp[i][j] = 0
                    continue
                x = int(dp[i][j+1]) if inbound(i,j+1) else 0
                y =  int(dp[i+1][j]) if inbound(i+1,j) else 0
                z =  int(dp[i+1][j+1]) if inbound(i+1,j+1) else 0
                dp[i][j] = min(x,y,z) + int(matrix[i][j])
                l = max(dp[i][j],l)
        

        return l**2
