class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        #go through list of lists -> similar pairs
        if len(sentence1) != len(sentence2):
            return False
        #we need a set of all the values to check membership
        dictionary = set(map(tuple, similarPairs))

        for i in range(len(sentence1)):
            if sentence2[i] != sentence1[i]:
                if (sentence1[i], sentence2[i]) not in dictionary and (sentence2[i], sentence1[i]) not in dictionary:
                    return False
        

        return True
            
        