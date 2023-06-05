class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # # Trivial nested loop solution. LeetCode time limit exceeded
        # # Quadratic time complexity: O(n^2); Linear space complexity: O(n)
        # result = []
        #
        # for i, day in enumerate(temperatures):
        #     found_higher = False
        #
        #     for j in range(i + 1, len(temperatures)):
        #         if day < temperatures[j]:
        #             result.append(j - i)
        #             found_higher = True
        #             break
        #
        #     if not found_higher:
        #         result.append(0)
        #
        # return result

        # Stack-based approach
        # Linear time complexity: O(n); Linear space complexity: O(n)
        size = len(temperatures)
        stack = []
        result = [0] * size

        for i in range(size):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result
