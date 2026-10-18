# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def push_left_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.push_left_nodes(root)

    def next(self) -> int:
        top_node = self.stack.pop()
        if top_node.right:
            self.push_left_nodes(top_node.right)
        return top_node.val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()