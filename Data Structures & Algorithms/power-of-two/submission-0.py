class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        import math

        if n > 0 and (math.log2(n) % 1 == 0):
            return True

        return False
