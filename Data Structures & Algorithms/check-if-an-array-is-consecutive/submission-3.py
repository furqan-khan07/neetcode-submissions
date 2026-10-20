class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        nums.sort()
        indx = 0

        for indx in range(len(nums) - 1):
            if nums[indx] + 1 != nums[indx + 1]:
                return False


        return True



