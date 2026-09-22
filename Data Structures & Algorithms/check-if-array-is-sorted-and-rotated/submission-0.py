class Solution:
    def check(self, nums: List[int]) -> bool:

        
        base = sorted(nums)

        for x in range(0, len(nums)):

            if nums == base[x::] + base[:x]:
                return True

        return False





        