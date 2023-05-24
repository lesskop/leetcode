class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set()
        max_len = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                char_set.remove(s[left])
                left += 1

        return max_len

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#
#         sub = s[0]
#         sub_len = 1
#         lens = []
#
#         for i in range(1, len(s)):
#             if s[i] not in sub:
#                 sub += s[i]
#                 sub_len += 1
#             else:
#                 lens.append(sub_len)
#                 sub = s[i]
#                 sub_len = 1
#
#         lens.append(sub_len)
#         return max(lens)
