from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = defaultdict(int)

        for char in magazine:
            char_count[char] += 1

        for char in ransomNote:
            if char_count[char] == 0:
                return False
            else:
                char_count[char] -= 1

        return True
