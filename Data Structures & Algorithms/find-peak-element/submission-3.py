class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        lennums = len(nums)

        if lennums == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return lennums - 1

        for i in range(1, lennums - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i



        