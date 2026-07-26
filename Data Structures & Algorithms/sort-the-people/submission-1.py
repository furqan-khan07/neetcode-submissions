class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        freq = {}
        for name, height in zip(names, heights):
            freq[height] = name

        return [freq[h] for h in sorted(freq, reverse=True)]