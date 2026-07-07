class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        freq = Counter(nums)

        freqsorted = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        ret = list(freqsorted)[:k]

        return ret



        