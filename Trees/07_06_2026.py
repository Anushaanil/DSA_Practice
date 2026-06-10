from collections import deque

# Basic binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# Constructing tree manually

#                5
#             /     \
#            3       7
#          /   \    /  \
#         2     4  6    9
#              /       / \
#             1       8  10

# BST -- Left node val < cur node val, Right node val > cur node val
# writing this in LC format --  [5,4,6,2,8,3,9,null,null,1,null,null,null,7,10]

root = TreeNode(5)

l1 = TreeNode(3)
root.left = l1

l1_l2 = TreeNode(2)
l1.left = l1_l2

l1_r2 = TreeNode(4)
l1.right = l1_r2

l1_r2_l3 = TreeNode(1)
l1_r2.left = l1_r2_l3

r1 = TreeNode(7)
root.right = r1

r1_l2 = TreeNode(6)
r1.left = r1_l2

r1_r2 = TreeNode(9)
r1.right = r1_r2

r1_r2_l3 = TreeNode(8)
r1_r2.left = r1_r2_l3

r1_r2_r3 = TreeNode(10)
r1_r2.right = r1_r2_r3

class BinarySearchTree:
    def lowestCommonAncestorIterative(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        while root:
            if p.val < root.val and q.val < root.val:        
                root = root.left
            
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            else:
                return root
    
    def lowestCommonAncestorRecursive(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:        
            return self.lowestCommonAncestorRecursive(root.left, p, q)
            
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorRecursive(root.right, p, q)
        
        return root
    
                
bst = BinarySearchTree()
res = bst.lowestCommonAncestorRecursive(root, TreeNode(6), TreeNode(8))
# print(res.val)


class BasicRecursionExercises:
    def hello(self, n):
        print("start: ", n)

        if n == 0:
            return
        
        self.hello(n-1)

        print("end: ", n)
    
    def addition_print(self, n):
        if n == 0:
            return 100

        x = self.addition_print(n-1)

        print(n, x)

        return x + 10


br = BasicRecursionExercises()
# br.hello(2)
print(br.addition_print(3))