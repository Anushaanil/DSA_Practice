'''
 # @ Create Time: 2026-02-12 01:01:15
 # @ Modified time: 2026-02-17 22:05:07
'''
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
l5 = ListNode(5)
l6 = ListNode(45)


# Link nodes
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

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

def reverse_from_specific_positions(head, l, r):
    dummy = ListNode(0)
    dummy.next = head

    cur = head
    prev = dummy
    prevSub = None
    
    for _ in range(l-1):
        prev = cur
        cur = cur.next
    
    start = cur

    for _ in range(r-l+1):
        tmp = cur.next
        cur.next = prevSub
        prevSub = cur
        cur = tmp
    
    prev.next = prevSub
    start.next = cur

    return dummy.next

# reversed_head = reverse_from_specific_positions(head, 2, 4)
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
def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1
    
    if l2:
        tail.next = l2

    return dummy.next

l1 = ListNode(1)
n_1 = ListNode(2)
l1.next = n_1
n_2 = ListNode(5)
n_1.next = n_2
n_3 = ListNode(7)
n_2.next = n_3

l2 = ListNode(3)
n_4 = ListNode(4)
l2.next = n_4
n_5 = ListNode(6)
n_4.next = n_5

# merged_node = merge_two_sorted_lists(l1, l2)
# traverse(merged_node)


# Remove nth node from end
def remove_nth_node_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head

    p1 = dummy
    p2 = dummy

    for _ in range(n+1):
        p1 = p1.next
    
    while p1:
        p1 = p1.next
        p2 = p2.next
    
    p2.next = p2.next.next

    return dummy.next
    # p1 = head
    # p2 = head
    # index = 0

    # while p1 and index < n-1:
    #     p1 = p1.next
    #     index +=1
    
    # while p1:
    #     p2 = p2.next
    #     p1 = p1.next

    # p2.next = p1

    # return head
# traverse(head)
# updated_list = remove_nth_node_from_end(head, 2)
# traverse(updated_list)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    l1_str = l2_str = ''

    while l1:
        l1_str = l1_str + str(l1.val)
        l1 = l1.next
    
    while l2:
        l2_str = l2_str + str(l2.val)
        l2 = l2.next
    
    total = str(int(l1_str) + int(l2_str))
    dummy = ListNode(0)
    tail = dummy

    for val in total:
        new_node = ListNode(val)
        tail.next = new_node
        tail = tail.next
    
    return dummy.next

# new_list = addTwoNumbers(l1, l2)
# traverse(new_list)

from collections import defaultdict

def deleteDuplicates_hash(head):
    counter = defaultdict(int)
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    prev = dummy

    while cur:
        counter[cur.val]+=1
        cur = cur.next

    cur = head
    
    while cur:
        if counter[cur.val] > 1:
            prev.next = cur.next
        else:
            prev = cur

        cur = cur.next

    return dummy.next

def deleteDuplicates(head):
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    prev = dummy

    
    while cur:
        # print(prev.val, cur.val, cur.next.val)
        if cur.next and cur.val == cur.next.val:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            prev.next = cur.next
        else:
            prev = cur

        cur = cur.next

    return dummy.next

l1 = ListNode(0)
n_1 = ListNode(1)
l1.next = n_1
n_2 = ListNode(2)
n_1.next = n_2
# n_3 = ListNode(3)
# n_2.next = n_3
# n_4 = ListNode(5)
# n_3.next = n_4

head = l1

# new_list = deleteDuplicates(head)
# traverse(new_list)

def rotateRight(head, k):
    cur = head
    total_len = 0

    while cur:
        total_len +=1
        cur = cur.next
        
    
    rotations = k % (total_len)

    start = head
    cur = head
    split_node = head
    start_node = head

    for i in range(total_len-1):
        if i == total_len-rotations-1:
            start_node = cur.next
            split_node = cur
            
        cur = cur.next
    
    cur.next = start
    split_node.next = None
    
    return start_node

new_list = rotateRight(head, 4)
traverse(new_list)