class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = right = 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
