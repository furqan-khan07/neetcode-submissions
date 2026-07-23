class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math

        for num in range(k):

            mostgifts = max(gifts)
            giftsleft = math.floor(mostgifts ** 0.5)
            gifts[gifts.index(mostgifts)] = giftsleft


        return sum(gifts)

            


        