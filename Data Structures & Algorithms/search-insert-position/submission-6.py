class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        if target in nums:
            return nums.index(target)

        lnums = len(nums)
        low = 0
        high = lnums - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return low




        



       