class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        ret = []

        for word in words:

            for word2 in words:
                if word != word2:
                    if word in word2:
                        ret.append(word)

        
        return list(set(ret))
        