class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # # Trivial solution using `index()` method
        # try:
        #     return nums.index(target)
        # except ValueError:
        #     if target < min(nums):
        #         return 0
        #     elif target > max(nums):
        #         return len(nums)
        #     else:
        #         nums.append(target)
        #         return sorted(nums).index(target)

        # Binary search solution
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                start = mid + 1

            else:
                end = mid - 1

        return start
