class Solution:
    def isValid(self, s: str) -> bool:
        #go through half of the string push to stack
        result = []
        for i in range(len(s)):
            if s[i] == "]":
                if not result:
                    return False
                if result.pop() != "[":
                    return False
            elif s[i] == "}":
                if not result:
                    return False
                if result.pop() != "{":
                    return False
            elif s[i] == ")":
                if not result:
                    return False
                if result.pop() != "(":
                    return False
            else:
                result.append(s[i])
        
        if not result:
            return True

        return False
        
        