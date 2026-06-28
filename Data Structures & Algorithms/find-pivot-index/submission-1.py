class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for indx, num in enumerate(nums):

            if indx == 0 and 0 == sum(nums[1::]):
                return 0

            else:
                if sum(nums[:indx]) == sum(nums[indx+1:]):
                    return indx

        return -1
        