class MinStack:

    def __init__(self):
        self.minStack = []
        self.minn = []
        
        

    def push(self, val: int) -> None:
        
        self.minStack.append(val)
        if not self.minn or val <= self.minn[-1]:
            self.minn.append(val)
        

        

    def pop(self) -> None:
        
        if self.minStack[-1] == self.minn[-1]:
            self.minn.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.minStack[len(self.minStack)-1]
        

    def getMin(self) -> int:
        return self.minn[-1]
        

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()