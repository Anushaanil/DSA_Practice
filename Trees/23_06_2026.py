
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:

    def printTree(self, root):
        if not root:
            return None
        
        print('root', root.val)
        print('next', root.next.val if root.next else '#')

        # if root.left:
        #     print('left', root.left.val)
        # else:
        #     print('left', None)
        
        # if root.right:
        #     print('right', root.right.val)
        # else:
        #     print('right', None)
        
        self.printTree(root.left)
        self.printTree(root.right)

        return 
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])

        while q:
            nodes = len(q)
            for i in range(len(q)):
                cur_node = q.popleft()
                
                # If this isn't the last node of this level,
                # the next node is at the front of the queue.
                if i+1!=nodes:
                    cur_node.next = q[0]

                if cur_node.left:
                    q.append(cur_node.left)
                    
                if cur_node.right:
                    q.append(cur_node.right)
        return root


root = Node(1)
s1 = Node(2)
root.left = s1

s2 = Node(3)
root.right = s2

s3 = Node(4)
s1.left = s3

s4 = Node(5)
s1.right = s4

s5 = Node(7)
s2.right = s5

s = Solution()
s.connect(root)
# s.printTree(root)
        