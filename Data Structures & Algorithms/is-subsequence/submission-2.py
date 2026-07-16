class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        tpt = 0
        spt = 0
        slen = len(s)

        while spt < slen and tpt < len(t):

            if s[spt] == t[tpt]:
                spt += 1
                tpt += 1
            
            else:
                tpt += 1

        return spt == slen



            

        
        