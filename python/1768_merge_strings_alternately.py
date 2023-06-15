from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # if len(word1) > len(word2):
        #     size = len(word2)
        #     result_end = word1[size:]
        #
        # else:
        #     size = len(word1)
        #     result_end = word2[size:]
        #
        # return ''.join(word1[i] + word2[i] for i in range(size)) + result_end

        # Using `zip_longest()` method. None is replaced by an empty string with the parameter `fillvalue=''`
        return ''.join(char for pair in zip_longest(word1, word2, fillvalue='') for char in pair)
