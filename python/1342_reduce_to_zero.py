class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            steps += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

        return steps

        # # Bit manipulation
        # if num == 0:
        #     return 0
        # return num.bit_length() - 1 + num.bit_count()
