class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        left = 0
        right = len(nums) - 1
        maxsum = 0
        nums.sort()

        while left < right:

            cursum = nums[left] + nums[right]

            if cursum >= k:
                right -= 1
            
            elif cursum < k:
                left += 1
                maxsum = max(maxsum, cursum)


        if maxsum == 0:
            return -1
        else:
            return maxsum

        
        