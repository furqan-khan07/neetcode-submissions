class Solution:
    def maxDifference(self, s: str) -> int:


        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        maxodd = 0
        mineven = sum(freq.values())

        for val in freq.values():
            if val % 2 != 0:
                maxodd = max(maxodd, val)

            else: 
                mineven = min(mineven, val)
        
        return (maxodd - mineven)
        