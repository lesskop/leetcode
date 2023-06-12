class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1

        while start <= n:
            mid = (start + n) // 2

            g = guess(mid)

            if g == 0:
                return mid

            elif g == 1:
                start = mid + 1

            else:
                n = mid - 1
