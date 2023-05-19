class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # result = [nums[0]]
        # current_sum = nums[0]
        #
        # try:
        #     for i, num in enumerate(nums):
        #         current_sum += nums[i + 1]
        #         result.append(current_sum)
        # except IndexError:
        #     return result

        # List comprehension solution
        return [sum(nums[:i + 1]) for i, _ in enumerate(nums)]
