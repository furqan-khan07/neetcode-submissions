class Solution:
    def countSubstrings(self, s: str) -> int:

        def ispali(word: str) -> Bool:
            return word == word[::-1]

        count = 0

        substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

        for sub in substrings:
            if ispali(sub):
                count += 1

        return count




        