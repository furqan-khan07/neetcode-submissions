class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        pairs = 0
        lennums = len(nums)

        for i in range(0, lennums):
            for j in range(i + 1, lennums):
                if nums[i] == nums[j]:
                    pairs += 1

        return pairs

        