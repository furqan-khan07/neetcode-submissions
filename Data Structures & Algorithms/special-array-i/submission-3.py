class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        count = 0

        while count != len(nums) - 1:

            if (nums[count] % 2 == 0 and nums[count + 1] % 2 != 0) or (nums[count] % 2 != 0 and nums[count + 1] % 2 == 0):
                count += 1 
            else:
                return False



        return True
        