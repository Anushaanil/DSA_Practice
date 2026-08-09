from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def traverse(self, head):
        cur = head
        while cur:
            print(cur.val if cur else "0")
            cur = cur.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        cur = dummy

        while l1 or l2:
            if l1:
                l1_num = l1.val
                l1 = l1.next
            else:
                l1_num = 0
            
            if l2:
                l2_num = l2.val
                l2 = l2.next
            else:
                l2_num = 0

            cur_sum = l1_num + l2_num + carry
            carry = cur_sum//10
            cur.next = ListNode(cur_sum % 10)
            cur = cur.next

        if carry:
            cur.next = ListNode(carry)
      
        return dummy.next

l1 = ListNode(5)
l2 = ListNode(4)
l3 = ListNode(5)
l1.next = l2
l2.next = l3

l4 = ListNode(4)
l5 = ListNode(6)
# l6 = ListNode(5)
l4.next = l5
# l5.next = l6

s = Solution()
ans = s.addTwoNumbers(l1, l4)
s.traverse(ans)