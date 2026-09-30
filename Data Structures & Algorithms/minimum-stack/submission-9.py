class MinStack:
    
    def __init__(self):
        self.items = []
        self.prefix_minimum = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.prefix_minimum) == 0:
            self.prefix_minimum.append(val)
        else:
            self.prefix_minimum.append(min(val, self.prefix_minimum[-1]))

    def pop(self) -> None:
        self.items.pop()
        self.prefix_minimum.pop()

    def top(self) -> int:
        return self.items[-1]
        
    def getMin(self) -> int:
        return self.prefix_minimum[-1]
        
