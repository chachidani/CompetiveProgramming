class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = matrix.copy()
        matrix.clear()
        new_col = []
        
        for col in range(len(new_matrix[0])):
            for row in range(len(new_matrix)-1,-1,-1):
                new_col.append(new_matrix[row][col])
            matrix.append(new_col)
            new_col = []
        
    
    


        