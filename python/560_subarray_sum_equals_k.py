class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = sub_sum = 0
        n = len(nums)
        prefix_sum_count = {0: 1}

        for i in range(n):
            sub_sum += nums[i]
            to_remove = sub_sum - k

            result += prefix_sum_count.get(to_remove, 0)
            prev_count = prefix_sum_count.get(sub_sum, 0)
            prefix_sum_count[sub_sum] = prev_count + 1

        return result
