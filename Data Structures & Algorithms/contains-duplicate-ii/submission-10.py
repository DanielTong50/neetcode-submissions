class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = {}
        for i in range(len(nums)):
            duplicate.setdefault(nums[i], []).append(i)

        values_only = list(duplicate.values())

        for list_of_indices in values_only:
            for index in range(len(list_of_indices)-1):
                if list_of_indices[index+1] - list_of_indices[index] <= k:
                    return True
        
        return False