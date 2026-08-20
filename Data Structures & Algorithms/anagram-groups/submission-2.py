class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create empty list, it will store lists in them
        #every element within that list, will be a list of all anagrams
        #meaning the sets of the chars are equal

        #a couple things
        #go through strs, word by word and compare if a set of that
        #is equal to the first element -> of each element (since it is the same)

        #if we go through the whole thing without any success, then we add a new list to the output which contains 1 element (which is the str)

        output = {}

        for str in strs:
            key = "".join(sorted(str))

            output.setdefault(key, []).append(str)
        

        return list(output.values())
