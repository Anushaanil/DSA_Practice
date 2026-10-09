# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
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