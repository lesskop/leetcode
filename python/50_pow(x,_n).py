class Solution:
    def binary_exponentiation(self, x: float, n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        if n < 0:
            return 1 / self.binary_exponentiation(x, abs(n))

        if n % 2 == 1:
            return x * self.binary_exponentiation(x * x, (n - 1) // 2)
        else:
            return self.binary_exponentiation(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binary_exponentiation(x, n)
