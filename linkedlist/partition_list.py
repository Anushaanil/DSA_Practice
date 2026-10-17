# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def traverse(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next

    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        cur = head
        less_t_x_nodes = []
        greater_te_x_nodes = []

        while cur:
            if cur.val < x:
                less_t_x_nodes.append(cur)
            else:
                greater_te_x_nodes.append(cur)

            cur = cur.next
        
        less_t_x_nodes.extend(greater_te_x_nodes)
        
        if not less_t_x_nodes:
            return None

        for i in range(1, len(less_t_x_nodes)):
            less_t_x_nodes[i-1].next = less_t_x_nodes[i]
        
        less_t_x_nodes[-1].next = None
        
        return less_t_x_nodes[0]


l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(2)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

s = Solution()
head = l1
ans = s.partition(head, 3)
s.traverse(ans)