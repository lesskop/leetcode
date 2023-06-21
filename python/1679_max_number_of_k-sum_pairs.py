class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        result = 0
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                result += 1

                left += 1
                right -= 1

            elif current_sum < k:
                left += 1

            else:
                right -= 1

        return result
