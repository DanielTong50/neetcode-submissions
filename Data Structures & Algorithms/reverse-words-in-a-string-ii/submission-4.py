class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #reverse full array
        s.reverse()  

        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != " ":
                j+=1

            print(j)
            k = j - 1
            q = i
            while q < k:
                temp = s[q]
                s[q] = s[k]
                s[k] = temp
                k-=1
                q+=1

            i = j + 1
                     
                
        
        