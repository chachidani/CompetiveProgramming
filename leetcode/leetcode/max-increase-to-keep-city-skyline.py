class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowmax = [max(row) for row in grid]
        colmax = [max(col) for col in zip(*grid)]

        ans = 0
        for i in range(n):
            for j in range(n):
                minmax = min(rowmax[i], colmax[j])
                if grid[i][j] < minmax:
                    ans += minmax - grid[i][j]

        return ans