from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # # Very bad approach, generating all permutations of a string of length `n` has a O(n!) time complexity
        # strings = set(''.join(_) for _ in itertools.permutations(s))

        # for string in strings:
        #     if all(string[i] != string[i + 1] for i in range(len(string) - 1)):
        #         return string

        # return ''

        #######################################################################################################

        # Max heap approach. Time complexity: O(n log n); Space complexity: O(n)

        char_count = Counter(s)

        # The standard Python `heapq` library is used for min heaps, so the character frequency is inverted
        max_heap = [(-cnt, char) for char, cnt in char_count.items()]
        heapq.heapify(max_heap)

        prev = None
        result = ''

        while max_heap or prev:
            if prev and not max_heap:
                return ''
            
            cnt, char = heapq.heappop(max_heap)

            result += char
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt < 0:
                prev = (cnt, char)

        return result