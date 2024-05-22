# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(i,j):
            if i >= len(triangle):
                return 0
            if (i,j) not in memo:
                one = dp(i+1,j)+(triangle[i][j] if len(triangle[i]) > j else float('inf'))
                two = dp(i+1,j+1)+(triangle[i][j+1] if len(triangle[i]) > j+1 else float('inf'))
                memo[(i,j)] = min(one,two)
            return memo[(i,j)]
        return dp(0,0)
        

            
            

        
        
        