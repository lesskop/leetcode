class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        for i, n in enumerate(nums):

            if ranges and ranges[-1][-1] == n - 1:
                ranges[-1][-1] = n
            else:
                ranges.append([n, n])

        return [f'{x}->{y}' if x != y else str(x) for x, y in ranges]
