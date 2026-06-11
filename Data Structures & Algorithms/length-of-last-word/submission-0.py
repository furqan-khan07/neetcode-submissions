class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        broken = s.split()

        return len(broken[-1])
        