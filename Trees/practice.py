# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)

l1 = TreeNode(2)
l2 = TreeNode(4)
l3 = TreeNode(5)
l4 = TreeNode(7)

r1 = TreeNode(3)
r2 = TreeNode(6)
r3 = TreeNode(8)
r4 = TreeNode(9)

root.left = l1
root.right = r1
l1.left = l2
r1.left = l3
r1.right = r2
r2.left = l4
r2.right = r3
r3.right = r4


class TreeSolution:
    def printTree(self, root):
        if not root:
            return None
        
        print('root', root.val)

        if root.left:
            print('left', root.left.val)
        else:
            print('left', None)
        
        if root.right:
            print('right', root.right.val)
        else:
            print('right', None)
        
        self.printTree(root.left)
        self.printTree(root.right)

        return 
    
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        if root.left:
            print('left', root.left.val)
        else:
            print('left', None)

        left_depth = self.maxDepth(root.left)

        if root.right:
            print('right', root.right.val)
        else:
            print('right', None)
        
        right_depth = self.maxDepth(root.right)

        print('depth', left_depth, right_depth)
        print('sol', 1 + max(left_depth, right_depth))
        return 1 + max(left_depth, right_depth)
    
    def leafCount(self, root):
        # Base case 
        if root is None:
            return 0

        # conditional case for leaf
        if root.left is None and root.right is None:
            return 1
        
        l_nodes_count = self.leafCount(root.left)
        r_nodes_count = self.leafCount(root.right)
        
        return l_nodes_count + r_nodes_count
    
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val!=q.val:
            return False
        
        left_check = self.isSameTree(p.left, q.left)
        right_check = self.isSameTree(p.right, q.right)

        return left_check and right_check
            
    def invert_binary_tree(self, root):
        if not root:
            return None
        
        # temp = root.left
        # root.left = root.right
        # root.right = temp

        root.left, root.right = root.right, root.left

        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        return root
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        if left.val != right.val:
            return False
        
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root) -> bool:
        if not root:
            return True

        return self.isMirror(root.left, root.right)
    
    def buildTreeInPost(self, inorder, postorder):

        if not inorder:
            return None
        
        inorder_map = {val:idx for idx, val in enumerate(inorder)}

        root_val = postorder[-1]
        root = TreeNode(root_val)

        # idx = inorder.index(root_val)
        idx = inorder_map[root_val]
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx+1:]

        left_postorder = postorder[:idx]
        right_postorder = postorder[idx:-1]

        print('order1 left', left_inorder, left_postorder)

        root.left = self.buildTree(left_inorder, left_postorder)
        print('left val', root.left.val if root.left else None)

        print('order2 right', right_inorder, right_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        print('right val', root.right.val if root.right else None)

        return root
    
    def buildTreeInPre(self, preorder, inorder):
        if not inorder:
            return None
        
        inorder_map = {val:i for i, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left, right):
            nonlocal pre_idx

            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx+=1

            root = TreeNode(root_val)
            idx = inorder_map[root_val]

            # build left subtree first
            root.left = helper(left, idx-1)
            root.right = helper(idx+1, right)

            return root

        return helper(0, len(preorder)-1)

    def pathSum(self, root, remaining_target):
        
        if not root:
            return False
        
        remaining_target = remaining_target - root.val
        print('sum', remaining_target)

        if not root.left and not root.right:
            return remaining_target == 0
        
        l_sum = self.pathSum(root.left, remaining_target)
        print('l', l_sum)

        r_sum = self.pathSum(root.right, remaining_target)
        print('r', r_sum)

        return l_sum or r_sum
        
        
t = TreeSolution()
print(t.pathSum(root, 18))
# tree = t.buildTreeInPre([3,9,20,15,7], [9,3,15,20,7])
# t.printTree(tree)
# print()


# print(t.maxDepth(root))
# print(t.leafCount(root))
p = TreeNode(1)
p1 = TreeNode(2)
# p2 = TreeNode(3)
p.left = p1

q = TreeNode(1)
q1 = TreeNode(2)
q.right = q1

# print(t.isSameTree(p, q))
# t.printTree(root)
# print("\n")
# res = t.invert_binary_tree(root)
# t.printTree(res)

p = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(2)

l2 = TreeNode(3)
r2 = TreeNode(4)

l3 = TreeNode(4)
r3 = TreeNode(3)
p.left = l1
p.right = r1
l1.left = l2
l1.right = r2
r1.left = l3
r1.right = l3

# print(t.isSymmetric(p))