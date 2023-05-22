# from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # stack = deque()
        stack = []

        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            else:
                if not stack:
                    return False
                if x == ')' and stack.pop() != '(':
                    return False
                elif x == ']' and stack.pop() != '[':
                    return False
                elif x == '}' and stack.pop() != '{':
                    return False

        return not stack
