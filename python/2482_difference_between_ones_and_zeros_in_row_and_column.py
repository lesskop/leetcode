class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diff = [[0] * n for _ in range(m)]

        ones_row = [sum(row) for row in grid]
        zeros_row = [row.count(0) for row in grid]

        reversed_grid = [list(row) for row in zip(*grid)]

        ones_col = [sum(row) for row in reversed_grid]
        zeros_col = [row.count(0) for row in reversed_grid]

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        return diff
