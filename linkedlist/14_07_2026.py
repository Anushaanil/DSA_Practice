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

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # self.traverse(head)
        # print('\n')
        if not head or not head.next:
            return

        # 1. find middle point using fast and slow pointers
        fast = slow = head

        while fast and fast.next:
            # middle_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # seperating 2 lists
        # middle_prev.next = None
        middle = slow.next
        slow.next = None

        prev = None

        # 2. reverse from middle to end
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp

        # reorder now using starting and middle pointer
        cur = head
        while prev:
            temp1 = cur.next
            temp2 = prev.next

            cur.next = prev
            prev.next = temp1

            cur = temp1
            prev = temp2

        self.traverse(head)
        return head
        
        # I had tried this by visualizing the way in head, 
        # but it's inefficient and struggles in mid
        # dummy = head
        # cur = head
        # prev = None

        # while dummy!=prev:
        #     while cur.next:
        #         prev = cur
        #         cur = cur.next
            
        #     print(prev.val, cur.val)
            
        #     if cur == prev:
        #         return head
            
        #     temp = dummy.next
        #     dummy.next = cur
        #     cur.next = temp

        #     dummy = temp
        #     cur = prev

        #     print('temp', temp.val)
        #     print('dummy', dummy.val)
        #     print('cur', cur.val)
        #     print('prev', prev.val)

        # return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return None

        cur = head
        total_nodes = 0

        while cur:
            total_nodes+=1
            cur = cur.next

        current_count = 0
        prev = None
        cur = head

        while cur:
            current_count +=1
            target = total_nodes - current_count + 1
            if target == n:
                if not prev:
                    return head.next
                prev.next = cur.next
                break

            prev = cur
            cur = cur.next

        return head
    

# head = [2,4,6,8]
# Output: [2,8,4,6]

l1 = ListNode(2)
l2 = ListNode(4)
l1.next = l2
# l3 = ListNode(6)
# l2.next = l3
# l4 = ListNode(8)
# l3.next = l4
# l5 = ListNode(10)
# l4.next = l5

s = Solution()
head = l1
# print(s.reorderList(head))
ans = s.removeNthFromEnd(head, 2)
s.traverse(ans)