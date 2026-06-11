class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index, number in enumerate(nums):
            lookfor = target - number

            if lookfor in seen:
                return[seen[lookfor], index]

            seen[number] = index



        