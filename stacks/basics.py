# Implement Stack from List/Array
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return not self.stack
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)

# s = Stack()
# s.push(2)
# s.push(8) 
# s.push(5)
# s.display()
# print(s.top())
# print(s.pop())
# s.pop()
# s.pop()
# print(s.is_empty())
# print(s.size())
# s.display()

# Implement Stack using Linked List
class LinkedList:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.cur_size = 0

    def push(self, val):
        new_node = LinkedList(val)
        new_node.next = self.top
        self.top = new_node
        self.cur_size +=1

    def pop(self):
        if self.top is None:
            return None
        
        val = self.top.val
        self.top = self.top.next
        self.cur_size -=1
        return val
    
    def peek(self):
        return None if self.top is None else self.top.val
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self.cur_size
    
    def display(self):
        cur = self.top
        while cur:
            print(cur.val)
            cur = cur.next

# s = Stack()
# s.push(2)
# s.push(8) 
# s.push(5)
# s.display()
# print(s.peek())
# print(s.pop())
# s.pop()
# s.pop()
# print(s.is_empty())
# print(s.size())
# s.display()


# Implement Queue using Stack
class Stack:
    def __init__(self) -> None:
        self.input_stack = []
        self.output_stack = []
    
    def push(self, val):
        self.input_stack.append(val)
    
    def pop(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop(0))
        print(self.output_stack)
        return self.output_stack.pop()

    def top(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        print(self.output_stack)
        return self.output_stack[-1]
    
    def is_empty(self):
        return not self.input_stack and not self.output_stack
    
    def size(self):
        return len(self.output_stack)
    
    def display(self):
        print(self.input_stack)
        print(self.output_stack)

s = Stack()
s.push(2)
s.push(8) 
s.push(5)
s.display()

print(s.top())

print(s.pop())
s.pop()
s.pop()
print(s.is_empty())
print(s.size())
s.display()