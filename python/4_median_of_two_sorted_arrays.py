class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Trivial solution: merge 2 lists and sort the result. Then find the center element
        nums = sorted(nums1 + nums2)

        n = len(nums)
        center = n // 2

        if n % 2 == 0:
            return (nums[center] + nums[center - 1]) / 2
        else:
            return nums[center]
