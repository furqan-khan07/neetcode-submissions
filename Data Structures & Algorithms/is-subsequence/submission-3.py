class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        tpt = 0
        spt = 0
        slen = len(s)
        tlen = len(t)

        if slen > tlen:
            return False

        while spt < slen and tpt < tlen:

            if s[spt] == t[tpt]:
                spt += 1
                tpt += 1
            
            else:
                tpt += 1

        return spt == slen



            

        
        