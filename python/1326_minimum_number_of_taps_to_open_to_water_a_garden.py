class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [n + 2] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])

            for j in range(left, right + 1):
                dp[right] = min(dp[right], dp[j] + 1)

        if dp[n] >= n + 2:
            return -1

        return dp[n]
