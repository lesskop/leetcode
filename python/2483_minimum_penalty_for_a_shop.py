class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # # Time limit exceeded. Time complexity: O(n^2)
        # penalty = len(customers) + 1
        # earliest_hour = int()

        # for hour in range(len(customers) + 1):
        #     right_side = sum([0 if char == 'N' else 1 for char in customers[hour:]])
        #     left_side = sum([0 if char == 'Y' else 1 for char in customers[:hour]])

        #     current_penalty = right_side + left_side

        #     if current_penalty < penalty:
        #         penalty = current_penalty
        #         earliest_hour = hour

        # return earliest_hour

        # Time complexity: O(n)
        penalty = current_penalty = 0
        earliest_hour = int()

        for hour, char in enumerate(customers):
            if char == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1

            if current_penalty < penalty:
                penalty = current_penalty
                earliest_hour = hour + 1

        return earliest_hour
