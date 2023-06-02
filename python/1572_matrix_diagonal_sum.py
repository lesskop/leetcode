class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        result = 0
        size = len(mat)

        for i, row in enumerate(mat):
            result += row[i]
            if i != size - i - 1:
                result += row[size - i - 1]

        return result
