class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])-1
        row = 0
        while row < len(matrix):
            if matrix[row][right] < target:
                row += 1
            elif matrix[row][right] >= target:
                while left <= right:
                    mid = (left+right)//2
                    if matrix[row][mid] > target:
                        right = mid-1
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    elif matrix[row][mid] == target:
                        return True
                break
        return False
            



        