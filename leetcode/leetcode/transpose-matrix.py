class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_col = []
        new_row = []
        new_matrix = [[0]*len(matrix)]*len(matrix[0])
       
        for col in range(len(matrix[0])):

            for row in range(len(matrix)):
                new_col.append(matrix[row][col])
                
            new_row.append(new_col)
            new_col = []

        return new_row
       

        