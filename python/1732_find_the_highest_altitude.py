class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitudes = [0]

        for i in range(len(gain)):
            altitudes.append(gain[i] + altitudes[i])

        return max(altitudes)
