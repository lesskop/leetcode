# from collections import Counter


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # counter = Counter(nums)
        # values = counter.values()
        # keys = counter.keys()
        #
        # if len(keys) == 1 and list(values)[0] > 1:
        #     return True
        #
        # return False if len(set(values)) == 1 else True

        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)

        return False
