class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        import math
        amnt = math.floor(len(nums) / 3)
        freq = Counter(nums)
        ret = []

        for num, count in freq.items():
            if count > amnt:
                ret.append(num)

        return ret


        