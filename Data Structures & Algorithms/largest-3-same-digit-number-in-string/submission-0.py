class Solution:
    def largestGoodInteger(self, num: str) -> str:

        threenums = []

        indx = 0

        while indx < len(num) - 2:

            if num[indx] == num[indx + 1] == num[indx + 2]:
                threenums.append(num[indx] * 3)
                indx += 1

            else:
                indx += 1

        if threenums:
            return max(threenums)
        else:
            return ""
