class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = {}
        for i in range(len(nums)):
            duplicate.setdefault(nums[i], []).append(i)

        values_only = list(duplicate.values())
        for indices in values_only:
            for j in range(len(indices) - 1):
                if indices[j+1] - indices[j] <= k:
                    return True
        return False