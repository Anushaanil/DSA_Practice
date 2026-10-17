# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        queue = deque([root])
        right_side_nodes = []

        while queue:
            qsize = len(queue)

            for i in range(qsize):
                cur = queue.popleft()

                if i == qsize-1:
                    right_side_nodes.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return right_side_nodes

root = TreeNode(1)
a = TreeNode(2)
root.left = a

b = TreeNode(3)
root.right = b

d = TreeNode(4)
a.left = d

c = TreeNode(5)
d.left = c

s = Solution()
print(s.rightSideView(root))
