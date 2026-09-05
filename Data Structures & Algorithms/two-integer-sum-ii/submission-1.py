class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_set = {}
        for i in range(len(numbers)):
            key = target - numbers[i]
            if key in hash_set and hash_set[key] < i:
                return [hash_set[key]+1, i+1]
            else:
                hash_set[numbers[i]] = i