class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # # Linear search
        # for letter in letters:
        #     if ord(letter) > ord(target):
        #         return letter
        #
        # return letters[0]

        # Binary search
        if ord(target) >= ord(letters[-1]) or ord(target) < ord(letters[0]):
            return letters[0]

        start = 0
        end = len(letters) - 1

        while start <= end:
            mid = (start + end) // 2

            if ord(target) >= ord(letters[mid]):
                start = mid + 1

            else:
                end = mid - 1

        return letters[start]
