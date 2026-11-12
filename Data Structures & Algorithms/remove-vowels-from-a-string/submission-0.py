class Solution:
    def removeVowels(self, s: str) -> str:
        ret = ""

        vows = ['a', 'e', 'i', 'o', 'u']

        for char in s:
            if char not in vows:
                ret += char

        return ret
