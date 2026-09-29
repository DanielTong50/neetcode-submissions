class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        final_result = right
        while left < right:
            count = 0
            k = left + (right - left)//2
            for pile in piles:
                count+= math.ceil(pile/k)
            if count <= h:
                right = k
            elif count > h:
                left = k + 1
        return left