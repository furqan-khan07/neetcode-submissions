class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maxarr = []

        for indx, num in enumerate(arr):

            if indx != len(arr) - 1:
                maxarr.append(max(arr[indx + 1::]))

            else:
                maxarr.append(-1)

        return maxarr


        