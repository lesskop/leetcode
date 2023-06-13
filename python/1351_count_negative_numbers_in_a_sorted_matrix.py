class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        # # Trivial solution
        # result = 0
        #
        # for _, row in enumerate(grid):
        #     for _, num in enumerate(row):
        #         if num < 0:
        #             result += 1
        #
        # return result

        # # Modified solution
        # result = 0
        #
        # for _, row in enumerate(grid[::-1]):
        #     for _, num in enumerate(row[::-1]):
        #         if num >= 0:
        #             break
        #
        #         result += 1
        #
        # return result

        # # One-liner
        # return sum(num < 0 for row in grid for num in row)

        # Binary search
        def count_negatives_in_row(row: list[int]) -> int:
            start, end = 0, len(row) - 1

            while start <= end:
                mid = (start + end) // 2

                if row[mid] < 0:
                    end = mid - 1

                else:
                    start = mid + 1

            return len(row) - start

        return sum(count_negatives_in_row(row) for row in grid)
