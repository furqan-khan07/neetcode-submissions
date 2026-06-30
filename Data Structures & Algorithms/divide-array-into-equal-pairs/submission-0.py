class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        freq = {}

        for num in nums:

            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

            
        for num in freq:
            if freq[num] % 2 != 0:
                return False

        return True
        