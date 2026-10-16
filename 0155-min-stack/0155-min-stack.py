
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:

        self.stack.append(value)
        self.min.append(
            value if not self.min else min(value, self.min[-1])
        )
        
    def is_empty(self) -> None:
        return len(self.stack) == 0

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("Underflow")
        popped = self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("Underflow")
        return self.stack[-1]        

    def getMin(self) -> int:
        if self.is_empty():
            raise IndexError("Underflow")
        return self.min[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()