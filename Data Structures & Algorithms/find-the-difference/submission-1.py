class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        from collections import Counter

        sfreq = Counter(s)
        tfreq = Counter(t)

        for char in tfreq:
            if char not in sfreq:
                return char

            else:
                if tfreq[char] > sfreq[char]:

                    return char



        
        