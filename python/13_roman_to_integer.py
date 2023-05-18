class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        prev_value = 0

        for i in range(len(s) - 1, -1, -1):
            current_value = roman_to_int[s[i]]

            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result

    # # Funny solution
    # def romanToInt(self, s: str) -> int:
    #     roman_to_int = {
    #         'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    #     }
    #
    #     s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX')
    #     s = s.replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')
    #
    #     return sum(roman_to_int[char] for char in s)
    