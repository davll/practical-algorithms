class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0,1]
        #print(flowerbed)
        gapsize = 0
        count = 0
        for x in flowerbed:
            if x == 1:
                if gapsize > 2:
                    count += (gapsize - 2 + 1) // 2
                gapsize = 0
            else:
                gapsize += 1
        
        return count >= n
