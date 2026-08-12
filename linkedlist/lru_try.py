
class Node:
    def __init__(self, key=0, val=0) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = {}
        self.capacity = capacity

        # dummy nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_mru(self, cur_node):
        # 1. Remove node from current position
        if cur_node.prev:
            cur_node.prev.next = cur_node.next # prev -> next pointer link
            cur_node.next.prev = cur_node.prev

        # 2. Insert node before tail
        cur_node.prev = self.tail.prev
        cur_node.next = self.tail

        self.tail.prev.next = cur_node
        self.tail.prev = cur_node

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        
        # move the key to MRU
        cur_node = self.lru_cache[key] # fetch the existing node
        self.move_to_mru(cur_node)

        return cur_node.val
        
    def put(self, key: int, value: int) -> None:
        # 3 cases - key exists, key doesn't, capcity full

        if key in self.lru_cache:
            # move the key to MRU
            cur_node = self.lru_cache[key] # fetch the existing node
            cur_node.val = value # update the value
            self.move_to_mru(cur_node)
         
        else:
            if len(self.lru_cache) == self.capacity:
                # capcity is zero, so evict LRU

                # LRU node
                lru_node = self.head.next

                # Remove from linked list
                self.head.next = lru_node.next
                lru_node.next.prev = self.head

                # Remove from hashmap
                del self.lru_cache[lru_node.key]

            cur_node = Node(key, value)
            self.lru_cache[key] = cur_node

            self.move_to_mru(cur_node)
            
'''
Node Class:
    - defining a node contain (key, val) pair
    - next, prev pointers

'''
class Node:
    def __init__(self, key ,val):
        self.key , self.val = key , val
        # maintain next , previous pointers
        self.next  = self.prev = None

'''
LRUCache Class (HashMap):
    - small & fast memory holding the MRU elements in memory
    Constructor:
        1- Maintain a fixed capacity of a given size
        2- Initialize the head and Right pointers keep track of LRU element & MRU element Simultaneously
            - Left pointer -> track LRU
            - tail pointer -> track MRU
            - head & tail pointer must be connected (all the insertion of nodes will be done in middle between them)
    methods:
        1- get:
            - searches the hashmap for a given key if exists:
                a- return the value
                b- track the given node as MRU
        2- put:
            - insert a new element in the cache:
            - check the size of the cache (if cache size >= capacity):
                a- find the LRU element
                b- evict the LRU element
                c- insert the new element

        Helper function dealing with the Doubly Linked List:

        3- insert 
            - maintain 

        4- remove

'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Define an empty hash map
        self.cache = {}
        # Initialize the Dummy head and tail pointer to keep track of LRU and MRU elements & connect both of thrm
        self.head , self.tail = Node(0,0) , Node(0,0)
        self.head.next , self.tail.prev = self.tail , self.head
        
    def remove(self , node: Node):
        prevNode , nextNode = node.prev , node.next
        prevNode.next , nextNode.prev = nextNode , prevNode


    def insert(self , node: Node):
        # insertion happens at the End due MRU
        prevNode , nextNode = self.tail.prev, self.tail
        prevNode.next = nextNode.prev = node
        node.prev , node.next = prevNode , nextNode


    def get(self, key: int) -> int:
        # check if key exists in cache (hashmap)
        if key in self.cache:
            # Maintain Node in the Double Linked List & move element to MRU
            self.remove(self.cache[key])    # remove the LRU element
            self.insert(self.cache[key])    # insert it again to be appened to MRU
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # case-1: key is already in Cache -> update the value only & move it to MRU
        if key in self.cache:
            self.remove(self.cache[key]) # remove from Double Linked List
        # create a new node 
        # will works either if element is a new node (haven't existed in cache) or we are updating value of an existing element
        self.cache[key] = Node(key , value)
        # 2- Insert in Doubly linked list
        self.insert(self.cache[key])

        # check if the length of hashmap > capacity: evict LRU from hashmap + delete Node from Linked list
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]


lRUCache = LRUCache(2)
lRUCache.put(1, 10)  # cache: {1=10}
print(lRUCache.get(1))     # return 10
lRUCache.put(2, 20)  # cache: {1=10, 2=20}
lRUCache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
print(lRUCache.get(2))     # returns 20 
print(lRUCache.get(1))      # return -1 (not found)

# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

# Output:
# [null, null, 10, null, null, 20, -1]