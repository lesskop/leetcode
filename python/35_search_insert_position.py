class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            if target < min(nums):
                return 0
            elif target > max(nums):
                return len(nums)
            else:
                nums.append(target)
                return sorted(nums).index(target)
