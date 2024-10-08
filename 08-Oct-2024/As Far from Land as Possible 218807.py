# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if max(max(grid) )== 0  or min(min(grid)) == 1:
            return -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        queue = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 1:
                    queue.append((row,col,0))
                    visited.add((row,col))
        myl = []
        while queue:
            x , y, z = queue.popleft()
            myl.append(z)
            for r,c in directions:
                nr = x + r
                nc = y + c
                if (nr,nc) not in visited and inbound(nr,nc):
                    queue.append((nr,nc,z+1))
                    visited.add((nr,nc))
        return max(myl)


        


        