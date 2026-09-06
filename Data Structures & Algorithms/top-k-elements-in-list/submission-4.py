class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create frequencies of nums
        #sort by values of highest
        #extract k times to result

        result = []

        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True))

        keys_only = list(sorted_freq.keys())
        
        for i in range(k):
            result.append(keys_only[i])
        
        return result