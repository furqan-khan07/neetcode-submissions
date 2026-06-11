class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        max1 = 0

        for num in nums:
            if num == 1:
                count += 1

                if count > max1:
                    max1 = count
            else:
                count = 0

        return max1

        