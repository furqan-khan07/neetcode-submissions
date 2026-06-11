class Solution:
    def missingNumber(self, nums: List[int]) -> int:


        lenofn = len(nums)
        expectedsumofn = (lenofn * (lenofn+1) // 2)
        actualsum = sum(nums) 

        return expectedsumofn - actualsum


