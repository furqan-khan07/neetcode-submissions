class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        ret = []

        nlist = [*range(1, len(nums) + 1)]

        for num in nlist:
            if num not in nums:
                ret.append(num)

        return ret

        