class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #or we can use end points as intervals to check if it is between
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = (end+start)//2
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid])-1]:
                start1 = 0
                end1 = len(matrix[mid]) -1
                while start1 <= end1:
                    mid1 = (end1+start1)//2
                    if matrix[mid][mid1] == target:
                        return True
                    elif matrix[mid][mid1] < target:
                        start1 = mid1 + 1
                    elif matrix[mid][mid1] > target:
                        end1 = mid1 - 1
                return False
            elif matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][len(matrix[mid])-1] < target:
                start = mid + 1
        return False
        