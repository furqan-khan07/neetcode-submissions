class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def getprod(nums: List[int]) -> int:

            count = 1

            for num in nums:
                count *= num

            return count

        ret = []
        indx = 0

        while indx < len(nums):
            ret.append(getprod(nums[:indx] + nums[indx + 1:]))
            indx += 1

        return ret




        