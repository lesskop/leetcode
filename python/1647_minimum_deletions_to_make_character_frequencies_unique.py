from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        unique_freq = set()
        deletions = 0

        for freq in Counter(s).values():
            while freq > 0 and freq in unique_freq:
                freq -= 1
                deletions += 1

            unique_freq.add(freq)

        return deletions
