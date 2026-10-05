class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        setnums = set(nums)

        
        bestlen = 0

        for num in setnums:
            lennums = 1
            if num - 1 in setnums:
                continue

            while num + lennums in setnums:
                lennums += 1

            bestlen = max(lennums, bestlen)

        return bestlen






        






        


        





        
                


        
        