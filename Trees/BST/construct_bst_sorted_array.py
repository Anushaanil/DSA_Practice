# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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
    
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def constructTree(l, r):
            if l > r:
                return
            
            m = (l+r)//2
            root = TreeNode(nums[m])

            root.left = constructTree(l, m-1)
            root.right = constructTree(m+1, r)

            return root
        
        return constructTree(0, len(nums)-1)
    

s = Solution()
nums = [-10,-3,0,5,9]
root = s.sortedArrayToBST(nums)
s.printTree(root)