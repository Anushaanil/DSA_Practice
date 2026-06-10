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

root.left = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(2)
root.right.right.left = TreeNode(9)
root.right.right.right = TreeNode(10)
# root.right.right.right.right = TreeNode(11)


class BinaryTree:
    def level_order_traversal_print_nodes(self, root):
        if not root:
            return None

        queue = deque([root])
        result = []

        while queue:
            current_level_nodes = []

            for _ in range(len(queue)):
                cur_node = queue.popleft()
                current_level_nodes.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                    
                if cur_node.right:
                    queue.append(cur_node.right)
                    
            if current_level_nodes: result.append(current_level_nodes)

        return result
    
    def rightSideView(self, root):
        if root is None:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            res = None
            qsize = len(queue)

            for i in range(qsize):
                cur_node = queue.popleft()

                if i == qsize-1:
                    res = cur_node.val
 
                if cur_node.left:
                    queue.append(cur_node.left)
                    # if not res:res = cur_node.left.val
                
                if cur_node.right:
                    queue.append(cur_node.right)
                    # res = cur_node.right.val
                
            result.append(res)
                

        return result

    def goodNodes(self, root):
        def compute_goodnodes_count(root, max_so_far):
            if not root:
                return 0

            count = 0 

            if root.val >= max_so_far:
                count+=1
                # max_so_far = root.val

            new_max = max(max_so_far, root.val)
            
            l_count = compute_goodnodes_count(root.left, new_max)
            r_count = compute_goodnodes_count(root.right, new_max)

            return count + l_count + r_count
        
        return compute_goodnodes_count(root, root.val)
    

bt = BinaryTree()
bt.level_order_traversal_print_nodes(root)