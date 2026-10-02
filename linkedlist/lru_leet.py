class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    # use DLL for O(1) time operations
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def rearrange_lru_order_in_node(self, node):
        # add the node before the tail at end
        temp1 = node.prev
        temp2 = node.next

        if temp1:temp1.next = temp2
        if temp2:temp2.prev = temp1

        temp3 = self.head.next

        self.head.next = node
        node.next = temp3
        node.prev = self.head
        temp3.prev = node
        

    def delete_node(self):
        # remove the node at the back
        temp1 = self.tail.prev
        print('keyyy', temp1.key if temp1 else None)
        temp2 = temp1.prev if temp1 else None
        
        if temp2:
            temp2.next = self.tail
            self.tail.prev = temp2

        print('del key', temp1.key if temp1 else None)
        return temp1.key if temp1 else None

    def get(self, key: int) -> int:
        print('cache', self.cache)

        cache_key = self.cache.get(key)

        if not cache_key:
            return -1
        
        val = cache_key.val

        # function to rearrange LRU cache to move it to the front
        self.rearrange_lru_order_in_node(cache_key)

        return val


    def put(self, key: int, value: int) -> None:
        node_obj = self.cache.get(key)
        print(node_obj)
        print(len(self.cache), self.capacity, key, value)

        if node_obj:
            node_obj.val = value

        elif len(self.cache) < self.capacity:
            self.cache[key] = Node(key, value)

        else:
            print('I am here')
            # evict the LRU key and update cache
            del_key = self.delete_node()
            if del_key: del self.cache[del_key]
            self.cache[key] = Node(key, value)

        # function to rearrange LRU cache to move it to the front
        self.rearrange_lru_order_in_node(self.cache[key])

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