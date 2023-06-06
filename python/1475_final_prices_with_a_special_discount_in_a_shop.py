class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # # Trivial nested loop solution
        # # Quadratic time complexity: O(n^2); Constant space complexity: O(1)
        #
        # size = len(prices)
        #
        # for i in range(size):
        #     for j in range(i + 1, size):
        #         if prices[j] <= prices[i]:
        #             prices[i] -= prices[j]
        #             break
        #
        # return prices

        # Stack-based approach
        # Linear time complexity: O(n); Linear space complexity: O(n)

        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices
