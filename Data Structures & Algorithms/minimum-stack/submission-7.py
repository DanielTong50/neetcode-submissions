class MinStack:

    def __init__(self):
        self.stack = [] #initializes regular stack
        self.prefix_sum = [] #initializes prefix stack

    def push(self, val: int) -> None:
        if not self.prefix_sum: #checks if it is empty
            self.stack.append(val)
            self.prefix_sum.append(val)
        else:
            self.stack.append(val)
            self.prefix_sum.append(min(val, self.prefix_sum[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_sum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_sum[-1]
        
 