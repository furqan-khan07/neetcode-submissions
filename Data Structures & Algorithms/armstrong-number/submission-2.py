class Solution:
    def isArmstrong(self, n: int) -> bool:

        power = len(str(n))
        running = 0

        for num in str(n):
            running += int(num) ** power

        return running == n
        