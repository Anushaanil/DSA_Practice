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
        
# The most important comments you should retain mentally are:

# Preorder  -> ROOT LEFT RIGHT
# Inorder   -> LEFT ROOT RIGHT
# Postorder -> LEFT RIGHT ROOT

# Queue  -> BFS -> FIFO
# Stack  -> DFS -> LIFO

# and:

# Recursion = implicit stack
# Iterative DFS = explicit stack
# BFS = queue

# Those three ideas alone explain almost all traversal logic.

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


class BTTraversals:

    # PREORDER
    # ROOT -> LEFT -> RIGHT
    #
    # Main idea:
    # Process current node FIRST,
    # then recursively process left subtree,
    # then recursively process right subtree.
    #
    # Recursive call stack automatically remembers
    # where to return after subtree traversal.
    #
    # Output:
    # 1 2 4 5 8 3 6 7 9 10

    def pre_order_traversal(self, root):

        # Base condition:
        # stop recursion when node becomes None
        if root is None:
            return

        # Visit root first
        print(root.val)

        # Traverse left subtree
        self.pre_order_traversal(root.left)

        # Traverse right subtree
        self.pre_order_traversal(root.right)



    # POSTORDER
    # LEFT -> RIGHT -> ROOT
    #
    # Main idea:
    # process children first,
    # process root LAST.
    #
    # Useful when deleting/freeing tree
    # because child nodes are processed first.
    #
    # Output:
    # 4 8 5 2 6 9 10 7 3 1

    def post_order_traversal(self, root):

        if root is None:
            return

        # Go fully left
        self.post_order_traversal(root.left)

        # Then fully right
        self.post_order_traversal(root.right)

        # Finally process root
        print(root.val)



    # INORDER
    # LEFT -> ROOT -> RIGHT
    #
    # Important property:
    # inorder traversal of BST gives sorted order.
    #
    # Output:
    # 4 2 8 5 1 6 3 9 7 10

    def in_order_traversal(self, root):

        if root is None:
            return

        # Traverse left subtree first
        self.in_order_traversal(root.left)

        # Process root in middle
        print(root.val)

        # Traverse right subtree
        self.in_order_traversal(root.right)



    # LEVEL ORDER TRAVERSAL (BFS)
    #
    # Uses QUEUE because BFS requires FIFO order.
    #
    # deque is used because:
    # popleft() in list is O(n)
    # popleft() in deque is O(1)
    #
    # Queue stores nodes whose turn
    # to process has not yet come.
    #
    # Output:
    # 1 2 3 4 5 6 7 8 9 10

    def level_order_traversal(self, root):

        if root is None:
            return

        # Start BFS from root
        queue = deque([root])

        # Continue until queue becomes empty
        while queue:

            # Remove oldest inserted node
            current = queue.popleft()

            # Process current node
            print(current.val)

            # Add left child for future processing
            if current.left:
                queue.append(current.left)

            # Add right child for future processing
            if current.right:
                queue.append(current.right)



    # ITERATIVE PREORDER
    # ROOT -> LEFT -> RIGHT
    #
    # Uses STACK because stack mimics recursion.
    #
    # Important trick:
    # push RIGHT first,
    # then LEFT.
    #
    # Because stack is LIFO,
    # LEFT gets processed first.

    def iterative_pre_order_traversal(self, root):

        if root is None:
            return

        stack = [root]

        while stack:

            # Take latest inserted node
            current = stack.pop()

            print(current.val)

            # Push right first
            if current.right:
                stack.append(current.right)

            # Push left later so it comes out first
            if current.left:
                stack.append(current.left)



    # ITERATIVE INORDER
    # LEFT -> ROOT -> RIGHT
    #
    # Main idea:
    #
    # Keep going LEFT and push all nodes into stack.
    #
    # Once left becomes None:
    # pop node,
    # process it,
    # then move to right subtree.
    #
    # Stack stores ancestors waiting
    # for their turn to be processed.

    def iterative_in_order_traversal(self, root):

        stack = []

        # current pointer moves through tree
        current = root

        # Continue until:
        # no nodes left in stack
        # AND current becomes None
        while stack or current:

            # Go fully LEFT
            while current:

                # Save ancestor before going deeper
                stack.append(current)

                current = current.left

            # Leftmost node reached
            # retrieve latest ancestor
            current = stack.pop()

            # Process node
            print(current.val)

            # Move to right subtree
            current = current.right



    # Another iterative inorder version
    # Same logic but stores result in list

    def iterative_inorder(self, root):

        st = []
        node = root
        inorder = []

        while True:

            # Keep moving left
            if node is not None:

                st.append(node)
                node = node.left

            else:

                # Traversal completed
                if not st:
                    break

                # Process ancestor
                node = st.pop()

                inorder.append(node.val)

                # Explore right subtree
                node = node.right

        return inorder



    # ITERATIVE POSTORDER
    # LEFT -> RIGHT -> ROOT
    # using 2 stacks approach

    # Trick:
    #
    # Reverse preorder logic.
    #
    # preorder:
    # ROOT -> LEFT -> RIGHT
    #
    # modified preorder:
    # ROOT -> RIGHT -> LEFT
    #
    # reversing result gives:
    # LEFT -> RIGHT -> ROOT
    #
    # input_stack handles traversal
    # output_stack stores reverse order

    def iterative_post_order_traversal_2_stacks(self, root):

        if root is None:
            return

        input_stack = [root]
        output_stack = []

        while input_stack:

            node = input_stack.pop()

            # Store root-right-left order
            output_stack.append(node.val)

            # Left pushed first
            if node.left:
                input_stack.append(node.left)

            # Right pushed later
            # so processed first
            if node.right:
                input_stack.append(node.right)

        # Reverse order gives postorder
        while output_stack:
            print(output_stack.pop())

    def iterative_post_order_traversal_1_stack(self, root):

        stack = []

        # current pointer used for traversal
        cur = root

        post_order = []

        # Continue until:
        # no current node
        # AND stack empty
        while cur or stack:

            # Go fully LEFT
            if cur:

                stack.append(cur)

                cur = cur.left

            else:

                # Check right subtree of top node
                temp = stack[-1].right

                # No right subtree exists
                if not temp:

                    # Safe to process node
                    temp = stack.pop()

                    post_order.append(temp.val)

                    # IMPORTANT:
                    # Keep processing ancestors
                    # while coming back from RIGHT subtree
                    while stack and temp == stack[-1].right:

                        temp = stack.pop()

                        post_order.append(temp.val)

                else:
                    # Right subtree exists
                    # process it first
                    cur = temp

        return post_order


b = BTTraversals()

# b.pre_order_traversal(root)

# b.post_order_traversal(root)

# b.in_order_traversal(root)

# b.level_order_traversal(root)

# b.iterative_pre_order_traversal(root)

# b.iterative_in_order_traversal(root)

# b.iterative_post_order_traversal_2_stacks(root)
# print(b.iterative_post_order_traversal_1_stack(root))