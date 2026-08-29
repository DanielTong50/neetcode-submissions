class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        #creates frequencies for string s
        for i in range(len(s)):
            s1[s[i]] = s1.get(s[i], 0) + 1

        #creates frequencies for string t
        for i in range(len(t)):
            s2[t[i]] = s2.get(t[i], 0) + 1

        print(s1)
        print(s2)
        return s1 == s2