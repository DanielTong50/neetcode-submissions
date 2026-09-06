class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1

        for i in range(k):
            max_key, max_value = max(count.items(), key=lambda item: item[1])
            result.append(max_key)
            count[max_key] = 0

        return result