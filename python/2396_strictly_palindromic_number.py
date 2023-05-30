class Solution:
    @staticmethod
    def number_to_base(num: int, base: int) -> list[int]:
        if num == 0:
            return [0]

        digits = []

        while num:
            digits.append(int(num % base))
            num //= base

        return digits[::-1]

    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            num_list = self.number_to_base(n, base)
            if num_list != num_list[::-1]:
                return False

        return True
