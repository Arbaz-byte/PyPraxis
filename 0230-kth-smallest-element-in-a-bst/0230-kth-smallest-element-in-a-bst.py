# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int: # in-order traversal
        stack = []
        current = root

        while stack or current:
            # Travel to left most node 
            while current:
                stack.append(current)
                current = current.left
            
            # process the node 
            current = stack.pop()
            k -= 1

            # if reached kth value , return its value
            if k==0:
                return current.val
            
            # Move to right subtree
            current = current.right

        