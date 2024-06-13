# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        storer = []
        storec = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    storer.append(row)
                    storec.append(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in storer or col in storec:
                    matrix[row][col] = 0
      

    
        return matrix
        