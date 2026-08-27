class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        freq = {}
        ret = []

        for arr in grid:
            for num in arr:
                if num not in freq:
                    freq[num] = 1
                else:
                    freq[num] += 1

        
        for num in freq:
            if freq[num] == 2:
                ret.append(num)
                break

        
        nums = []


        for x in range(1, (len(grid) **2) + 1):
            nums.append(x)


        for num in nums:
            if num not in freq:
                ret.append(num)
                return ret

    