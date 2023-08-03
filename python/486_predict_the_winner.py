class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True

        def max_diff(left: int, right: int):
            if left == right:
                return nums[left]

            left_score = nums[left] - max_diff(left + 1, right)
            right_score = nums[right] - max_diff(left, right - 1)

            return max(left_score, right_score)

        return max_diff(0, len(nums) - 1) >= 0
