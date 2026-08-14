class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        counts = {}
        for x in nums:
            if x == 1:
                counts[1] = counts.get(1,0) + 1
                if counts[1] > max:
                    max = counts[1]
            else:
                counts[1] = 0;
        return max

        