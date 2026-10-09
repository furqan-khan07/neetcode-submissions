class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        
        hashed = {}
        total = 0
        for indx, char in enumerate(keyboard):
            hashed[char] = indx

        
        for indx in range(len(word) - 1):
            total += abs(hashed[word[indx]] - hashed[word[indx + 1]])

        return total + hashed[word[0]]





            



        
        