class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #if max (index) - current (index), aka the difference
        #so you start and then you check to see if there is a bigger one
        result = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            area = (end - start) * (min(heights[end],heights[start]))
            result = max(result,area)
            if heights[start] >= heights[end]:
                end-=1
            else:
                start+=1
        return result
                

