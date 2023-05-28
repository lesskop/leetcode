# from collections import Counter
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # for key, count in Counter(nums).items():
        #     if count == 1:
        #         return key

        # Beautiful
        return reduce(xor, nums)
