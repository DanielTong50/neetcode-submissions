class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} #we use sorted version for keys
        for string in strs: #traverse through all strings
            setstring = "".join(sorted(string)) #this gives sorted
            result.setdefault(setstring, []).append(string)
            #this handles both functionality
            #so we will hashmap with sorted keys -> and anagrams strings
        
        return list(result.values())
            

            