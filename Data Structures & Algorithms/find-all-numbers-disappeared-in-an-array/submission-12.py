class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        ret = []
        nondup = [*range(1, len(nums) + 1)]

        for num in nondup:
            if num not in nums:
                ret.append(num)


        return ret


        