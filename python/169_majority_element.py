from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = Counter(nums)
        max_count = max(counter.values())
        for num, count in counter.items():
            if count == max_count:
                return num
