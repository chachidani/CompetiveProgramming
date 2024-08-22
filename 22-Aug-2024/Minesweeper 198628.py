# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        directions = [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,0),(-1,1),(-1,-1)] 

        def inbound(row,col):
            return 0 <= row < n and 0 <= col < m
        digit = defaultdict(int)
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'M':
                    
                    for dr,dc in directions:
                        new_r = row + dr
                        new_c = col + dc
                        if inbound(new_r,new_c) and  board[new_r][new_c] == 'E' :
                            digit[(new_r,new_c)] += 1

        
        def dfs(row,col):
            visited.add((row,col))
           
            if digit[(row,col)]:
                board[row][col] = f'{digit[(row,col)]}'
                return 
            else:
                board[row][col] = 'B'
         
            for dr,dc in directions:
                new_r = row + dr
                new_c = col + dc
    
                if inbound(new_r,new_c) and board[new_r][new_c] == 'E' and (new_r,new_c) not in visited:
                   dfs(new_r,new_c)
                
        r,c = click
        if board[r][c] == 'X' or board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        elif board[r][c] == 'E':
            visited = set()
            dfs(r,c)
            return board
        else:
            return board




                

        



        