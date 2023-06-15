class Solution:
    def reverseVowels(self, s: str) -> str:
        # somehow `set(vowels)` works a bit slower than the simple string `vowels`
        vowels = 'aeiouAEIOU'

        # # Comprehensions
        # s_vowels = [char for char in s if char in vowels]
        #
        # return ''.join(char if char not in vowels else s_vowels.pop() for char in s)

        # Two pointers, the best runtime and memory usage.
        data = list(s)
        left, right = 0, len(data) - 1

        while left < right:
            if data[left] in vowels and data[right] in vowels:
                data[left], data[right] = data[right], data[left]

                left += 1
                right -= 1

            if data[left] not in vowels:
                left += 1

            if data[right] not in vowels:
                right -= 1

        return ''.join(data)
