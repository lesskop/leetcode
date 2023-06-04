class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # # Trivial nested loop solution
        #
        # # Quadratic time complexity: O(n^2); Constant space complexity: O(1)
        #
        # for _, row in enumerate(matrix):
        #     for _, val in enumerate(row):
        #         if val == target:
        #             return True
        #
        # return False

        # Since the matrix is sorted from left to right and from top to bottom,
        # we can go from the upper right corner and compare the values to the target

        # Linear time complexity: O(n + m); Constant space complexity: O(1)

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False
