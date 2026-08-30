class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            j = i + 1
            for j in range(len(nums)):
                if nums[i] == nums[j] and abs(i - j)<=k and i != j:
                    return True
        return False