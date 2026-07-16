class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        lennums = len(nums2)
        ret = []

        for num in nums1:
            indx = 0
            while indx < lennums:
                if nums2[indx] == num:
                    ret.append(indx)
                    break
                else:
                    indx += 1

        return ret
