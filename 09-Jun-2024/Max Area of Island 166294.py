# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))]for i in range(len(grid))]
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

        def dfs(row,col,visited):
            
            visited[row][col] = True
            value = 0
            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc

                if inbound(new_row,new_col) and not visited[new_row][new_col]:
                    value +=  dfs(new_row,new_col,visited)
                    


            
            return value + 1
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and not visited[row][col]:
                   
                    ans = max(ans,dfs(row,col,visited))
        return ans

        





        