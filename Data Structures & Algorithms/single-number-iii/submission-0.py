class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        freq = Counter(nums)
        ret = []

        for num, count in freq.items():
            if count == 1:
                ret.append(num)

        return ret

        