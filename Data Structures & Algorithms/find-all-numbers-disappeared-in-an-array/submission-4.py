class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        seen = set(nums)
        ret = []

        for x in range(1, len(nums) + 1):
            if x not in seen:
                ret.append(x)

        return ret

        