class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        final_result = right
        while left <= right:
            count = 0
            k = left + (right - left)//2
            for pile in piles:
                count+= math.ceil(pile/k)
            if count <= h:
                final_result = k
                right = k -1
            elif count > h:
                left = k + 1

        return final_result