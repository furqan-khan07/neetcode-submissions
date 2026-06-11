class Solution:
    def missingNumber(self, nums: List[int]) -> int:


        count = 0

        while True:

            if count not in nums:
                return count
                break

            else: 
                count += 1
