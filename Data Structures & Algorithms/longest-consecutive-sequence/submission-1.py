class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            #if it is the start
            if nums[i] - 1 not in nums_set:
                val = nums[i]
                temp_longest = 0
                while val in nums_set:
                    temp_longest +=1
                    longest = max(temp_longest, longest)
                    val+=1
        return longest