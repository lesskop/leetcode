class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for num in row[::-1]:
                if target == num:
                    return True
                elif target > num:
                    break

        return False
