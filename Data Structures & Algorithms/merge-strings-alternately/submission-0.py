class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        retstring = ""

        lenw1 = len(word1)
        lenw2 = len(word2)


        for x in range(min(lenw1, lenw2)):
            retstring += word1[x] + word2[x]

            if x == lenw1 - 1:
                retstring += word2[x + 1::]
                return retstring
            
            if x == lenw2 - 1:
                retstring += word1[x + 1::]
                return retstring

        return retstring


        
        





            
        