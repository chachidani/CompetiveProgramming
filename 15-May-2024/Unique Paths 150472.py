# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(tuple)
        
        
        def end(row,col):
            return row == m-1 and col == n-1
        direction = [(0,1),(1,0)]
        def inbound(row,col):
            return 0 <= row < m and 0 <= col < n
        def dp(row,col):
            if not inbound(row,col):
                return 0

            if end(row,col):
                return 1
            
            if (row,col) not in  memo:
                memo[(row,col)] = dp(row,col+1)+dp(row+1,col)
            return memo[(row,col)]
                
             
        return dp(0,0)
