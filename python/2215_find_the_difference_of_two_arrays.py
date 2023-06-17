class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_distinct, nums2_distinct = set(nums1), set(nums2)

        return [list(nums1_distinct - nums2_distinct), list(nums2_distinct - nums1_distinct)]
