# from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # num_to_letter = {i + 1: ascii_uppercase[i] for i in range(26)}
        num_to_letter = {i + 1: chr(65 + i) for i in range(26)}

        title = ''
        while columnNumber > 0:
            columnNumber -= 1
            div = columnNumber // 26
            mod = columnNumber % 26
            columnNumber = div
            title = num_to_letter[mod + 1] + title

        return title
