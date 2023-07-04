class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_map = {char: 0 for char in s}

        for char in s:

            if hash_map[char] != 0:
                return char

            hash_map[char] += 1
