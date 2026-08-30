class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = {}
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and j <= i + k:
                if nums[i] == nums[j]:
                    return True
                j+=1
            i+=1
        return False
                
        
        