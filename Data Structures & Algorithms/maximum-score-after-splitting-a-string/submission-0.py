class Solution:
    def maxScore(self, s: str) -> int:

        score = 0
        

        for count in range(len(s) - 1):

            left = s[:count + 1]
            right = s[count + 1:]

            zeros = 0
            ones = 0
            for val in left:
                if val == "0":
                    zeros += 1

            for val in right:
                if val == "1":
                    ones += 1
            
            score = max(score, ones + zeros)
        
        return score