class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        appearances = nums.count(target)
        return appearances > len(nums) / 2
        