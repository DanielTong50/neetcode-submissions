class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        lowest = right
        while left <= right:
            mid = left + (right-left)//2
            current = 0
            print(current)
            for pile in piles:
                current+=math.ceil(pile/mid)
            print (current)
            if current <= h:
                lowest = min(lowest,mid)
                right = mid - 1
                
            else:
                left = mid + 1
        return lowest