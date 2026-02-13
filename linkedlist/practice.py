'''
core operations

1. Traverse
2. Reverse
3. Insert at position
4. Delete a node
5. Find middle
6. Detect cycle
7. Merge two sorted lists
8. Remove nth node from end

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create nodes
l1 = ListNode(6)
l2 = ListNode(10)
l3 = ListNode(1)
l4 = ListNode(8)


# Link nodes
l1.next = l2
l2.next = l3
l3.next = l4

head = l1

def traverse(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

def reverse(head):
    cur = head
    prev = None

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

# reversed_head = reverse(head)
# traverse(reversed_head)

def insert_at_pos(head, new_node, pos):
    cur = head
    index = 0

    if pos == 0:
        new_node.next = cur
        return new_node
    
    while cur and index < pos-1:
        cur = cur.next
        index += 1
    
    if not cur:
        return head
    
    new_node.next = cur.next
    cur.next = new_node
    return head
  
# new_node = ListNode(5)
# pos = 4
# new_list = insert_at_pos(head, new_node, pos)
# traverse(new_list)

def delete_node(head, pos):
    cur = head
    index = 0

    if pos == 0:
        cur = cur.next
        return cur
    
    while cur and index < pos - 1:
        cur = cur.next
        index+=1

    if cur and cur.next:
        cur.next = cur.next.next
    return head

# updated_list = delete_node(head, 3)
# traverse(updated_list)

def find_middle(head):
    '''
    # This code is great but not optimal better to use floyd algorithm.
    cur = head
    index = 0

    while cur:
        cur = cur.next
        index+=1
    
    middle_index = index // 2

    index = 0
    cur = head
    while cur and index < middle_index:
        cur = cur.next
        index+=1

    return cur.val, middle_index
    '''
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

l5 = ListNode(9)
l4.next = l5
l6 = ListNode(3)
l5.next = l6
middle_node = find_middle(head)
# print(middle_node.val)

# traverse(head)
# val, index = find_middle(head)
# print(val, index)

# Detect cycle
def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

# print(detect_cycle(head))

# Merge two sorted lists

# Remove nth node from end
def remove_nth_node_from_end(head, n):
    p1 = head
    p2 = head
    index = 0

    while p1 and index < n-1:
        p1 = p1.next
        index +=1
    
    while p1:
        p2 = p2.next
        p1 = p1.next

    p2.next = p1

    return head

updated_list = remove_nth_node_from_end(head, 2)
traverse(updated_list)