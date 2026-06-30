class Solution:
    def confusingNumber(self, n: int) -> bool:

        numstring = str(n)
        for num in numstring:
            if int(num) not in [0, 1, 6, 8, 9]:
                return False

        newnum = ""

        for num in numstring[::-1]:
            if int(num) not in [6, 9]:
                newnum += num

            elif int(num) == 6:
                newnum += "9"
            elif int(num) == 9:
                newnum += "6"

        if newnum == numstring:
            return False


        return True




        