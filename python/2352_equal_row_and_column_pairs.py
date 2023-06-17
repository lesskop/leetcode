from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_counter = Counter(tuple(row) for row in grid)

        columns = [tuple(col) for col in zip(*grid)]

        return sum(row_counter[columns[col]] for col in range(len(grid)))
