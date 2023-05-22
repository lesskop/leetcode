from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        evens = [num for num in nums if num % 2 == 0]
        if not evens:
            return -1

        counter = Counter(evens)
        max_count = max(counter.values())
        tie = []
        for num, count in counter.items():
            if count == max_count:
                tie.append(num)

        return min(tie)
