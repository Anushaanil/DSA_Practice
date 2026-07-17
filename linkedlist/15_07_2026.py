from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def traverse(self, head):
        cur = head
        while cur:
            print(cur.val if cur else "0")
            print('->')
            print(cur.random.val if cur.random else None)
            print('\n')
            cur = cur.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_list = Node(0)

        dummy = new_list
        cur = head
        nodes_dict = {}

        # assign the next pointers and create new nodes first
        while cur:
            dummy.next = Node(cur.val)
            nodes_dict[cur] = dummy.next # store old and new lists in here
            cur = cur.next
            dummy = dummy.next

        # iterate over old list to form new one again
        cur = head
        new_cur = new_list.next

        while cur:
            if cur.random:
                new_cur.random = nodes_dict[cur.random]
            
            new_cur = new_cur.next
            cur = cur.next

        return new_list.next


l1 = Node(3)
l2 = Node(7)
l3 = Node(4)
l4 = Node(5)

l1.next = l2
l2.next = l3
l3.next = l4

l2.random = l4
l3.random = l1
l4.random = l2

s = Solution()
s.copyRandomList(l1)
# Input: head = [[3,null],[7,3],[4,0],[5,1]]

# Output: [[3,null],[7,3],[4,0],[5,1]]