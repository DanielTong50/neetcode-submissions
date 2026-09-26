class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        final = right
        while left <= right:
            current = 0
            mid = left + ((right-left)//2)
            for pile in piles:
                current+=math.ceil(pile/mid)
            if current <= h:
                final = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return final
            