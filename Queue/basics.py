# Implement Queue using Arrays/List
# Pythonic way
class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        return self.queue.pop(0)
    
    def top(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self):
        return not self.queue
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)

# q = Queue()
# q.enqueue(2)
# q.enqueue(8) 
# q.enqueue(5)
# q.display()
# print(q.top())
# print(q.dequeue())
# q.dequeue()
# print(q.is_empty())
# print(q.size())
# q.display()

# Interview Expectations
class Queue:
    def __init__(self, size) -> None:
        self.max_size = size
        self.queue = [None]*size
        self.start = -1
        self.end = -1
        self.cur_size = 0
    
    def push(self, val):
        if self.cur_size == self.max_size:
            print("queue overflow")

        if self.cur_size == 0:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.max_size

        self.queue[self.end] = val
        self.cur_size+=1
    
    def pop(self):
        if self.cur_size == 0:
            return "Queue is empty"
        
        element = self.queue[self.start]
        self.queue[self.start] = None

        if self.cur_size == 1:
            self.start = self.end = -1

        else:
            self.start = (self.start + 1) % self.max_size

        self.cur_size-=1
        return element
            
    
    def top(self):
        if self.cur_size == 0:
            return None
        return self.queue[self.start]
    
    def is_empty(self):
        return self.cur_size == 0
    
    def size(self):
        return self.cur_size
    
    def display(self):
        print(self.queue)

# q = Queue(5)
# q.push(2)
# q.push(8) 
# q.push(5)
# q.display()
# print(q.top())
# print(q.pop())
# q.pop()
# print(q.is_empty())
# print(q.size())
# print(q.pop())
# print(q.pop())
# q.display()

# Implement Queue using Linked List
class LinkedList:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.cur_size = 0
    
    def push(self, val):
        new_node = LinkedList(val)
        if not self.start:
            self.start = self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

        self.cur_size+=1
    
    def pop(self):
        if self.start is None:
            return "queue is empty"

        val = self.start.val
        temp = self.start.next
        self.start = temp

        if self.start is None:
            self.end = None
            
        self.cur_size-=1

        return val
    
    def size(self):
        return self.cur_size
    
    def peek(self):
        return self.start.val if self.start else None
    
    def is_empty(self):
        return self.cur_size == 0
    
    def display(self):
        cur = self.start

        while cur:
            print(cur.val)
            cur = cur.next

q = Queue()
q.push(7)
q.push(2)
q.push(3)
q.push(5)
q.display()
print(q.pop())
print(q.peek())
q.pop()
q.pop()
print(q.is_empty())
print(q.size())
print(q.pop())
print(q.peek())
print(q.pop())
q.display()