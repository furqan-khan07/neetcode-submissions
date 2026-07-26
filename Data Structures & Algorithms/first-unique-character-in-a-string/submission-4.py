class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = Counter(s)

        for char, count in freq.items():
            if count == 1:
                return s.find(char)

        return -1
        