# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []

        for i in range(2,n):
            tempR = []
            for j in range(2,n):
                temp = 0
                for k in range(i-2,i+1):
                    for l in range(j-2,j+1):
                        temp = max(temp,grid[k][l])
                tempR.append(temp)
            res.append(tempR)
        return res



        
        