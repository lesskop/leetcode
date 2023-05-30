class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        max_row = [max(row) for row in grid]
        max_col = [max(col) for col in zip(*grid)]

        max_increase = 0

        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                max_increase += min(max_row[r], max_col[c]) - value

        return max_increase
