from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10**7

        if len(dist) >= hour + 1:
            return -1

        while left < right:
            mid = (left + right) // 2

            if sum([ceil(d / mid) for d in dist[:-1]]) + (dist[-1] / mid) <= hour:
                right = mid

            else:
                left = mid + 1

        return left
