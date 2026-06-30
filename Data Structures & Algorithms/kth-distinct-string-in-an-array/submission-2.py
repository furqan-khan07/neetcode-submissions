class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        from collections import Counter

        freq = Counter(arr)
        unique = []

        for char in freq:

            if freq[char] == 1:
                unique.append(char)

        if k > len(unique):
            return ""

        else:
            return unique[k - 1]

        