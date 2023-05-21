class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # # My dumb and non-Pythonic solution
        # if not strs or not any(word for word in strs):
        #     return ''
        #
        # for i in range(min(len(x) for x in strs)):
        #     prefixes = set([word[:i + 1] for word in strs])
        #     if len(prefixes) > 1:
        #         return '' if i == 0 else strs[0][:i]
        #
        # return strs[0][:min(len(x) for x in strs)]

        # Elegant solution
        if not strs:
            return ''

        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]

        return shortest


# Test cases
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
print(sol.longestCommonPrefix(["a"]))
print(sol.longestCommonPrefix(["", ""]))
print(sol.longestCommonPrefix(["", "b"]))
