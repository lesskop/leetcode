class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = sum(nums[1:])

        for i in range(len(nums)):
            if left == right:
                return i

            left += nums[i]

            if i < len(nums) - 1:
                right -= nums[i + 1]

        return -1