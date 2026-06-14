class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        from collections import Counter

        sort = Counter(nums)
        ones = []

        for num in sort:
            if sort[num] == 1:
                ones.append(num)

        if ones:
            return max(ones)
        else:
            return -1



        