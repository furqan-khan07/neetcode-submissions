class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        inboth = []
        if len(nums1) < len(nums2):

            for num in nums1:
                if num in nums2:
                    inboth.append(num)

        else:
            for num in nums2:
                if num in nums1:
                    inboth.append(num)

        return list(set(inboth))
        