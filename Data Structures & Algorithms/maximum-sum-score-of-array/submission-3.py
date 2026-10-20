class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:

        lennums = len(nums)
        if lennums == 1:
            return nums[0]

        total = sum(nums)
        running = 0
        scores = []

        for i in range(lennums):
            running += nums[i]
            scores.append(max(running, total - running + nums[i]))

        return max(scores)





        



