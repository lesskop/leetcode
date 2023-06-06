class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # # Time complexity: O(n * m); Space complexity: O(1)
        #
        # for i in range(len(nums1)):
        #     nums2_index = nums2.index(nums1[i])
        #     found_greater = False
        #
        #     for j in range(nums2_index + 1, len(nums2)):
        #         if nums2[j] > nums1[i]:
        #             nums1[i] = nums2[j]
        #             found_greater = True
        #             break
        #
        #     if not found_greater:
        #         nums1[i] = -1
        #
        # return nums1

        # Stack-based approach
        # Time complexity: O(n * m); Space complexity: O(n)

        stack = [nums2[0]]
        next_greater = dict()

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                next_greater[stack[-1]] = nums2[i]
                stack.pop()

            stack.append(nums2[i])

        return [next_greater.get(n, -1) for n in nums1]
