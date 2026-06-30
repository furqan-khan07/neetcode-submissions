class Solution:
    def scoreOfString(self, s: str) -> int:

        score = 0
        indx = 0

        while indx != len(s) - 1:

            score += abs(ord(s[indx]) - ord(s[indx+1]))
            indx += 1

        return score
        