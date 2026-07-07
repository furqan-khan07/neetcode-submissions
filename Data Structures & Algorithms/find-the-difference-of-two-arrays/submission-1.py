class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        num1 = []
        num2 = []

        for num in nums1:
            if num not in nums2:
                num1.append(num)

        for num in nums2:
            if num not in nums1:
                num2.append(num)

        return [list(set(num1)), list(set(num2))]
