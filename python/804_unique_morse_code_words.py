class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                       "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        char_to_code = {chr(i + 97): morse_codes[i] for i in range(26)}

        transformations = set()
        for word in words:
            transformations.add(''.join([char_to_code.get(char) for char in word]))

        return len(transformations)