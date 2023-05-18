class Solution:
    # My implementation with bad runtime
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, num in enumerate(nums):
            for i, n in enumerate(nums):
                if index != i and num + n == target:
                    return [index, i]

    # # Good runtime
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     seen = {}
    #     for i, value in enumerate(nums):
    #         remaining = target - nums[i]
    #
    #         if remaining in seen:
    #             return [i, seen[remaining]]
    #         else:
    #             seen[value] = i
