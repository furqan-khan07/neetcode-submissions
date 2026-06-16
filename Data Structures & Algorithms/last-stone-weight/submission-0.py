class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 0:

            if len(stones) == 1:
                return stones[0]

            else:
                biggest = max(stones)
                stones.remove(biggest)
                second = max(stones)
                stones.remove(second)


                if biggest == second:
                    pass
                if biggest > second:
                    stones.append(biggest - second)
                
        return 0



        