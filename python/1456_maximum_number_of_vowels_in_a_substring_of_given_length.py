class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = 'aeiou'

        sub = s[:k]
        sub_vowels = sum(1 for char in sub if char in VOWELS)
        max_vowels = sub_vowels

        for i in range(k, len(s)):
            if s[i - k] in VOWELS:
                sub_vowels -= 1

            if s[i] in VOWELS:
                sub_vowels += 1

            max_vowels = max(max_vowels, sub_vowels)

        return max_vowels
