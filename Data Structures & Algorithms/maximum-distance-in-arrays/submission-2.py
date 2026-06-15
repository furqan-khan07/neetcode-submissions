class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        smalls = []
        bigs = []

        for indx, arr in enumerate(arrays):
            smalls.append([arr[0], indx])
            bigs.append([arr[-1], indx])

        smalls.sort()
        bigs.sort(reverse=True)


        if smalls[0][1] != bigs[0][1]:
            return bigs[0][0] - smalls[0][0]

        else:
            return max(bigs[0][0] - smalls[1][0], bigs[1][0] - smalls[0][0])

        



        






        

        



        


        