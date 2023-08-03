class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        digit_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i: int, cur_str: str):
            if len(cur_str) == len(digits):
                result.append(cur_str)
                return

            for char in digit_chars[digits[i]]:
                backtrack(i + 1, cur_str + char)

        if digits:
            backtrack(0, '')

        return result
