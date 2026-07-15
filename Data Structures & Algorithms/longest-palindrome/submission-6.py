class Solution:
    def longestPalindrome(self, s: str) -> int:

        from collections import Counter
        freq = Counter(s)
        count = 0
        odds = 0


        for value in freq.values():

            running = value // 2 * 2
            count += running
            odds += value - running

        if odds >= 1:
            count += 1

        return int(count)


        