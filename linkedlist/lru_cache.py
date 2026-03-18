class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        
        # dummy head and tail nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after_head(self, node):
        next_head_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_head_node
        next_head_node.prev = node


    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        node = self.key_map.get(key)
        if node:
            self.delete_node(node)
            self.insert_after_head(node)
            print(node.val)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        node = self.key_map.get(key)
        if node:
            node.val = value
            self.delete_node(node)
            self.insert_after_head(node)
            
        else:
            if len(self.key_map) < self.capacity:
                new_node = Node(key, value)
                self.key_map[key] = new_node
                self.insert_after_head(new_node)
                
            else:
                lru_node = self.tail.prev
                self.delete_node(lru_node)
                del self.key_map[lru_node.key]
        
                new_node = Node(key, value)
                self.key_map[key] = new_node
                self.insert_after_head(new_node)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(4)

obj.put(2, 6)
obj.put(4, 7)
obj.put(8, 11)
obj.put(7, 10)
obj.get(2)
obj.get(8)
obj.put(5, 6)
obj.get(7)
obj.put(5, 7)
obj.get(5)