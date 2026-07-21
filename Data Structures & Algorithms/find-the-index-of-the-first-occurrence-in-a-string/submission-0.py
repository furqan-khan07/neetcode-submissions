class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        indx = 0

        while indx < len(haystack) - len(needle) + 1:
            
            for indxletter, letter in enumerate(needle):

                if haystack[indx + indxletter] == letter:
                    continue
                else:
                    indx += 1
                    break
            else:
                return indx

        return -1

        