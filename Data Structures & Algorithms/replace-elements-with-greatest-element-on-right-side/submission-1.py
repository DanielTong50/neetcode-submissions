class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        largest = -1
        for num in reversed(arr):
            result.append(largest)
            if num >= largest:
                largest = num
            
        result.reverse()

        result[len(result)-1] = -1

        return result