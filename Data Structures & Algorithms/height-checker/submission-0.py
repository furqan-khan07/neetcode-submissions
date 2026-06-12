class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        nonexp = 0

        expected = sorted(heights)

        for e, h in zip(expected, heights):

            if e != h:
                nonexp += 1

        return nonexp

        