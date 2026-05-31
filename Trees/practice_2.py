from collections import deque

# Basic binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


# Constructing tree manually

#                1
#             /     \
#            2       3
#          /   \    /  \
#         4     5  6    7
#              /       / \
#             8       9  10

root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
root.right.right.right = TreeNode(10)
# root.right.right.right.right = TreeNode(11)


class BinaryTree:
    def max_depth_using_recursion(self, root):
        if root is None:
            return 0

        l_max = self.max_depth_using_recursion(root.left)
        r_max = self.max_depth_using_recursion(root.right)

        return 1 + max(l_max, r_max)
    

    def max_depth_using_BFS(self, root):

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                element = queue.popleft()
                print(element.val)

                if element.left:
                    queue.append(element.left)
                
                if element.right:
                    queue.append(element.right)
                
            depth+=1

        return depth
    
    def dfs_height(self, root):
        if root is None:
            return 0
        
        left_height = self.dfs_height(root.left)
        if left_height == -1: return -1

        right_height = self.dfs_height(root.right)
        if right_height == -1: return -1

        if abs(left_height - right_height) > 1 :
            return -1
        
        return 1 + max(left_height, right_height)

    def is_balanced_binary_tree(self, root):
        return self.dfs_height(root)!=-1
    
    def max_height_for_diameter(self, root):
        if root is None:
            return 0
        
        l_h = self.max_height_for_diameter(root.left)
        r_h = self.max_height_for_diameter(root.right)

        self.max_diameter = max(self.max_diameter, l_h + r_h)

        return 1 + max(l_h, r_h)

    def diameter_binary_tree(self, root):
        self.max_diameter = 0
        self.max_height_for_diameter(root)
        return self.max_diameter
    
bt = BinaryTree()
# print(bt.max_depth_using_recursion(root))
# print(bt.max_depth_using_BFS(root))
# print(bt.is_balanced_binary_tree(root))
print(bt.diameter_binary_tree(root))