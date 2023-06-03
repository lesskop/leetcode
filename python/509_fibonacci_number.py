class Solution:
    # # Trivial recursive solution
    # # Time complexity O(2^n), space complexity O(n)
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #
    #     if n == 1:
    #         return 1
    #
    #     return self.fib(n - 1) + self.fib(n - 2)

    # Iterative solution
    # Time complexity O(n), space complexity O(1)
    def fib(self, n: int) -> int:
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return a
