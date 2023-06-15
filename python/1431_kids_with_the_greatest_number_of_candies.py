class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        enough = max(candies) - extraCandies
        return [candy >= enough for candy in candies]