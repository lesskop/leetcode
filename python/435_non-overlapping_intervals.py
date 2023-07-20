class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        result = 0
        temp_end = float('-inf')

        for start, end in intervals:
            if start >= temp_end:
                temp_end = end
            else:
                result += 1

        return result
