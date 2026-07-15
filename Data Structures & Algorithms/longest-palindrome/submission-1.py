class Solution:
    def longestPalindrome(self, s: str) -> int:

        from collections import Counter
        freq = Counter(s)
        count = 0
        odds = 0


        for value in freq.values():

            count += value // 2 * 2
            odds += value - value // 2 * 2


        if odds >= 1:
            count += 1

        return int(count)


        