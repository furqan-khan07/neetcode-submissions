class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:


        freq = {}

        for indx, num in enumerate(arr1):

            if num not in freq:
                freq[num] = 1

            else:
                freq[num] += 1

        

        ret = []

        for num in arr2:
            for x in range(freq[num]):
                ret.append(num)

        extra = []
        for num in arr1:
            if num not in arr2:
                extra.append(num)

        extra.sort()

        ret += extra

        return ret

        