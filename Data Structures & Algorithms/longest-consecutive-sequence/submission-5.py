class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                temp_longest = 0 
                val = nums[i]
                while val in nums_set:
                    temp_longest+=1
                    val+=1
                    longest = max(temp_longest, longest)

        return longest
