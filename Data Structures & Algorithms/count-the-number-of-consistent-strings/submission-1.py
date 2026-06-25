class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        alist = set(allowed)
        count = 0

        for word in words:

            for letter in word:

                if letter not in alist:
                    break

            else:
                count += 1

        return count