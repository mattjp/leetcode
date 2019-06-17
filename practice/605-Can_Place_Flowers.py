# 605. Can Place Flowers
#
# Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
# However, flowers cannot be planted in adjacent plots - they would compete for water and both 
# would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means 
# not empty), and a number n, return if n new flowers can be planted in it without violating the
# no-adjacent-flowers rule.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            available += 1
        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            available += 1
        for plot in range(1,len(flowerbed)-1):
            if flowerbed[plot-1] == 0 and flowerbed[plot] == 0 and flowerbed[plot+1] == 0:
                flowerbed[plot] = 1
                available += 1
        if len(flowerbed) > 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            available += 1
        return available >= n
