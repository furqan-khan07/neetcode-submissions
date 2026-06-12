class Solution:
    def findLucky(self, arr: List[int]) -> int:

        count = {}
        freq = []

        for num in arr:
            if num in count:
                count[num] += 1

            else:
                count[num] = 1
 
        for num in count:
            if num == count[num]:
                freq.append(num)
        

        if freq:
            return max(freq)

        else:
            return -1
        