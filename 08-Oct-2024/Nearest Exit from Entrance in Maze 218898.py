# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(row,col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == '.'


        queue = deque()
        visited = set()
        queue.append((entrance[0] , entrance[1] , 0))
        visited.add((entrance[0] , entrance[1] ))
        ans = []
        while queue:
            x,y,z = queue.popleft()
            if (x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[0]) - 1) and [x, y] != entrance:
                return z
           
            for r,c in directions:
                nr = x + r
                nc = y + c
                if inbound(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,z+1))
                
                
                

        return -1 
