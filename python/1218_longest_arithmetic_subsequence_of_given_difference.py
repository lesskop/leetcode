from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)

        for n in arr:
            dp[n] = dp[n - difference] + 1

        return max(dp.values())
