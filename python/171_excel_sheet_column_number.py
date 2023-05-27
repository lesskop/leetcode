class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letter_to_num = {chr(65 + i): i + 1 for i in range(26)}
        nums = [letter_to_num.get(letter) for letter in columnTitle[::-1]]

        col = 0
        for i, num in enumerate(nums):
            col += 26 ** i * num

        # for i in range(len(nums)):
        #     col += 26 ** i * nums[i]

        return col
