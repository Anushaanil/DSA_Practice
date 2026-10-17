# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversenodes(self, start, end):
        prev = None
        cur = start

        while cur and cur!=end:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


    def getkthnode(self, cur, k):
        while cur and k > 1:
            cur = cur.next
            k-=1
        return cur
        

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        temp = head
        prev_node = None
        next_node = None

        while temp:
            # find the kth node
            kthnode = self.getkthnode(temp, k)
            if not kthnode:
                if prev_node:
                    prev_node.next = temp
                break
            else:
                next_node = kthnode.next
                kthnode.next = None
                # reverse nodes
                self.reversenodes(temp, next_node)

                if temp == head:
                    head = kthnode
                else:
                    prev_node.next = kthnode

                prev_node = temp
                temp = next_node

        return head