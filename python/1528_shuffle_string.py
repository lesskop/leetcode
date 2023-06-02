class Solution:
    # Hash table solution
    def restoreString(self, s: str, indices: list[int]) -> str:
        ind_to_s = {indices[i]: s[i] for i in range(len(s))}

        result = ''
        for i in range(len(s)):
            result += ind_to_s.get(i)

        return result

    # # In-place shuffling
    # def restoreString(self, s: str, indices: list[int]) -> str:
    #     result = [''] * len(s)
    #
    #     for i, char in enumerate(s):
    #         result[indices[i]] = char
    #
    #     return ''.join(result)
