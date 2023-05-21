class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # result = ''
        # for num in digits:
        #     result += str(num)
        #
        # return [int(num) for num in str(int(result) + 1)]

        # One liner
        return [int(x) for x in str(int(''.join(map(str, digits))) + 1)]
