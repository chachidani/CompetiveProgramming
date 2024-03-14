class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])-1
        rowleft = 0
        rowright = len(matrix)-1
        row = 0
        while rowleft <= rowright:
            mid = (rowleft+rowright)//2
            if matrix[mid][right] < target:
                rowleft = mid+1
            elif matrix[mid][right] >= target and matrix[mid][left] <= target:
                row = mid
                break
            elif matrix[mid][right] > target:
                rowright = mid-1


        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] > target:
                right = mid-1
            elif matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] == target:
                return True
              
        return False
            



        