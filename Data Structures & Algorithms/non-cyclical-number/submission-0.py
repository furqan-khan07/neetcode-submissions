class Solution:
    def isHappy(self, n: int) -> bool:

        seen = []

        while n != 1:

            seen.append(n)
            sumnum = 0

            for dig in str(n):
                sumnum += int(dig)**2


            if sumnum in seen:
                return False
            
            n = sumnum
        
        return True