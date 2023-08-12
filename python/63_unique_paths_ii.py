class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * cols
        dp[-1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if grid[r][c]:  # or grid[r][c] == 1 (obstacle)
                    dp[c] = 0
                elif c + 1 < cols:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]
