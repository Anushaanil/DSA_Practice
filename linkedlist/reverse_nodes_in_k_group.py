# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionBF:
    def traverse(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
    
    def reversenodes(self, cur_list, start, end):
        next_node = cur_list[end].next

        for i in range(end, start, -1):
            cur_list[i].next = cur_list[i-1]

        cur_list[start].next = next_node
        
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        cur_list = []
        cur = head

        while cur:
            cur_list.append(cur)
            cur = cur.next

        n = len(cur_list)

        for start in range(0, n, k):
            end = start + k - 1
            # only operate on complete group
            if end >=n:
                break

            # reverse the nodes
            self.reversenodes(cur_list, start, end)

        # rejoin the left out nodes
        for i in range(0, n, k):
            if i + 2*k - 1 < n:
                cur_list[i].next = cur_list[i + 2*k - 1]
                print(i, i+2*k-1)

        return cur_list[k - 1] if n >= k else head


class SolutionOptimal:
    def traverse(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
    
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
        """ 
        Steps
        1. Create dummy node and make it head and prev_group_tail
        2. iterate from starting of group till k nodes to know the kth node
        3. cur would become cur.next which is starting of next group, store that as next_group
        4. 
        """
        
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
                prev_node.next = next_node
                temp = next_node

        return head


# s = SolutionBF()
s = SolutionOptimal()
l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l2.next = l3
l4 = ListNode(4)
l3.next = l4
l5 = ListNode(5)
l4.next = l5
l6 = ListNode(6)
l5.next = l6

head = l1
k = 2

result_node = s.reverseKGroup(head, k)
s.traverse(result_node)