class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def move(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            
    def pop(self) -> int:
        self.move()
        return self.output_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not(self.output_stack) and not(self.input_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()