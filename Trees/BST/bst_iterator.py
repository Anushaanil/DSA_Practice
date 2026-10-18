# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    """
    The rule to rememberstack
    - When initializing or processing a right subtree: push the node and all its left descendants onto the stack.
    - When calling next(): pop the top node and return its value.
    - When checking hasNext(): return whether the stack is non-empty.
    """
    
    def push_left_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.push_left_nodes(root)

    def next(self) -> int:
        if not self.stack:
            return None
        
        top_node = self.stack.pop()

        if top_node.right:
            self.push_left_nodes(top_node.right)

        # print(top_node.val)
        return top_node.val

    def hasNext(self) -> bool:
        # print(len(self.stack)>0)
        return len(self.stack)>0
        
root = TreeNode(7)

l1 = TreeNode(3)
l2 = TreeNode(9)


r1 = TreeNode(15)
r2 = TreeNode(20)

root.left = l1
root.right = r1
r1.left = l2
r1.right = r2


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
    
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation [7, 3, 15, None, None, 9, 20]
bSTIterator = BSTIterator(root)
bSTIterator.next();    # return 3
bSTIterator.next();    # return 7
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 9
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 15
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 20
bSTIterator.hasNext(); # return False

# class BSTIterator:

#     def __init__(self, root: TreeNode | None):
#         self.stack = []
#         self._push_left(root)        

#     def _push_left(self, node):
#         while node:
#             self.stack.append(node)
#             node = node.left

#     def next(self) -> int:
#         node = self.stack.pop()
#         self._push_left(node.right)
#         return node.val

#     def hasNext(self) -> bool:
#         return bool(self.stack)