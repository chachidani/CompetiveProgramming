# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.n = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.n:
            self.stack.append(x)
        

    def pop(self) -> int:
        if len(self.stack) > 0:
            m = self.stack.pop()
            return m
        return -1
        

    def increment(self, k: int, val: int) -> None:
        l = 0
        while l < len(self.stack) and k > 0 :
            self.stack[l] += val
            k -= 1
            l += 1

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)