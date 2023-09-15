class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = left = right = 0

        while right < len(nums) - 1:
            longest_jump = 0

            for i in range(left, right + 1):
                longest_jump = max(longest_jump, i + nums[i])

            left = right + 1
            right = longest_jump
            min_jumps += 1

        return min_jumps