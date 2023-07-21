class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        lens = [1] * n
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lens[j] + 1 > lens[i]:
                        lens[i] = lens[j] + 1
                        counts[i] = 0

                    if lens[j] + 1 == lens[i]:
                        counts[i] += counts[j]

        max_len = max(lens)

        return sum(counts[i] for i in range(n) if lens[i] == max_len)
