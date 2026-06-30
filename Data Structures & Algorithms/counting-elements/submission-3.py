class Solution:
    def countElements(self, arr: List[int]) -> int:

        count = 0
        lenarr = len(arr)

        for indx, num in enumerate(arr):

            if num + 1 in arr:
                count += 1

        return count
        