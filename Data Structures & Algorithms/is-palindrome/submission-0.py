class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = "".join(char for char in s if char.isalnum())
        checks = cleaned.lower()

        if checks == checks[::-1]:
            return True

        return False