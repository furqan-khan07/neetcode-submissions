class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        appearances = nums.count(target)

        if appearances > (len(nums) / 2):
            return True
        
        return False
        