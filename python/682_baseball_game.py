class Solution:
    def calPoints(self, operations: list[str]) -> int:
        # For operation "+", there will always be at least two previous scores on the record.
        # For operations "C" and "D", there will always be at least one previous score on the record.
        record = []

        for op in operations:
            try:
                record.append(int(op))
            except ValueError:
                if op == 'C':
                    record.pop()
                elif op == 'D':
                    record.append(record[-1] * 2)
                elif op == '+':
                    record.append(record[-1] + record[-2])

        return sum(record)
