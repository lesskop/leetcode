# from string import ascii_lowercase, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # for char in s:
        #     if (char not in ascii_lowercase) and (char not in digits):
        #         s = s.replace(char, '')
        # return s == s[::-1]

        # New isalnum() method explored
        s = [char for char in s.lower() if char.isalnum()]
        return s == s[::-1]
