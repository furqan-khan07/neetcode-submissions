class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        count = 0

        for word in words:

            running = list(chars)

            for letter in word:

                if letter not in running:
                    break

                else:
                    running.remove(letter)

            else:
                count += len(word)

        return count

            

        

