class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        cost = 0


        while len(sticks) > 1:
            sticks.sort()
            added = sticks[0] + sticks[1] 
            cost += added
            sticks = sticks[2:]
            sticks.append(added)


        return cost
        