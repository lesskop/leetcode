class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [map(lambda x: abs(x - 1), reversed(row)) for row in image]
