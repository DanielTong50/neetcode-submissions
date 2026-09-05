class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) -1
        start = 0
        while start != end:
            result = numbers[start] + numbers[end]
            if result == target:
                return [start+1,end+1]
            elif result < target:
                start+=1
                continue
            else:
                end-=1
