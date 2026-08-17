class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        if t == s or t in s:
            return 0

        sindx = 0
        tindx = 0
        lent = len(t)

        while sindx < len(s) and tindx < lent:

            if t[tindx] == s[sindx]:
                sindx += 1
                tindx += 1

            else:
                sindx += 1

        return lent - tindx



















        