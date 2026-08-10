class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices.sort()
        least = prices[0]
        least2 = prices[1]
        left = money - least - least2

        if left >= 0:
            return left

        else:
            return money


        