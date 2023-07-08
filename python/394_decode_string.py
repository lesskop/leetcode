class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        result = ''

        for char in s:

            if char.isalpha():
                result += char

            elif char.isdigit():
                num = num * 10 + int(char)

            elif char == '[':
                stack.append(result)
                stack.append(num)
                result = ''
                num = 0

            elif char == ']':
                n = stack.pop()
                prev_str = stack.pop()
                result = prev_str + n * result

        return result
