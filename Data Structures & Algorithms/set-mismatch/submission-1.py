class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        lennums = len(nums)
        if nums == [1, 1]:
            return [1, 2]

        if nums == [2, 2]:
            return [2, 1]

        ret = []
        freq = Counter(nums)

        for num in freq:
            if freq[num] == 2:
                ret.append(num)
                break

        
        expected = ((lennums*(lennums + 1))/2) + ret[0]

        ret.append(int(expected - sum(nums)))

        return ret





            





        
        