class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # x = nums[:n]
        # y = nums[n:]
        #
        # for i in range(n):
        #     nums[i * 2] = x[i]
        #     nums[i * 2 + 1] = y[i]
        #
        # return nums
        #
        # # Using zip() method
        # return [val for pair in zip(x, y) for val in pair]

        # One-liner
        return [val for pair in zip(nums[:n], nums[n:]) for val in pair]
