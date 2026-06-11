class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag = list(magazine)
        note = list(ransomNote)

        for char in mag:

            if char in note:
                note.remove(char)

                if not note:
                    return True
              

        
        return not note
        