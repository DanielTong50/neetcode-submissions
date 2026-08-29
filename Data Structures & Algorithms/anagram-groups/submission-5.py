class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} #we use sorted version for keys
        
        for string in strs: #traverse through all strings
            #count frequencies of string
            #transform to array -> and use that as a key (keystring)
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] +=1

            result.setdefault(tuple(count), []).append(string)
            
        
        return list(result.values())
        

            