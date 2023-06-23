from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Using `math.gcd()`
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]

        # # Dumb
        # result = temp = ''
        #
        # for i in range(min(len(str1), len(str2))):
        #     temp += str1[i]
        #
        #     if not any(x for x in str1.split(temp)) and not any(x for x in str2.split(temp)):
        #         result = temp
        #
        # return result
