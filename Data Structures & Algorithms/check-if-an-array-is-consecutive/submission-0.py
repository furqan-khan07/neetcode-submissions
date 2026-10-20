class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        nums.sort()
        indx = 0

        while indx < len(nums) - 1:
            if nums[indx] + 1 != nums[indx + 1]:
                return False

            indx += 1

        return True



