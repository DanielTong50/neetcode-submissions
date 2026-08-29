class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result+=word
            result+="•"
        return result
    
    def decode(self, s: str) -> List[str]:
        result = []
        temp = ""
        for char in s:
            if char == "•":
                result.append(temp)
                temp = ""
            else:
                temp+=char
        
        return result
            
            