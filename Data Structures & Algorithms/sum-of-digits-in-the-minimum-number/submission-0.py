class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        
        mini = min(nums)
        sumd = 0

        for digi in str(mini):
            sumd += int(digi)

        
        if sumd % 2 == 0:
            return 1
        else:
            return 0

