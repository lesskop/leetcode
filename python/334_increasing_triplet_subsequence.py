class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first_min = second_min = float('inf')

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False

        # # Works only for adjacent increasing triplet subsequence
        # for i in range(1, len(nums) - 1):
        #     if nums[i - 1] < nums[i] < nums[i + 1]:
        #         return True
        #
        # return False
