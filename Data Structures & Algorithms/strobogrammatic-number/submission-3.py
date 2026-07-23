class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        newnum = ""

        for digit in num[::-1]:

            if digit == "0":
                newnum += "0"

            elif digit == "9":
                newnum += "6"

            elif digit == "6":
                newnum += "9"

            elif digit == "8":
                newnum += "8"

            elif digit == "1":
                newnum += "1"

            else:
                return False

        if num == newnum:
            return True

        else:
            return False


        