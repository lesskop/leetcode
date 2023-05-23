class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

        result = ''
        for key in reversed(int_to_roman.keys()):
            if num // key > 0:
                result += int_to_roman[key] * (num // key)
                num %= key

        return result
