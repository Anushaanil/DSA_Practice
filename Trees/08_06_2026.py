from collections import deque
from typing import Optional, List

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
#        /             / \
#       1             8  10

# BST -- Left node val < cur node val, Right node val > cur node val
# writing this in LC format --  [5,4,6,2,8,3,9,null,null,1,null,null,null,7,10]

# root = TreeNode(5)

# l1 = TreeNode(3)
# root.left = l1

# l1_l2 = TreeNode(2)
# l1.left = l1_l2

# l1_r2_l3 = TreeNode(1)
# l1_l2.left = l1_r2_l3

# l1_r2 = TreeNode(4)
# l1.right = l1_r2

# r1 = TreeNode(7)
# root.right = r1

# r1_l2 = TreeNode(6)
# r1.left = r1_l2

# r1_r2 = TreeNode(9)
# r1.right = r1_r2

# r1_r2_l3 = TreeNode(8)
# r1_r2.left = r1_r2_l3

# r1_r2_r3 = TreeNode(10)
# r1_r2.right = r1_r2_r3


# subroot = TreeNode(7)
# s1 = TreeNode(6)
# subroot.left = s1

# s2 = TreeNode(9)
# subroot.right = s2

# s3 = TreeNode(8)
# s2.left = s3

# s4 = TreeNode(10)
# s2.right = s4
        
root = TreeNode(1)
s1 = TreeNode(2)
root.left = s1

s2 = TreeNode(3)
root.right = s2

s3 = TreeNode(8)
s2.left = s3

s4 = TreeNode(10)
s2.right = s4


class BinaryTree:
    def isSubtree(self, root, subRoot):
        def isSameTree(root, subRoot):
            if root is None and subRoot is None:
                return True
            
            if root is None or subRoot is None:
                return False
            
            if root.val!=subRoot.val:
                return False
            
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        l_tree = self.isSubtree(root.left, subRoot)

        r_tree = self.isSubtree(root.right, subRoot)

        # return root.val == subRoot.val
        print(l_tree, r_tree)
        return l_tree or r_tree
    
    def isValidBST(self, root) -> bool:
        def isValid(root, low, high):
            if root is None:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, high)

        return isValid(root, float('-inf'), float('inf'))

    def isValidBSTInorderSolution(self, root):
        prev = float('-inf')

        def inorder(root):
            nonlocal prev

            if root is None:
                return True
            
            if not inorder(root.left):
                return False
            
            if root.val <= prev:
                return False
            
            prev = root.val

            return inorder(root.right)
        
        return inorder(root)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None

        def inorder_traversal(root):
            # Left - Root - Right
            if root is None:
                return
            
            if self.ans is not None:
                return
            
            inorder_traversal(root.left)

            if self.ans is not None:
                return

            self.count+=1
            
            print(self.count, k)
            
            if k == self.count:
                print('answer is here', k, self.count, root.val)
                self.ans = root.val
                print('answer', self.ans)
                return
          
            inorder_traversal(root.right)

        inorder_traversal(root)
        return self.ans
    
    def kthSmallestListRecursion(self, root: Optional[TreeNode], k: int) -> int:
        self.values = []

        def inorder_traversal(root):
            if not root:
                return
            
            inorder_traversal(root.left)
            self.values.append(root.val)
            inorder_traversal(root.right)
        
        inorder_traversal(root)
        return self.values[k-1]
    
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
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildTreeHelper(left_boundary, right_boundary):
            
            if left_boundary > right_boundary:
                return None
            
            root_val = preorder[self.pre_index]
            self.pre_index+=1
            
            root = TreeNode(root_val)
            
            in_index = self.index_map[root.val]
            print(self.pre_index)

            # if self.pre_index > len(inorder):
            #     return root

            root.left = buildTreeHelper(left_boundary, in_index-1)
            root.right = buildTreeHelper(in_index+1, right_boundary)

            return root
        
        # can't use this map directly inside when slicing, because inorder array keeps shrinking and 
        # indices inside this are not valid for shrinked inorder arr, so use .index() if slicing is used.
        # but it uses o(n2) as new lists are created and index is searched across new list evry time.

        self.index_map = {val:i for i, val in enumerate(inorder)}

        if not inorder:
            return None
        
        self.pre_index = 0

        return buildTreeHelper(0, len(preorder)-1)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def computeMaxPath(root):
            
            if not root:
                return 0
            
            l_sum = max(0, self.maxPathSum(root.left))
            r_sum = max(0, self.maxPathSum(root.right))

            total_sum = root.val + l_sum + r_sum

            self.max_path_sum = max(self.max_path_sum, total_sum)

            return root.val + max(l_sum, r_sum)
        
        self.max_path_sum = float('-inf')
        computeMaxPath(root)
        return self.max_path_sum
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []

        def serialize_helper(root):
            if root is None:
                self.result.append("N")
                return None
            
            self.result.append(f"{root.val}")

            serialize_helper(root.left)
            serialize_helper(root.right)

        serialize_helper(root)

        return ','.join(self.result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.idx = 0

        def serialize_helper(data):
            print(data)

            if data[self.idx] == "N":
                self.idx +=1
                return None
            
            root = TreeNode(data[self.idx])

            self.idx +=1

            root.left = serialize_helper(data)
            root.right = serialize_helper(data)

            return root

        data = data.split(',')
        return serialize_helper(data)

bt = BinaryTree()
# print(bt.isSubtree(root, subroot))
# print(bt.isValidBST(root))
# print(bt.isValidBSTInorderSolution(root))
# print(bt.kthSmallest(root, 4))
# preorder = [1,2,3,4]
# inorder = [2,1,3,4]
# tree = bt.buildTree(preorder, inorder)

# bt.printTree(tree)
# print(bt.maxPathSum(root))

serialized_output = bt.serialize(root)
print(serialized_output)

deserialized_output = bt.deserialize(serialized_output)
bt.printTree(deserialized_output)