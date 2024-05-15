# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))]for i in range(len(grid))]
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0
        
        
        def dfs(visited,row,col):
            nonlocal val
            visited[row][col] = True
            
            for d_r ,d_c in directions:
                new_row = row + d_r
                new_col = col + d_c
                
                if inbound(new_row,new_col) and  not visited[new_row][new_col]:
                    val += grid[new_row][new_col]
                    dfs(visited,new_row,new_col)
                    
        

            return val
            
        value = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0 and not visited[row][col] :
                    val = grid[row][col] 
                    value = max(value,dfs(visited,row, col))
        return value


        