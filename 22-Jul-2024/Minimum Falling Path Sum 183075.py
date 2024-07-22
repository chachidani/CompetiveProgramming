# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
     
        def inbound(row,col):
            return 0 <= row < r and 0 <= col < c
        
        
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                x = matrix[i+1][j+1] if inbound(i+1,j+1) else float('inf')
                y = matrix[i+1][j]  if inbound(i+1,j) else float('inf')
                z = matrix[i+1][j-1] if inbound(i+1,j-1) else float('inf')
                l = min(x,y,z) 
                matrix[i][j] += (l if l != float('inf') else 0) 
        

        return min(matrix[0])
