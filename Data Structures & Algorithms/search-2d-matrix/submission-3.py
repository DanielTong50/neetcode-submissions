class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #treat like ranges, left = matrix[0] right = matrix[len(matrix)-1]
        #mid = left + (right - left)//2
        #if target is in the range of mid -> search through it and get answer
        #if target is too big for range, create new mid
        if len(matrix) == 0:
            return false
        left = 0
        right = len(matrix)-1
        while left <= right:
            mid = left + (right-left)//2
            if (matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid])-1]):
                #we are good and can check
                return target in matrix[mid]
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][len(matrix[mid])-1]:
                left = mid + 1
        return False
        