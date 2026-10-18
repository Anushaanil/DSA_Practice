# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # inorder traversal in BST gives sorted order, 
        # add them to list and return it's kth element as soon as found.
        ans = None
        elements = []
        
        def inorder_traversal(node, k):
            nonlocal ans, elements

            if not node:
                return
            
            # left node first

            if node.left: 
                inorder_traversal(node.left, k)
                
            elements.append(node.val)

            if len(elements) == k:
                ans = elements[-1]
                return

            if node.right: 
                inorder_traversal(node.right, k)

        inorder_traversal(root, k)
        return ans

    def kthSmallestNoSpace(self, root, k):
        ans = None
        count = k
        
        def inorder_traversal(node):
            nonlocal ans, count

            if not node:
                return
            
            # left node first
            inorder_traversal(node.left)
            count-=1

            if count == 0:
                ans = node.val
                return

            inorder_traversal(node.right)

        inorder_traversal(root)
        return ans
    
# root = TreeNode(3)

# l1 = TreeNode(1)
# l2 = TreeNode(4)



# r1 = TreeNode(2)
# # r2 = TreeNode(20)

# root.left = l1
# root.right = l2
# l1.right = r1

root = TreeNode(4)

l1 = TreeNode(2)
l2 = TreeNode(6)
l3 = TreeNode(1)
l4 = TreeNode(3)


root.left = l1
root.right = l2
l1.left = l3
l1.right = l4

s = Solution()
ans = s.kthSmallestNoSpace(root, 3)
print(ans)