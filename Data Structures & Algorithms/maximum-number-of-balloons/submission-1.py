class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        chars = {}

        for letter in text:

            if letter in chars:
                chars[letter] += 1

            else:
                chars[letter] = 1



        return min(
            chars.get("b", 0),
            chars.get("a", 0),
            chars.get("l", 0) // 2,
            chars.get("o", 0) // 2,
            chars.get("n", 0)
        )