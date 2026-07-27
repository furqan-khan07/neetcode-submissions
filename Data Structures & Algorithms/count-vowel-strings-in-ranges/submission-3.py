class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        ret = []
        vowels = ["a", "e", "i", "o", "u"]

        for quer in queries:

            count = 0
            for word in words[quer[0]:quer[1] + 1]:
                if word[0] in vowels and word[-1] in vowels:
                    count += 1

            ret.append(count)

        return ret


