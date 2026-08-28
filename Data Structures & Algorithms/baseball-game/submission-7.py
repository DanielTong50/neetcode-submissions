class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in range(len(operations)):
            if operations[i] == "+":
                result.append(result[len(result)-1] + result[len(result)-2])
            elif operations[i] == "C":
                result.pop()
            elif operations[i] == "D":
                result.append(result[len(result)-1] * 2)
            else:
                result.append(int(operations[i]))
        
        return sum(result)