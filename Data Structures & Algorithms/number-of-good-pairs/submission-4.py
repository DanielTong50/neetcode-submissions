class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        num_dict = {}
        for i in range(len(nums)):
            num_dict.setdefault(nums[i], []).append(i)
        for list_item in list(num_dict.values()):
            curr = len(list_item)
            result+= int((curr*(curr-1))/2)
        return result
            