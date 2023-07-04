from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0

        for num, count in Counter(nums).items():
            if count == 1:
                result += num

        return result
