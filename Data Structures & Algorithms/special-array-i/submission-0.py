class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        count = 0

        while count != len(nums) - 1:

            if (nums[count] % 2 == 0 and nums[count + 1] % 2 == 0) or (nums[count] % 2 == 1 and nums[count + 1] % 2 == 1):
                return False

            count += 1

        return True
        