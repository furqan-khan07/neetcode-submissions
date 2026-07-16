class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        indx = 0
        endx = 1
        sumof = nums[0]

        while endx < len(nums):

            if nums[endx - 1] < nums[endx]:
                endx += 1

            else:
                sumof = max(sumof, sum(nums[indx:endx]))
                indx = endx
                endx = indx + 1

        sumof = max(sumof, sum(nums[indx:endx]))

        return sumof






        