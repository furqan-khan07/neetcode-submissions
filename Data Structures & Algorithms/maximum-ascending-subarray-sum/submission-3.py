class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        maxsum = 0
        count = 0
        lastnum = 0
        indx = 0

        while indx < len(nums):

            if nums[indx] > lastnum:

                count += nums[indx]
                lastnum = nums[indx]
                indx += 1

            else:
                count = nums[indx]
                lastnum = nums[indx]
                indx += 1

            maxsum = max(maxsum, count)

        return maxsum










        