from itertools import groupby


class Solution:
    def compress(self, chars: list[str]) -> int:
        result = []

        for key, group in groupby(chars):
            count = len(list(group))

            result.append(key)

            if count > 1:
                result += str(count)

        chars[:] = result
