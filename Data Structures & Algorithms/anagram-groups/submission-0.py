class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = []
        seen = {}

        for word in strs:

            makesim = "".join(sorted(word))

            if makesim in seen:
                seen[makesim].append(word)
            else:
                seen[makesim] = [word]

        for key in seen:
            ret.append(seen[key])

        return ret






        


        


            


       






                
        