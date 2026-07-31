class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        lenf = len(flowerbed)
        free = 0

        if lenf == 1 and flowerbed[0] == 0:
            return True

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            free += 1
            flowerbed[0] = 1
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            free += 1
            flowerbed[-1] = 1

        for i in range(1, lenf - 1):

            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                free += 1



        
        
        return free >= n

        

        

        